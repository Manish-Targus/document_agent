
try:
    from qdrant_client.http.exceptions import UnexpectedResponse
    print("Import successful")
except ImportError as e:
    print(f"ImportError: {e}")
except Exception as e:
    print(f"Error: {e}")
