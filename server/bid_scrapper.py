from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

def setup_driver():
    """Configure Chrome to look more like a normal user and avoid detection."""
    chrome_options = Options()
    # Remove automated control indicators
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # Add common browser arguments
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-gpu')
    
    # Set a common, modern user agent
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    chrome_options.add_argument(f'user-agent={user_agent}')
    
    # Create driver with options
    driver = webdriver.Chrome(options=chrome_options)
    
    # Execute CDP commands to further mask automation
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent})
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': '''
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
        '''
    })
    
    return driver

def get_bid_data_with_selenium():
    """
    Uses Selenium to load the GEM bids page and execute the original
    JavaScript function to fetch data, bypassing bot detection.
    """
    driver = setup_driver()
    
    try:
        # 1. Navigate to the main bids page
        print("🌐 Navigating to GEM bids page...")
        driver.get("https://bidplus.gem.gov.in/all-bids")
        time.sleep(5)  # Let the page load completely
        
        print("✅ Page loaded. Checking for page variables...")
        
        # 2. Execute JavaScript to check if critical page variables are loaded
        check_script = """
        return {
            has_jquery: typeof $ !== 'undefined',
            has_param: typeof window.param !== 'undefined',
            has_filter: typeof window.filter !== 'undefined',
            has_csrf: typeof window.csrf_bd_gem_nk !== 'undefined',
            page_title: document.title
        };
        """
        
        page_status = driver.execute_script(check_script)
        print(f"📋 Page Status: {json.dumps(page_status, indent=2)}")
        
        # 3. Inject and execute the original loadBids() function
        # Using the exact function you extracted from the page
        print("🚀 Executing original loadBids() function...")
        
        # First, define the function in the page context
        load_bids_script = """
        // Define the function exactly as on the original page
        window.loadBids = function(page = null) {
            return new Promise((resolve, reject) => {
                $('#bidCard').html('<div style="text-align:center;margin-top:100px;"><img src="resources/images/gemloader.gif"  /></div>');
                var bidStatus = '["Not Evaluated","Technical Evaluation","Financial Evaluation","Bid Award"]';
                var bidStatusJson = JSON.parse(bidStatus);
                var postdata = {};
                if (page) {
                    postdata['page'] = page;
                }
                postdata['param'] = window.param;
                postdata['filter'] = window.filter;
                
                $.ajax({
                    type: 'POST',
                    url: 'https://bidplus.gem.gov.in/all-bids-data',
                    dataType: 'json',
                    data: {'payload': JSON.stringify(postdata), 'csrf_bd_gem_nk': window.csrf_bd_gem_nk},
                    success: function (data) {
                        window.lastAjaxResult = data; // Store for retrieval
                        resolve(data);
                    },
                    error: function (xhr, status, error) {
                        reject({
                            status: xhr.status,
                            statusText: xhr.statusText,
                            error: error,
                            response: xhr.responseJSON
                        });
                    }
                });
            });
        };
        
        // Return success
        return "loadBids function defined successfully";
        """
        
        # Inject the function
        driver.execute_script(load_bids_script)
        
        # 4. Execute the function to get page 1 data
        print("📥 Fetching bid data (Page 1)...")
        
        # Execute and wait for result
        result_script = """
        return window.loadBids(1)
            .then(data => {
                return { success: true, data: data };
            })
            .catch(error => {
                return { success: false, error: error };
            });
        """
        
        # Selenium can't directly handle Promises, so we use execute_async_script
        result = driver.execute_async_script("""
        var callback = arguments[arguments.length - 1];
        window.loadBids(1)
            .then(function(data) {
                callback({ success: true, data: data });
            })
            .catch(function(error) {
                callback({ success: false, error: error });
            });
        """)
        
        # 5. Process the result
        if result and result.get('success'):
            data = result.get('data')
            print(" SUCCESS! Data retrieved via original page function.")
            
            # Save the data
            timestamp = int(time.time())
            filename = f"gem_bids_selenium_{timestamp}.json"
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print(f"💾 Data saved to: {filename}")
            
            # Parse and display summary
            if data and data.get('code') == 200:
                response = data.get('response', {}).get('response', {})
                docs = response.get('docs', [])
                print(f"📊 Total records found: {response.get('numFound', 0)}")
                print(f"📄 Documents retrieved: {len(docs)}")
                
                if docs:
                    print("\n📋 Sample bids (first 3):")
                    for i, doc in enumerate(docs[:3], 1):
                        bid_no = doc.get('b_bid_number', 'N/A')
                        item_name = doc.get('b_category_name', ['N/A'])[0]
                        print(f"{i}. {bid_no} - {item_name[:60]}...")
            
            return data
        else:
            error = result.get('error', {}) if result else "No result"
            print(f"❌ Failed to fetch data. Error: {json.dumps(error, indent=2)}")
            return None
            
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        import traceback
        traceback.print_exc()
        return None
        
    finally:
        # Keep browser open for inspection, close manually
        print("\n⚠️ Keeping browser open for 30 seconds for inspection...")
        print("   Close the browser window when done, or let it close automatically.")
        time.sleep(30)
        driver.quit()
        print("✅ Browser closed.")

def fetch_multiple_pages_with_selenium(start_page=1, end_page=3):
    """
    Fetch multiple pages by simulating clicks on the pagination
    or by calling loadBids() with different page numbers.
    """
    print(f"\n📚 Fetching pages {start_page} to {end_page}...")
    
    driver = setup_driver()
    all_bids = []
    
    try:
        # Navigate to page
        driver.get("https://bidplus.gem.gov.in/all-bids")
        time.sleep(5)
        
        # Inject the loadBids function
        driver.execute_script("""
        window.loadBids = function(page = null) {
            return new Promise((resolve, reject) => {
                var postdata = {
                    param: window.param || "",
                    filter: window.filter || {},
                    page: page || 1
                };
                
                $.ajax({
                    type: 'POST',
                    url: '/all-bids-data',
                    dataType: 'json',
                    data: {
                        'payload': JSON.stringify(postdata),
                        'csrf_bd_gem_nk': window.csrf_bd_gem_nk
                    },
                    success: function(data) {
                        resolve(data);
                    },
                    error: function(xhr, status, error) {
                        reject(error);
                    }
                });
            });
        };
        """)
        
        for page in range(start_page, end_page + 1):
            print(f"\n📄 Fetching page {page}...")
            
            try:
                # Execute for each page
                result = driver.execute_async_script(f"""
                var callback = arguments[arguments.length - 1];
                window.loadBids({page})
                    .then(function(data) {{
                        callback({{ success: true, data: data }});
                    }})
                    .catch(function(error) {{
                        callback({{ success: false, error: error }});
                    }});
                """)
                
                time.sleep(2)  # Be polite between requests
                
                if result and result.get('success'):
                    data = result.get('data')
                    if data and data.get('code') == 200:
                        docs = data.get('response', {}).get('response', {}).get('docs', [])
                        if docs:
                            all_bids.extend(docs)
                            print(f"✅ Page {page}: Found {len(docs)} bids (Total: {len(all_bids)})")
                        else:
                            print(f"⚠️ Page {page}: No documents found")
                            break
                    else:
                        print(f"❌ Page {page}: Invalid response code")
                        break
                else:
                    print(f"❌ Page {page}: Failed to fetch")
                    break
                    
            except Exception as e:
                print(f"❌ Error on page {page}: {e}")
                break 
        
        # Save all collected data
        if all_bids:
            timestamp = int(time.time())
            filename = f"gem_all_pages_{timestamp}.json"
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(all_bids, f, indent=2, ensure_ascii=False)
            
            print(f"\n💾 All pages saved to: {filename}")
            print(f"📊 Total bids collected: {len(all_bids)}")
            
            # Show summary by organization
            org_counts = {}
            for bid in all_bids:
                org = bid.get('ba_official_details_deptName', 'Unknown')
                org_counts[org] = org_counts.get(org, 0) + 1
            
            print("\n🏢 Top Organizations:")
            for org, count in sorted(org_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
                print(f"  • {org}: {count} bids")
        
        return all_bids
        
    except Exception as e:
        print(f"❌ Error in multi-page fetch: {e}")
        return None
    finally:
        driver.quit()

# Main execution
if __name__ == "__main__":
    print("=" * 70)
    print("🚀 GEM BID+ - Selenium-Based Data Extractor")
    print("=" * 70)
    print("This script uses browser automation to bypass IP blocking")
    print("by executing the original page JavaScript.")
    print("-" * 70)
    
    print("\nChoose an option:")
    print("1. Test single page fetch (Recommended first)")
    print("2. Fetch multiple pages (e.g., 1-3)")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == '2':
        try:
            pages = int(input("How many pages to fetch? (1-5 recommended): ").strip())
            pages = max(1, min(5, pages))  # Safety limit
        except:
            pages = 3
            print(f"⚠️ Using default: {pages} pages")
        
        fetch_multiple_pages_with_selenium(1, pages)
    else:
        get_bid_data_with_selenium()
    
    print("\n" + "=" * 70)
    print("✨ Process completed!")
    print("=" * 70)





from playwright.async_api import async_playwright
from datetime import datetime
import asyncio
from playwright.sync_api import sync_playwright


# async def capture_bids():
#     """Directly monitor and capture the specific API endpoint"""
    
#     print("🎯 DIRECT API CAPTURE MODE")
#     print("=" * 60)
    
#     captured_data = []
    
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
        
#         # Create a page and listen for requests BEFORE navigating
#         page = await browser.new_page()
        
#         # Set up request interception to see ALL requests
#         await page.route('**', lambda route: route.continue_())
        
#         # Function to capture responses
#         async def capture_response(response):
#             if 'https://bidplus.gem.gov.in/all-bids-data' in response.url:
#                 try:
#                     print(f"\n🎯 CAPTURED TARGET API!")
#                     print(f"   URL: {response.url}")
#                     print(f"   Method: {response.request.method}")
#                     print(f"   Status: {response.status}")
                    
#                     # Get request headers
#                     request_headers = response.request.headers
#                     print(f"   Request Headers:")
#                     for key, value in request_headers.items():
#                         if any(k in key.lower() for k in ['cookie', 'authorization', 'token', 'csrf']):
#                             print(f"     {key}: [REDACTED]")
                    
#                     # Get response data
#                     data = await response.json()
                    
#                     # Save the complete data
#                     entry = {
#                         'timestamp': datetime.now().isoformat(),
#                         'url': response.url,
#                         'method': response.request.method,
#                         'status': response.status,
#                         'request_headers': dict(request_headers),
#                         'response_headers': dict(response.headers),
#                         'request_body': await response.request.post_data_json() if response.request.method == 'POST' else None,
#                         'data': data
#                     }
                    
#                     captured_data.append(entry)
                    
#                     # Save immediately
#                     filename = f"direct_capture_{int(time.time())}.json"
#                     with open(filename, 'w', encoding='utf-8') as f:
#                         json.dump(entry, f, indent=2, ensure_ascii=False)
#                     print(f"💾 Saved: {filename}")
                    
#                     # Show response structure
#                     if isinstance(data, dict):
#                         print(f"📊 Response keys: {list(data.keys())}")
#                         if 'response' in data:
#                             if 'response' in data['response']:
#                                 docs = data['response']['response'].get('docs', [])
#                                 print(f"   📄 Found {len(docs)} bid documents")
#                                 if docs:
#                                     print(f"   📝 First bid ID: {docs[0].get('id', 'N/A')}")
                    
#                 except Exception as e:
#                     print(f"❌ Error capturing response: {e}")
        
#         page.on('response', capture_response)
        
#         try:
#             print("\n🌐 Navigating to page...")
#             await page.goto('https://bidplus.gem.gov.in/all-bids', wait_until='networkidle')
            
#             # Open DevTools to monitor network
#             await page.evaluate("window.openDevTools = true;")
            
#             print("\n🔄 Now monitoring for API calls...")
#             print("   Interact with the page to trigger API calls")
#             print("   Try: Scrolling, clicking pagination, changing filters")
#             print("   Press Ctrl+C in terminal when done")
            
#             # Keep running until interrupted
#             try:
#                 while True:
#                     await page.wait_for_timeout(1000)
#             except KeyboardInterrupt:
#                 print("\n🛑 Manual interruption - stopping capture")
            
#             # Save all captured data
#             if captured_data:
#                 return {'status': 'success', 'data': captured_data}
#                 with open("direct_api_capture_all.json", "w", encoding="utf-8") as f:
#                     json.dump(captured_data, f, indent=2, ensure_ascii=False)
#                 print(f"\n💾 Saved {len(captured_data)} API captures to direct_api_capture_all.json")
#             else:
#                 print("\n❌ No API data captured")
                
#         finally:
#             await browser.close()
#             print("✅ Browser closed")

# bid_scraper.py
import json
import time
from datetime import datetime
from playwright.sync_api import sync_playwright
import sys
import os

def capture_gem_bids():
    """Synchronous Playwright function to capture GEM bids"""
    print("🎯 Starting GEM bid capture with Playwright...")
    
    captured_data = []
    
    try:
        with sync_playwright() as p:
            # Launch browser
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            # Set up request interception
            page.route("**", lambda route: route.continue_())
            
            def on_response(response):
                url = response.url
                if 'https://bidplus.gem.gov.in/all-bids-data' in url:
                    try:
                        print(f"\n✅ CAPTURED API: {url}")
                        
                        # Try to get JSON response
                        try:
                            data = response.json()
                            body = request.post_data_json()

                            page_no = body.get("page")
                            print(f"   Status: {response.status}")
                            print(f"   Method: {response.request.method}")
                            
                            # Create capture entry
                            entry = {
                                'timestamp': datetime.now().isoformat(),
                                'url': url,
                                'body': body,
                                #  '{"page":${page_no} ,"param":{"searchBid":"","searchType":"fullText"},"filter":{"bidStatusType":"ongoing_bids","byType":"all","highBidValue":"","byEndDate":{"from":"","to":""},"sort":"Bid-End-Date-Oldest"}}
                                #  ',
                                'status': response.status,
                                'request_headers': dict(response.request.headers),
                                'response_headers': dict(response.headers),
                                'data': data
                            }
                            
                            captured_data.append(entry)
                            
                            # Save individual file
                            filename = f"gem_capture_{int(time.time())}.json"
                            with open(filename, 'w', encoding='utf-8') as f:
                                json.dump(entry, f, indent=2, ensure_ascii=False)
                            print(f"💾 Saved to: {filename}")
                            
                            # Show bid count
                            if isinstance(data, dict):
                                docs = data.get('response', {}).get('response', {}).get('docs', [])
                                if docs:
                                    print(f"📊 Found {len(docs)} bids")
                                    print(f"📝 First bid: {docs[0].get('id', 'N/A')}")
                            
                        except Exception as json_error:
                            print(f"⚠️ Couldn't parse JSON: {json_error}")
                            
                    except Exception as e:
                        print(f"❌ Error processing response: {e}")
            
            # Attach response handler
            page.on("response", on_response)
            
            # Navigate to page
            print("\n🌐 Navigating to GEM bids page...")
            page.goto('https://bidplus.gem.gov.in/all-bids', wait_until='networkidle')
            print("✅ Page loaded successfully")
            
            # Wait and interact to trigger API calls
            print("\n🔄 Monitoring for API calls (30 seconds)...")
            
            # Try to trigger API calls
            page.wait_for_timeout(2000)
            
            # Try scrolling
            page.evaluate("window.scrollBy(0, 500)")
            page.wait_for_timeout(1000)
            
            # Try clicking on filters or pagination if they exist
            try:
                # Look for pagination buttons
                pagination_selectors = [
                    'a[href*="page="]',
                    'button:has-text("Next")',
                    'button:has-text("2")',
                    '.pagination a',
                    '.dataTables_paginate a'
                ]
                
                for selector in pagination_selectors:
                    elements = page.query_selector_all(selector)
                    if elements and len(elements) > 0:
                        elements[0].click()
                        page.wait_for_timeout(2000)
                        print(f"✅ Clicked pagination: {selector}")
                        break
                        
            except Exception as click_error:
                print(f"⚠️ Couldn't click pagination: {click_error}")
            
            # Monitor for remaining time
            start_time = time.time()
            while time.time() - start_time < 30:  # Monitor for 30 seconds total
                page.wait_for_timeout(1000)
                elapsed = int(time.time() - start_time)
                if elapsed % 10 == 0:
                    print(f"   Monitoring... {elapsed}/30 seconds")
            
            browser.close()
            print("✅ Browser closed")
            
            # Save all captures
            if captured_data:
                summary_file = "all_gem_captures.json"
                with open(summary_file, 'w', encoding='utf-8') as f:
                    json.dump({
                        'total_captures': len(captured_data),
                        'captures': captured_data
                    }, f, indent=2)
                
                print(f"\n🎉 Capture complete! Saved {len(captured_data)} API calls to {summary_file}")
                return captured_data
            else:
                print("\n⚠️ No API data was captured")
                return []
                
    except Exception as e:
        print(f"💥 Fatal error: {e}")
        import traceback
        traceback.print_exc()
        return []

    # Run when executed directly

async def capture_bids():
    """Directly monitor and capture the specific API endpoint"""
    
    print("🎯 DIRECT API CAPTURE MODE")
    print("=" * 60)
    
    captured_data = []
    
    try:
        # Use a different launch method for Windows
        async with async_playwright() as p:
            print("🚀 Launching browser with Windows-compatible settings...")
            
            # Use launch_persistent_context instead of launch() for better Windows support
            browser = await p.chromium.launch_persistent_context(
                user_data_dir="./playwright_data",  # Persistent data helps stability
                headless=True,
                args=[
                    '--disable-blink-features=AutomationControlled',
                    '--no-sandbox',
                    '--disable-dev-shm-usage',
                    '--disable-gpu'  # Optional: helps with some Windows issues
                ],
                timeout=60000  # Longer timeout
            )
            
            pages = browser.pages
            page = pages[0] if pages else await browser.new_page()
            
            # Set up request interception
            await page.route('**', lambda route: route.continue_())
            
            # Function to capture responses
            async def capture_response(response):
                try:
                    url = response.url
                    if 'https://bidplus.gem.gov.in/all-bids-data' in url:
                        print(f"\n🎯 CAPTURED TARGET API!")
                        print(f"   URL: {url}")
                        print(f"   Method: {response.request.method}")
                        print(f"   Status: {response.status}")
                        
                        # Get response data
                        try:
                            data = await response.json()
                            print(f"✅ Successfully parsed JSON response")
                        except:
                            text = await response.text()
                            print(f"⚠️ Response is not JSON, got {len(text)} chars")
                            return
                        
                        # Save the complete data
                        entry = {
                            'timestamp': datetime.now().isoformat(),
                            'url': url,
                            'method': response.request.method,
                            'status': response.status,
                            'data': data  # Simplified for now
                        }
                        
                        captured_data.append(entry)
                        
                        # Save immediately
                        filename = f"direct_capture_{int(time.time())}.json"
                        with open(filename, 'w', encoding='utf-8') as f:
                            json.dump(entry, f, indent=2, ensure_ascii=False)
                        print(f"💾 Saved: {filename}")
                        
                        # Show response structure
                        if isinstance(data, dict):
                            print(f"📊 Response keys: {list(data.keys())}")
                            
                except Exception as e:
                    print(f"❌ Error in response handler: {e}")
            
            page.on('response', capture_response)
            
            print("\n🌐 Navigating to page...")
            await page.goto(
                'https://bidplus.gem.gov.in/all-bids', 
                wait_until='domcontentloaded',  # Changed from 'networkidle'
                timeout=30000
            )
            
            print("✅ Page loaded successfully")
            print("\n🔄 Monitoring for API calls for 30 seconds...")
            
            # Monitor for a fixed time instead of infinite loop
            for i in range(30):  # 30 seconds
                await page.wait_for_timeout(1000)
                if i % 5 == 0:
                    print(f"   Still monitoring... ({i+1}/30 seconds)")
            
            print("\n⏰ Monitoring period complete")
            
            # Save all captured data
            if captured_data:
                with open("direct_api_capture_all.json", "w", encoding="utf-8") as f:
                    json.dump(captured_data, f, indent=2, ensure_ascii=False)
                print(f"\n💾 Saved {len(captured_data)} API captures to direct_api_capture_all.json")
                return {'status': 'success', 'count': len(captured_data), 'data': captured_data[0]['data']['response']['response']['docs'],'totalPages': captured_data[0]['data']['response']['response']['numFound']}
            else:
                print("\n❌ No API data captured during monitoring period")
                return {'status': 'no_data', 'count': 0}
                
    except Exception as e:
        print(f"\n💥 CRITICAL ERROR in capture_bids: {e}")
        import traceback
        traceback.print_exc()
        return {'status': 'error', 'message': str(e)}




            