# BID DOCUMENT PART-II FOR

## TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

### NEW DELHI

### JUNE 2025

----

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER DOCUMENT
## PART-II

### SCOPE OF WORK
### AND
### SPECIAL CONDITIONS OF CONTRACT

- The Special Conditions of Contract (SCC) as laid down in this document override the terms laid down in the General Conditions of Contract (Standard Bid Document Part-I or SBD-I (including modifications)).
- These documents are available on the IREPS (Indian Railways E-Procurement System) website and can be downloaded from the site www.ireps.gov.in.
- All terms and conditions not specifically mentioned in the SCC shall be governed as per the terms and conditions of tender and SBD-I (including modifications).

----

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Contents

1. **Project Background**................................................................................................................................. 8
- 1.1. About Indian Railways........................................................................................................... 8
- 1.2. About CRIS ............................................................................................................................ 8
- 1.3. About Next Generation Passenger Reservation System (PRS).................................................. 8
- 1.4. About Passenger Reservation System Data layer (PRS Data layer)........................................... 8
2. **Scope of Work**......................................................................................................................................... 9
3. **Next Generation PRS System Deployment Architecture** ....................................................................... 9
- 3.1 Overall System Deployment Architecture .................................................................................... 9
- 3.2 New PRS System Deployment Architecture for Data Layer ......................................................... 11
- 3.2.1 Transactional Datastore ............................................................................................................... 11
- 3.2.2 RDBMS .......................................................................................................................................... 12
- 3.2.3 In Memory Data Grid (caching) Solution...................................................................................... 12
- 3.2.4 Operating System (To be provided by the Bidder)....................................................................... 13
- 3.2.5 PRS Data layer environment details with enterprise version deployment .................................. 14
- 3.3 Sizing Consideration for the PRS Data layer ............................................................................... 14
- 3.3.1 Transactional Datastore ............................................................................................................... 15
- 3.3.2 RDBMS .......................................................................................................................................... 15
- 3.3.3 In Memory Data Grid (caching) solution ...................................................................................... 16
- 3.3.3.1 Sizing requirement for production environment for In Memory Data Grid.............................. 16
4. **Detailed scope of work** ......................................................................................................................... 17
- 4.1 Deployment Architecture and detailed design...................................................................... 17
- 4.2 Software supply, Installation, Configuration and performance tuning ................................... 19
- 4.3 Migration requirements for Transactional Data Store........................................................... 20
- 4.4 Monitoring Dashboard and Security requirements ............................................................... 21
- 4.5 Security Requirements ........................................................................................................ 21
- 4.6 Integration Support for the products procured through separate sourcing processor or open-source components ........................................................................................................................ 22
- 4.8 Setting and configuring of DR (Disaster Recovery) processes ................................................ 22
- 4.8.1. DR parameters....................................................................................................................... 22
- 4.8.3. Failover and Failback strategy ............................................................................................... 23
- 4.8.4. Switchover strategy ............................................................................................................... 24
- 4.8.5. Switchback strategy............................................................................................................... 24

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 4.8.6. Security strategy
## 4.8.7. Testing strategy
## 4.8.8. Monitoring strategy
## 4.9 Comprehensive Maintenance Support for complete supplied components for a period of 3 years
## 4.9.1. Resident Engineer Deployment
## 4.10 Uptime requirements
## 4.10.1 Service Level Agreement (SLA) for software solutions products
## 4.11 SLA Breach Penalty
## 4.12 Backend Support from OEMs
## 4.12.1 Backend support from OEM for technical support of all supplied Software
## 4.12.2 OEM man-days of all supplied Software
## 4.13 Training
## 5. Qualification (PQ) Criteria for Bidder
## 6. Technical Requirements
## 7. Instructions to Bidders
### 7.1 Availability of Tender
### 7.2 General Conditions
### 7.3 Compliant Offers / Completeness of Response
### 7.4 Submission of Bids
### 7.5 Pre-bid Conference
### 7.6 Site Visit
### 7.7 Evaluation of offers
### 7.8 Delivery schedule
### 7.9 Consignee, Delivery Address and Installation Location
## 8. Performance cum Warranty Guarantee (PBG) Bond
## 9. Project Deliverables and Timelines
## 9.1 Responsibility matrix
## 10. Liquidated damages in Delay in Delivery and Commissioning
## 11. Inspection and Acceptance Test Procedure (ATP)
### 11.1 Preliminary Testing
### 11.2 Final Acceptance Testing
### 11.3 System Commissioning
## 12. Payment Terms
### 12.1 Enhancement and reduction of quantities
## 13. Documentation
## 14. Role of CRIS

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

15. Make in India Compliance
16. Land Border with India Compliance
19. Annexure IB – List of Software and Hardware Components
20. Annexure IC – Details for DR Site Data Replication
21. Annexure ID – Backup Details
22. Annexure IE - Details of components of Overall System Deployment Architecture
22.1. Physical Servers
22.2.1. Management Nodes
22.2.2. Compute Nodes for Application Workload
22.2.2.1. Kubernetes Worker Nodes
22.2.2.2. Transaction Database Nodes
22.2. SAN Storage
22.3. Container Platform
22.4. Service Mesh
22.5. Application Service Gateway
22.5.1. Ingress Controller
22.5.2. API Gateway
22.5.3. Hardware Load Balancer
22.6. Data Layer
22.7.1. In-Memory data grid
22.7.2. Database
22.7. Event Broker Platform
22.9. Logging and Diagnostics
22.10. Identity access management
22.11. Data Backup
23. Annexure – II: Schedule of Requirements
24. Annexure – III: Functional Requirement
24.1. Transactional Datastore Solution Functional Requirements
24.2. RDBMS Solution Functional Requirements
24.3. In Memory Data Grid (caching) Solution Functional Requirements
25. Annexure – IV: Technical Specification
25.1. Transactional Data store
25.2. RDBMS

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 24. In Memory Data Grid (caching)
- Page 93

## 26. Annexure – V: Format for submission of Details of credentials/ documents furnished towards compliance of Qualification Criteria
- Page 101

## 27. Annexure – VI: Checklist for submission of Technical Evaluation
- Page 102

## 28. Annexure – VII: Support Office Details in Delhi/NCR and Secunderabad
- Page 103

## 29. Annexure – VIII: OEM Product Deployment Undertaking
- Page 103

## 30. Annexure – IX: Final Acceptance Testing Procedure
- Page 103
- 30.1. Transactional Datastore
- Page 103
- 30.2. Transactional Datastore DR
- Page 104
- 30.3. RDBMS
- Page 104
- 30.4. RDBMS DR
- Page 105
- 30.5. In Memory Data Grid (caching)
- Page 106

## 31. Annexure – X: Test Certificates
- Page 106
- 31.1. Preliminary Test Certificate
- Page 106
- 31.2. Final Acceptance Testing Certificate
- Page 108
- 31.3. System Commissioning Certificate
- Page 109

## 32. Annexure – XI: Technical Use Cases
- Page 110
- Page 110
- 32.1.1 Technical use case report for YCSB
- Page 110
- 32.1.2 Benchmarking criteria
- Page 110
- 32.2 Technical Use cases for In Memory Data Grid (caching)
- Page 112
- 32.2.1 Technical use case
- Page 112
- 32.2.2 Benchmarking Criteria
- Page 113

## 33. Annexure XII: Certificate from Bidder for Compliance to GoI Order for Countries sharing Land Border with India
- Page 113

## 34. Annexure-XIII: NON-DISCLOSURE AGREEMENT (NDA)
- Page 113

## 35. Annexure-XIV: Data layer Solution (Software component) – Breakup Detail Format
- Page 113

## 36. Annexure-XV: Format for Bidder to submit solution for each technical use case solution
- Page 115

## 37. Annexure-XVI: Format for OEM compliance certificate for technical use case solution
- Page 116

## 38. Annexure-XVII: Declaration of inclusion of OEM Services by the Bidder
- Page 117

- Page 118

- Page 118

## 41. Annexure XXI: OEM's Authorisation to Bidder and Undertaking for Backend Support
- Page 118

## 42. Annexure – XXII: Self Certification by Bidder for Make in India
- Page 120

## 43. Annexure-XXIII: Installation and configuration – Breakup Detail Format
- Page 120

## 44. Annexure XXIV: Past Performance Details of Bidder
- Page 120

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Annexures
- **Annexure XXV:** Declaration of Non-Blacklisting for OEM ............................................................. 122
- **Annexure XXVI:** Declaration of Non-Blacklisting by Bidder .......................................................... 123

----

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
Page 7 of 124
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 1. Project Background

### 1.1. About Indian Railways
- Indian Railways (IR) is amongst the largest Railway systems in the world, addressing a significant part of the country’s transportation needs, both in the passenger and freight segment.
- The annual revenue of Indian Railways is about Rs.2,40,000 Cr.

### 1.2. About CRIS
- Ministry of Railways established Centre for Railway Information Systems (CRIS) in 1986 as the umbrella organization for all ICT activities of Indian Railways (IR).
- CRIS is a project-oriented organization engaged in development of major IT systems of the Railways.

### 1.3. About Next Generation Passenger Reservation System (PRS)
- One of the major applications of Indian Railways is the Passenger Reservation System (PRS).
- The system currently operates from 4 Data centres connected by a core IP network, enabling universal terminals across the country for berth reservations.
- More than 7000 terminals installed at over 2000 points of presence across the country, connected to data centres using a state-of-the-art IP based terminal network.
- The system handles more than 900 booking/cancellation transactions per second and 12,000 enquiry transactions per second.
- The current PRS system, developed in the 90s, will be rebuilt on the latest technologies to keep pace with advancements.
- The transition will be evolutionary to mitigate risks involved in migrating such a large IT system.
- The main objective is to build an open standard-based system for easy integration with other systems/devices.
- Enhancements required include multiple payment modes, smart card integration, and seamless integration with business analytics and decision support systems.
- The new system must adhere to high capacity OLTP system requirements: high scalability, performance, availability, security, ease of operations, and agility.

### 1.4. About Passenger Reservation System Data Layer (PRS Data Layer)
- The PRS Data Layer is crucial for managing data persistence and caching, ensuring availability, scalability, and agility while maintaining business integrity.
- It consists of a Data Persistent Layer and Cache layer for data processing and persistence.
- Updates in data fetched from the Persistent Datastore and Cache will be reflected in both layers.
- The layer will be highly resilient, scalable, and agile, ensuring business integrity with high availability.
- The Cache layer will store data in memory for faster access and processing, specifically for train data used in enquiries.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 1. Introduction
- This RFP is for procuring the Transactional Data store and its underlying Operating System, RDBMS, Cache (IMDG) solution for PRS Data Layer.
- The solution should handle high volumes of data and concurrent requests, ensuring high availability and scalability.

## 2. Scope of Work

- Supply, installation, and integration of:
- Transactional Data Store and its underlying Operating System
- RDBMS
- In Memory Data Grid (caching)
- Setup includes Disaster Recovery replication, Acceptance Testing, Performance Tuning, and Commissioning.
- Locations: Primary data centre at Railway Internet Data Centre (RIDC), CRIS, New Delhi, and DR Data Centre at Secunderabad Railway Station.

### 2.2. Provisioning of OEM Technical Resources
- Required OEM technical resources for:
- Deployment architecture design
- Installation and configuration
- Performance tuning activities
- Data modelling and architecture validation
- An undertaking from OEM is required.
- Knowledge transfer session for CRIS team on the implemented solution.

### 2.3. Technical Support and Integration
- Provide technical support and OEM resources for integration with other infrastructure components of Next Generation PRS.
- Components include Container Orchestration platform, IAM/PIAM, SIEM, NMS, etc.
- Details of hardware and software components specified in Annexure – IB and Annexure XIX.

### 2.4. Maintenance Support
- Maintenance support of supplied software components for a period of 03 years from the date of commissioning at Primary DC and DR DC.

## 3. Next Generation PRS System Deployment Architecture

### 3.1 Overall System Deployment Architecture
- The deployment of the Next Generation Passenger Reservation System will follow the specified architecture.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## EXTERNAL
- G2G
- B2C
- B2B
- AGEN DISPLAY
- EXTERNAL SYSTEM FOR INTEGRATION
- EXTERNAL GATEWAY
- BANKS
- API GATEWAY
- UIDAI
- OTHERS

## POLICY MANAGEMENT
- FIREWALL
- INTERNAL SYSTEMS
- COUNTER
- NGET
- CONSUMER IDENTITY PROVIDER
- CRIS RIDC DMZ
- ADC
- OTHERS
- FIREWALL

## Militarized Zone
- SERVER LOAD BALANCER
- Production
- Observability

- PRS
- Microservices
- Application

- RDBMS
- In-Memory Data Grid (IMDG)
- Messaging / Event Broker Platform
- Zookeeper
- Transactional Data Store

- Kubernetes Cluster
- Virtual Instances
- Container Platform
- Bare Metal Host
- Virtualisation Layer
- Bare Metal Servers
- Management Nodes
- Storage
- Compute

**Note:** This RFP is for the procurement of RDBMS, IMDG, and Transactional Data Store Solution and its underlying Operating System.

For details of deployment architecture, refer to Annexure I-E.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 3.2 New PRS System Deployment Architecture for Data Layer

- The deployment of data layer consists of:
- Transactional datastore
- RDBMS
- In Memory Data Grid (caching) solutions

### 3.2.1 Transactional Datastore

- The transactional datastore solution will consist of a minimum of two clusters:
- One located in the Primary Data Centre (DC)
- The other in the Disaster Recovery (DR) DC

#### Primary DC

```
Transactional                                                  RDBMS
Data-Store

Node-1
Synch.
Replication

Node-N    Node-2
Primary DB  Standby DB

Nede-4    Node
```

#### DR DC

```
Transactional                RDBMS
Data-Store

Node-1
Synch.
Replication

Node-N    Node-2
Primary DB  Standby DB

Nede-4    Node
```

- The transactional datastore solution will be deployed in production over the Bare metal servers at both the Primary DC and DR DC clusters independently.
- Both the clusters present at primary and DR DC will be up at all the time with asynchronous replication configured between Primary DC and DR DC.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Transactional Datastore Solution
- Available at both data centres simultaneously with read and write capability.
- Prioritizes data integrity to eliminate data loss within the cluster.
- Enforces strong data consistency for all write operations.
- Configured replication factor/number of copies in accordance with OEM best practices for high availability.
- Engineered to handle high-volume workloads with uniform performance.
- Capable of deployment over Kubernetes cluster, VM instances, and bare metal servers.
- Offers a dashboard for comprehensive monitoring of all clusters, including:
- Storage - Total, Usage, Free
- Memory - Total, Usage, Free
- Replication factor of different namespaces/databases
- IOPS (Input/Output Operations Per Second)
- TPS (Transactions Per Second)
- Throughput
- User administration
- User role-based access control
- RTO (Recovery Time Objective)
- RPO (Recovery Point Objective)

## RDBMS
- Configured in cluster with High Availability (HA) to eliminate single points of failure.
- Standby database within a data centre should serve read requests.
- Deployed in an active-active configuration between primary DC and DR DC with asynchronous replication.
- RDBMS clusters deployed on RedHat OpenShift container platform in both primary and DR DC.
- Offers real-time monitoring of RDBMS in primary and DR DC with dashboard for:
- Database instances
- CPUs
- Disk storages
- Memory
- Statements in application including dynamic SQL
- Tables
- Locks
- Connection
- Deadlock
- Transactions

## In Memory Data Grid (Caching) Solution
- Deployed over RedHat OpenShift Container Platform (Version 4.14 or above) in both primary DC and DR Data centre.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- Secunderabad Railway Station premises, Secunderabad independently.
- Both the clusters present at primary and DR DC will be up at all the time with asynchronous replication configured between Primary DC and DR DC for data set as per the application requirements.
- All the services of In Memory Data Grid (caching) solution will be available at both the data centres simultaneously with the required capability of read and write.
- The solution should provide the dashboards and monitoring tools to provide insights into the performance, health, and usage of the data grid.

## Monitoring Metrics
- **Node Overview**: Health, status, and resource utilization of each node.
- **Memory Usage**: Real-time memory usage metrics, including heap and off-heap memory.
- **Cache Efficiency**: Hit/miss ratios, eviction rates, and data distribution.
- **Network Performance**: Latency and data transfer metrics.
- **Transaction Metrics**: Operation throughput and latency.

```
Primary DC    DR DC

IMDG          IMDG

Node-1    Node-1

Node-N    Node-2  DR with Async    Node-N    Node-2
Replication

Nede-4    Node    Nede-4    Node
```

## Operating System (To be provided by the Bidder)
- The underlying operating system for the setup will be Red Hat Enterprise Linux.
- Based on the requirement of the proposed transaction data store solution, i.e., deployed directly over the Bare metal servers or deployed over the Virtual machine instances, the subscription of the RHEL with smart management, premium support for 03 years need to be provisioned by the bidder.

### Servers for Deployment
- Following are the number of servers that will be provided by CRIS for deployment of transaction Datastore for which operating system has to be provided by the bidder:

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Data Centre Environment Type
- Physical Server provided by CRIS (Server Details – Annexure I-A)

### Primary Site
- Production: 5
- Staging: 1

### DR Site
- Production: 5

**Note:** The MAF of OEM of Red Hat Operating System is required in the format mentioned in clause (Sno 4- OEM Undertaking).

## PRS Data Layer Environment Details with Enterprise Version Deployment
PRS Data layer components will install with enterprise grade on all the environment as per below given table:

### PRS Data Layer - Environment wise Enterprise Version Deployment Details
| Environment Type | Physical Server provided by CRIS | Transactional Datastore with supporting management components | In Memory Data Grid (Caching) | RDBMS |
|------------------|-----------------------------------|--------------------------------------------------------------|-------------------------------|-------|
| Production       | 5                                 | Bare Metal                                                  | Container *                   | Container * |
| Primary Site     | Staging                           | 1                                                          | VM                            | Container * (Open-Source version) * |
| Production       | 5                                 | Bare Metal                                                  | Container *                   | Container * |
| DR Site          | Staging                           | 0*                                                         | Container *                   | (Open-Source version) * |

* The deployment will be done within the container orchestration platform provided by CRIS.

**Note:** The proposed Transactional Data Store solution for the production environment shall be deployed across all five servers, as specified in Annexure IA, provided by CRIS. The Bidder must supply the necessary licenses for all these servers, as detailed in the table above.

For Transaction data Store, if the YCSB benchmark (Section 32.1) is conducted using more physical servers or equivalent virtual instances than those specified in the table above for production environment of primary DC, the Bidder shall be responsible for providing the required additional licenses along with the corresponding servers, ensuring compliance with the specifications outlined in Annexure IA.

## Sizing Consideration for the PRS Data Layer
The sizing requirements for three components i.e., Transactional datastore, RDBMS, and In Memory Data Grid (caching) solution are given below.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 3.3.1 Transactional Datastore
The solution for transactional Data Store for Primary Data centre (DC) and Disaster Recovery (DC) will be sized based on the following sizing requirement:

### Sizing requirement for production environment for Transactional Datastore
Solution will be designed based on the following day one requirements:

- a) The solution should cater 1,50,000 Reads per second.
- b) The solution should cater 25,000 Writes per second.
- c) The Solution should deliver low-latency performance, with a P99 latency of 2 milliseconds or less for reads and 3 milliseconds or less for writes operations for 6 TB of unique data in a DC, maintaining a Read/Write ratio of 80% reads to 20% writes.
- d) The DR DC setup should be identical as Primary DC w.r.t. sizing parameters and should be capable to handle 100% of Primary DC load with same level of performance.
- e) The subscription for the supplied solution should be as per the Day one performance requirement.

The solution should be capable to deploy over Kubernetes cluster, VM instances and Bare metal servers.

| Environment | Minimum Nodes | Physical Core per Node | RAM (GB) per Node | Storage (GB) per Node | Total RAM (GB) | Total Storage (GB) | |
|-------------|---------------|------------------------|--------------------|-----------------------|-----------------|--------------------|---|
| Staging     | 3             | 4                      | 32                 | 200                   | 12              | 96                 | 600                |

*Note: The sizing parameter of staging environment in DR -DC is same as above.*

## 3.3.2 RDBMS

### Sizing requirement for production environment for RDBMS
The solution for RDBMS for Primary Data centre (DC) and Disaster Recovery (DC) will be in High availability within the data centre. The solution should be capable to be deployed over Kubernetes cluster, VM instances and Bare metal servers. The DC and the DR cluster should be in Active-Active mode. The RDBMS with 12 number of cores will be deployed in each of the primary DC and DR DC over the Kubernetes setup, i.e., the DR DC setup should be identical as Primary DC w.r.t. sizing parameters and should be capable to handle 100% of Primary DC load with same level of performance.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Total number of Subscription UOM Environments required for Primary and DR DC
- **Primary DC**: Number of Cores/Nodes 12/3 nodes of min. 4 cores each
- **DR DC**: Number of Cores/Nodes 12/3 nodes of min. 4 cores each

- **RDBMS (Open-Source version)**

| Environment | Minimum Nodes | Core per Node | Physical RAM (GB) | Storage (GB) | Deployment | Total Core | Total RAM (GB) | Total Storage (GB) |
|-------------|---------------|----------------|--------------------|---------------|------------|------------|-----------------|---------------------|
| Staging     | 2             | 4              | 16                 | 250           | Container   | 8          | 32              | 500                 |

**Note:**
- The sizing parameter of staging environment in DR-DC is same as above.

## In Memory Data Grid (caching) solution
- The solution for In Memory Data Grid (caching) solution for Primary Data centre (DC) and Disaster Recovery (DC) will be sized based on the following sizing requirement:

### Sizing requirement for production environment for In Memory Data Grid
- a) The solution should cater 1.5 million operations per second.
- b) The solution should provide response time of sub-milli second for read and write operations for 1 TB of data, maintaining a Read/Write ratio of 70% reads to 30% writes.
- c) The solution at DR DC should be capable to handle 100% of Primary DC load and response time.
- d) The Subscription for the supplied software should be as per the Day one performance requirement.

- The solution should be capable to deploy over Kubernetes cluster, VM instances and Bare metal servers.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

### IMDG (Cache)

| Environment | Nodes | Minimum RAM (GB) | Storage (GB) per Node | Total Deployment Core | Total RAM (GB) | Total Storage (GB) | |
|-------------|-------|------------------|-----------------------|-----------------------|----------------|---------------------|---|
| Staging     | 3     | 32               | 100                   | Container             | 7              | 96                  | 300                 |

**Note:**
- OEM need to certify the various components sizing to achieve optimum performance as per details given within this section (i.e., section 3).
- The sizing parameter of staging environment in DR -DC is same as above.

## 4. Detailed scope of work

- The bidder shall be responsible for providing all software components, operating system and services, specified or otherwise, which are required to fulfil the intent of ensuring operability, maintainability and reliability of the proposed solution covered under the deployment Architecture (Section 3 and related sections), functional requirements (Annexure -III) and technical specifications (Annexure IV) within the quoted/contract price.

- To carry out the scope of work, the Bidder must nominate a Project manager (PMP certified professional) and technical team which should have expertise on all the supplied Data layer Software components i.e., Transactional Data store, RDBMS, In Memory Data Grid (caching). The OEM of each supplied Data layer Software components are also required to nominate a manager and technical team who will carry out the scope of work defined for the OEM.

- Bidder shall sign Info-Sec NDA /Confidentiality Agreement as part of the larger Services Level Agreements (SLA) as per the format given in Annexure 14 of Standard Bid Document Part-I.

## 4.1 Deployment Architecture and detailed design

a. The PRS Data layer software shall be deployed in Primary data centre (DC) at CRIS, Chanakyapuri, New Delhi and the remote Disaster Recovery Data Centre at Secunderabad Railway Station premises, Secunderabad, as per the system deployment architecture given under section 3 above. However, this can be modified as per the finalized deployment architecture approved by CRIS.

b. The bidder along with OEM should design and architect the solution as per CRIS requirements and the requirements/dependencies of the OEMs of all the supplied software. The design should ensure the operability, maintainability, and reliability of the system.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- Performance requirements along with no single point of failure.
- High level of stability and robustness for the solution.
- Industry standard best practices policies should be applied.
- Design should be vetted by the OEMs involved.

## Design Workshops
- Organized by the Bidder at CRIS Chanakyapuri with the CRIS team.
- Understanding of technical and functional requirements, security features required, etc.
- Conducted by the OEMs expert resources of all supplied software components.
- OEMs of each supplied component shall provide high-level design and architecture document to CRIS and bidder.

## High-Level Design Document
- Bidder shall prepare the High-Level Design document and deployment architecture for supplied components (Transactional Data store, RDBMS, In Memory Data Grid).
- Requirements/dependencies on other components reviewed and approved by OEMs and submitted to CRIS for approval.

## Implementation Plan
- Bidder shall submit implementation Plan and Project Plan detailing each task with target date and assigned resource persons (OEM/Bidder).
- Plan for installation of all supplied items included.

## Low-Level Design Document (LLD)
- Bidder will submit the LLD of each supplied software component, prepared and vetted by the OEM of respective component.
- LLD to be submitted before the start of installation of the component and revised after deployment.

## Test Plans
- Once the LLD is approved and deployment is started, bidder shall prepare all necessary Test Plans (including test cases).
- Approved by respective OEMs for Acceptance Testing in consultation with the CRIS team.

## Traceability Matrix
- Solution Provider will prepare a Traceability matrix for verification based on requirements in the Design Workshop, Scope of Work, and Deliverables.
- Verified by CRIS after completion of work at each stage and signed off by CRIS team.

## Server Provisioning
- CRIS will provide five bare-metal servers for production Transactional Datastore solution.
- Detailed server specifications mentioned in Annexure IA for production environment at primary and DR DC.
- One server for staging environment at primary DC.
- Transactional Datastore solution along with the supplied operating system will be deployed on the CRIS provided servers.

## Additional Components
- Any additional component (hardware, software, or networking) required for deployment should be supplied by the bidder at no additional cost.
- Additional components should be included in the appropriate line item.
- Maximum of 4U size for additional physical components.
- Should be supplied without any financial implications if discovered later during implementation/testing.
- Additional components must meet support/uptime, Backend support from OEMs, SLA, and penalty clauses in the Tender part-II section 4.9, 4.10, 4.11, and 4.12.

## Note
- OEMs should ensure successful implementation and system operations.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 4.2 Software supply, Installation, Configuration and performance tuning

- **a.** The bidder shall supply all the software components with 3-year subscription. The software supplied should have enterprise level support as per backend support clause defined in Section 4.12. The subscription has to be valid for a period of 3 years from date of commissioning.

- **b.** All the supplied Subscription certificates should be in the name of the Centre for Railway Information Systems (CRIS). All the software subscriptions supplied by the bidder should be commercially supported enterprise version.

- **c.** Any Agreements / EULAs to be signed between the customer / end user, OEM, and / or service provider should be enclosed along with the offer. These may need to be reworded to be mutually acceptable. Any such agreement produced after placement of order will not be considered.

- **d.** The bidder should provide the solution with details of software components required for achieving the sizing mentioned in section 3.3, taking into consideration the hardware provided by CRIS as mentioned in Annexure-IA, for the primary data centre (DC) located at CRIS, Chanakyapuri, New Delhi, as well as the Remote Disaster Recovery Data Centre (DR) at Secunderabad Railway Station premises, Secunderabad.

- **e.** Bidder need to provision the required OEM technical resources (Professional services) for deployment architecture, design, Installation, configuration (including Disaster Recovery replication setup and processes), performance tuning and commissioning of all the supplied software component for primary and DR data centres.

- **f.** The bidder along with the OEMs will be responsible for carrying out all tasks related to software installation, configuration, customization and integration as per items mentioned in Schedule of Requirement (Annexure-II).

- **g.** The bidder along with the OEMs will be responsible for carrying out all tasks related to setting up the high availability, data replication, backup etc.

- **j.** The installation and configuration must be performed and certified by the respective OEM and bidder has to submit the OEM certification for the same. OEMs shall be responsible for successful installation and configuration.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- Implementation and system operations. Bidder shall provide an undertaking from the respective OEMs for the necessary tie-up in this regard.

- Submission of a detailed Installation report/guide and configuration guide for the installed S/W.

- The OEMs of respective product also must conduct knowledge transfer session along with product training for CRIS team on the solution implemented.

- Bidder shall define DBA processes and practices (Checklist) in line with the OEM recommendations for all components supplied by the bidder.

- Bidder shall ensure that all BYODs will be kept free of Malware and under V-M-C of CRIS /Rlys.

- Bidder to ensure all the default credentials of software components installed to be changed.

- Bidder shall ensure that all unused ports/services of equipment should be configured in deny mode. Bidder shall ensure that all default users of equipment should be in closed/disabled mode after installation of equipment.

- Bidder shall ensure that all applications which are not required must be uninstalled or disabled during installation.

## Migration requirements for Transactional Data Store

- The bidder should provide consulting man-days in addition to the requirement mentioned in section 4.2 of the provided Transactional data store solution for schema design and code migration consultation.

- The OEM of the Transactional data store solution needs to follow its best practices in the schema design and the code provided as mentioned in clause (f) below.

- The offered Transactional data store solution should provide OEM supported Spring Data library integration with Spring Boot based applications.

- Modules have been developed using open-source and community edition technologies of NoSQL. The Data access layer is written in Java using Spring Boot and Spring Data.

- The existing schema design should be reviewed by the OEM for leveraging the capabilities of the offered Transactional data store to meet the performance parameter as defined in section 3.3 and suggest the new design which shall be finalized in coordination with CRIS.

- The OEM needs to provide updated spring data code for access mechanism to perform CURD operations. In addition, the OEM also needs to provide the code for complex queries involving Scan.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 4.4 Monitoring Dashboard and Security Requirements

- Bidder shall provide a unified dashboard for monitoring system health and various metrics for both primary and DR site.
- Monitoring should adhere to global ITAM-ITSM standards and CMDB best practices.
- Bidder shall define and implement processes for management and monitoring of the Transactional Datastore, RDBMS, and In Memory Data Grid (caching) solution.
- Monitoring of key indicators like memory, storage, errors, latency parameters, datastore, and cluster level statistics.
- Regular monitoring log files on key indicators.
- User and security management to provide role-based access and authorization.

## 4.5 Security Requirements

- Implementation of security policies on the supplied Software components as per CRIS guidelines.
- Define Security Architecture (SA) and submission of the compliance report.
- Internal/external auditing of the setup by CRIS Internal Security team.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Integration Support for the products procured through separate sourcing processor or open-source components

- Bidder along with the OEM/s shall work out for integration of existing components/tools with the new supplied components.
- These tools/components include:
- IAM/PAMs
- ITSM tool
- SIEM (Security Information and Event Management)
- VA (Vulnerability Assessment)
- NTP source
- OpenShift
- Event streaming tools
- Details of existing components deployed in CRIS RIDC Chanakyapuri New Delhi are given in Annexure 1-B and Annexure-XIX.

- The bidder shall make available OEM resource of the products supplied by the bidder during finalization of deployment Architecture of other Software components mentioned in Annexure-1B (community or sourced through separate procurement process).

- The bidder along with respective OEMs shall provide full support during the deployment of Next Generation PRS application on the integrated platform.

- The bidder along with respective OEMs shall provide full support during performance tuning and Load testing services of the Next Generation PRS system.

- Bidder needs to configure automated backup and restoration process for all components as per the details provided in Annexure ID and provide the detail documentation/SOP.
- These automated backup processes can be configured using either the capability of supplied product or by writing the ansible scripts or by using the combination of both.
- The frequency and the target backup will be decided during the LLD phase as per the proposed solution.

- Mechanism to check the backup (and restoration of backup) regularly, also need to be implemented.

## Setting and configuring of DR (Disaster Recovery) processes

- DR plans and processes (including detailed run-sheets) are to be developed by the bidder on basis of inputs provided by CRIS.
- The processes will be clearly documented and shall include a clear division of responsibility for each activity.
- The replication of required data will be configured in Next Generation PRS using the capability of the data layer product deployed in the setup. Refer section 3.2 for more details.

### DR parameters

- Following are the parameters that need to be configured for setting up the DR for supplied PRS data layer components:

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- Recovery Time Objective (RTO): 5 minutes
- Recovery Point Objective (RPO): 1 minute

a) Proposed solution for Transaction data store should be available on primary data centre and DR data centre simultaneously (i.e., services shall be up at all the time at both sites with asynchronous replication configured across sites) with the required capability of read and write.

b) Proposed solution for In Memory Data Grid (caching) should be available on primary data centre and DR data centre simultaneously (i.e., services shall be up at all the time at both sites with asynchronous replication configured across sites) with the required capability of read and write.

c) Proposed solution for Relational Database Management Systems (RDBMS) should be available on primary data centre and DR data centre in an active-active configuration with asynchronous replication across sites.

d) The Proposed solution should be configured to provide controlled automated failover from primary to DR site and vice-versa.

e) The replication should not obstruct the performance of the system at primary DC and both the primary and DR DC must be available during the replication as well.

f) For data replication across site, only single copy of data is transmitted across the sites, instead of transmitting multiple copies based on the configured replication factor.

g) DR plans and processes (including detailed run-sheets) are to be developed by the bidder on basis of inputs provided by CRIS. The processes will be clearly documented and shall include a clear division of responsibility for each activity.

h) Solution should be able to read/write data from both the data centre simultaneously with both-way replication latency in real time (in milliseconds).

i) Replication of data must be flexible and tuneable based on various business requirements.

## 4.8.3. Failover and Failback strategy

a) This strategy should include the components of the system that will come into play in case of a disaster/incident at the primary sites, to ensure that the required service levels continue to be provided to CRIS and its customers from facilities located at the DR site.

b) In the event of a disaster/incident (that is, an incident that disables the primary site in a manner that requires the DR site to be made operational), the system should failover to the DR site.

c) The DR site should continue to provide services for the failed primary sites, with minimum service interruption and data loss (as per parameters specified in section 4.8.1).

d) In case of the Disaster at primary DC, all the servers and communication equipment running in these sites would therefore be out of service, and the DR system would be expected to restart services adhering to the DR parameters for recovery and operation defined in section 4.8.1.

e) In general, the Data Layer will be considered operational from the DR site when the services of all the supplied Data layer components are available.

f) CRIS will take further steps to make the application layer operational after the data layer components and other system software services are made available.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 4.8.4. Switchover strategy
- This strategy should include the components of the Data Layer that come into play when a planned switchover is made to the DR site for drill or planned maintenance purposes.
- During DR system testing / drills, DR / BC auditing, planned maintenance of the equipment at the primary site, and other similar conditions, a planned switchover might need to be made to the DR site.
- Switchover will be a planned activity. It might need to be executed at short notice in the case of emergent maintenance needs.
- There should be no data loss in case of a planned switchover. Switchover should be possible for any one node/cluster or for all nodes/clusters simultaneously.

## 4.8.5. Switchback strategy
- This strategy should include the components of the system that come into play when system operation switches back to the primary site after being operated for a time from the DR site. The following three cases should be covered:
- Complete Disaster (destruction of equipment / data at Primary site or interruption in service lasting over 30 days): In this case, the primary site has to be set up afresh.
- Partial Disaster (interruption of service from primary for less than 30 days without destruction of equipment / data at primary site): In this case, the primary site must be started up from the state that existed at the time of disaster.
- Switchback from planned switchover: In this case, the primary site must be started up from the state that existed at the time of switchover, but the overall process is much more controlled.
- As soon as the facilities at the primary sites have been restored, the applications need to be switched back to the primary sites from the DR site.
- Switchback should be a planned activity. There should be no data loss in the event of a switchback. The mechanism should be in place for new delta changes back to primary from DR site before switching back to Primary DC.
- In case of Partial Disaster as described in para above, “primary – primary conflict” between the DR and primary site at the time of primary system restart should also be resolved automatically.

## 4.8.6. Security strategy
- This strategy should clearly lay down the security measures that will be taken by the bidder to ensure that the Data Layer components and data are accorded the appropriate level of confidentiality, integrity, and availability.
- It should also include all aspects of network security. This shall be in-line with the CRIS security policy and jointly defined with CRIS team.
- Bidder need to ensure compliance to this strategy/policy.

## 4.8.7. Testing strategy
- The testing strategy should ensure that recovery and switchback strategies are regularly tested.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 2. Disaster Recovery (DR) Drills
- At least two DR drills in a year (once every six months) and appropriate corrective and preventive measures are adopted.

## 3. Duration of DR
- The duration of DR will be determined based on the requirements specified by CRIS, which may vary from few hours to 3 days or according to the specific needs.
- The bidder is required to support the system throughout this specified period, ensuring that DR capabilities are effectively managed and aligned with CRIS's requirements.

## 4.8.8. Monitoring Strategy
1. The monitoring strategy should lay down how the PRS Data layer software components shall be effectively monitored throughout the contract period by the bidder.
2. Bidder will provide a single view of the PRS Data layer software components from a central web-based dashboard which should also integrate it with monitoring dashboard of primary Site for unified view.
3. All parameters such as RTO / RPO, replication status, DR status, Data lag status etc. should be monitored through this system.
4. Bidder should configure and carry out local as well as remote monitoring of the PRS Data layer software components from CRIS Chanakyapuri, New Delhi premises. The primary responsibility for the management and monitoring of the PRS Data layer software components and adherence to prescribed service levels shall remain that of the bidder.
5. The activities performed by the bidder should be logged. This log should be monitorable by CRIS staff on quarterly basis or as and when the need arises.
6. The monitoring metrics and data has to be retained as per the CRIS policy.

## 4.9 Comprehensive Maintenance Support for Complete Supplied Components for a Period of 3 Years
- a) Maintenance coverage will be on 24 x 7 basis as per uptime requirements defined in section 4.10.
- b) Bidder shall nominate an Account Manager/Senior functionary as single point of contact for day-to-day coordination with CRIS throughout the maintenance period. The bidder also has to allocate technical team having expertise in all supplied Software components.
- c) The bidder will provide escalation mechanism with complete details including address, phone number (office as well as residential), mobile number etc. of the allocated resources.
- d) Bidder shall deploy one resource on 365 days basis as detailed out in section 4.9.1.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

e) The bidder shall provide and install updates and upgrades for the entire set of software components as and when released by the OEM (latest patches). Software updates/upgrades shall also be done keeping in view advancement in technology, shortcomings of the system, security vulnerabilities, or changes required for improving functional efficiency and security level of the system. The bidder should ensure that the security patches are applied after every re-installation/maintenance activity. The SLA defined in section 4.10.1 shall be applicable for security patches implementation. In case of breach, penalties applicable have been defined in same section. The plan for any upgrade duly approved by OEM(s), should be submitted to CRIS in advance along with rollback plan for approval. The activity should be planned in coordination and approval of CRIS. Depending on criticality of activity, on instructions from CRIS, the bidder shall arrange the OEM resource at the site. The bidder shall ensure complete rollback to original status in case of problem and shall take necessary system backups before any activity of SW upgrade/Changes in configuration etc.

f) Upgrade should be provided based on rolling upgrade to maintain the availability of the system during the upgrade process without shutting down the entire cluster but only a single node in which upgrade will be performed.

g) The bidder shall carry out the configuration changes for the complete software components as per requirement given by CRIS and shall follow Change Control Process which shall be jointly defined with CRIS.

h) The bidder shall maintain Site Management Guide for provisioned software configuration under maintenance and keep it in electronic as well as hard copy form in CRIS premises. Bidder shall be responsible to update the Site Management Guide on regular basis and reflect the latest configuration and shall also maintain the Change documents.

i) In case of a failure or degraded performance, a detailed incident report including analysis should be prepared in consultation with the OEM of the respective product(s) with an objective to avoid similar failures in future. Preliminary report should be submitted within 24 hours. A detailed technical report along with RCA will have to be submitted to CRIS within one week.

j) Bidder shall provide the required support and coordinate with the supplying agencies of existing hardware, software, network for integration between these systems/tools and the software components supplied/maintained by the bidder. The bidder shall also coordinate with the agencies responsible for maintenance of these systems for resolution of issues.

k) Bidder shall depute OEM resources, if required, for any activity planned in the Data centre affecting the working of Next Generation PRS application.

l) Bidder shall carry out a comprehensive performance analysis of all supplied softwares on a monthly basis and shall submit a report. The report should include performance analysis for all components and the recommendations for change of parameters / configuration / Resource requirement etc. if any. The parameters to be monitored and the report format shall be jointly decided along with CRIS and the OEMs resource.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- Documentation/SOP. The Backup mechanism should be vetted by OEMs. Mechanism to check the backup regularly also need to be implemented.

- Bidder shall perform periodic activity for restoration of backup of Transactional Data store, RDBMS and In Memory Data Grid (caching) on a new instance/VM provided by CRIS.

- Bidder will also be responsible for restoration of the Transactional Datastore from backup in case of failure, setting up of new instance to same or new environment.

- Bidder shall define and implement the purging on basis of inputs provided by CRIS team and automated purging mechanism to be developed so that data can be purged after a specified period. The purging mechanism should be duly vetted by OEMs and should not degrade the performance.

- Irrespective of any other limitations, the Bidder/ OEM have to ensure availability of the Security patches for software supplied in CRIS for a minimum period of Five years, from the date of Installation Acceptance. To ensure this, the Bidder/ OEM are advised to supply the latest Firmware and System SW versions, irrespective of their old offers.

## 4.9.1. Resident Engineer Deployment

- The bidder shall deploy Resident Engineers (REs) at primary Site for carrying out day to day system maintenance and monitoring activities for the supplied components in primary data centre and DR data centre, used for Next generation PRS system. Bidder has to provide RE for a period of 03 year from the Date of go-live (Milestone M3 defined in Section 9). Following shall be the minimum number of personnel present on-site to handle the support:

| Resource Required | Number of Shifts | Personnel in Shifts | Minimum Qualification | Minimum Experience |
|-------------------|------------------|---------------------|-----------------------|--------------------|
| Resident Engineer  | 1 resource every day (365 X 24 X 7) | 3 shifts of 8 hours* | BE/B. Tech. or equivalent | Minimum 2 years of relevant experience in managing Transaction data Store. Certified in Transaction data Store offered in bid. |

- Minimum 5 resources required.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- Shift timing and days of week can be changed by CRIS as per requirement/activities planned.

- “The Contractor should commit to complying with all Labour Laws and indemnify CRIS against any liability on this account. In the event of CRIS being so charged, the Contractor will be liable for fulfilling all costs to CRIS in this respect including all legal charges.”

## 4.10 Uptime requirements

- The bidder shall provide the uptime for the Software and all other supplied components as detailed in section below:
- a) The bidder shall provide an uptime guarantee of 99.9% on monthly basis. The system will be treated down when there is a total failure of Next Generation PRS services or degradation in system performance on account of failure/malfunctioning of software components being maintained by the bidder. In case of failures exceeding the defined uptime for the month, it shall attract penalty as defined in ‘Total Service failure’ item of section 4.11 – titled “SLA Breach Penalty”.

- b) The total service failures should be limited to a maximum number of 02 in a calendar month. No failure shall exceed 0.72 hours (43.2 minutes) excluding application start-up time. If the duration of any failure exceeds 0.72 hours (43.2 minutes) it would attract penalty as defined in ‘Total Service failure Section’ of SLA Breach Penalty (section 4.11).

- c) Irrespective of the duration of failures, if there are more than 02 failures in a month, this too shall be treated as Total Service failure and shall attract damages as defined in ‘Total service failure’ column of Section 4.11.

- d) For any system failure within a month total grace period in terms of downtime calculation will not exceed 0.72 hours (43.2 minutes). If in any circumstances, total downtime exceeds 0.72 hours (43.2 minutes) for first 2 failures within a month, failure duration beyond 0.72 hours (43.2 minutes) will be considered for calculating penalty. If total downtime for first two failures is less than 0.72 hours, even then no grace time will be permitted for third and subsequent failure within that calendar month.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

### Penalty Conditions
- Failures of any of the supplied components resulting in total service failure of the Next Generation PRS Service(s) will attract penalties as defined in the ‘Total Service failure’ item of section 4.11 titled “SLA Breach Penalty”.

- For calculating Penalty:
- Excess failure time shall be counted.
- If the number of failures exceeds the permissible limit, the complete failure period shall be counted.

- Planned downtime or downtime due to failures of equipment/software not supplied by the bidder or Power/UPS failure will not be considered for uptime calculations.

- Planned downtime exceeding the allotted downtime for activities of supplied components maintained by the bidder resulting in failure will attract penalties as per the “total system failure” item of section 4.11 – titled “SLA Breach Penalty”.

- If a planned activity of components maintained by the bidder results in unplanned downtime, the system shall be treated as down and will attract penalties for total system failure.

### 4.10.1 Service Level Agreement (SLA) for Software Solutions Products
The Service Level Agreement (SLA) for software subscriptions required under software solutions supplied through this tender shall be as follows:

| SLA Requirement       | Severity Level | Production Support (Time from call logging with OEM) |
|----------------------|----------------|-------------------------------------------------------|
| Support Availability  |                | 24 hours x 7 days                                    |
| Initial Response      | Severity-1    | 30 minutes                                           |
| Service Level Objective| Severity-2    | 30 minutes                                           |
|                       | Severity-3    | 4 hours                                             |
|                       | Severity-4    | 1 day                                               |

### Severity Definitions
- **Severity 1 (Urgent)**: A problem that severely impacts the use of the software in a production environment (e.g., loss of production data or non-functioning production systems). This situation halts business operations and no procedural workaround exists.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Severity Levels

- **Severity 2 (High)**:
- A problem where the software is functioning but use in a production environment is severely reduced.
- The situation is causing a high impact to portions of business operations and no procedural workaround exists.

- **Severity 3 (Medium)**:
- A problem that involves partial, non-critical loss of use of the software in a production environment or development environment.
- For production environments, there is a medium-to-low impact on business, but business continues to function, including by using a procedural workaround.
- For development environments, the situation is causing the project to no longer continue or migrate into production.

- **Severity 4 (Low)**:
- A general usage question, reporting of a documentation error, or recommendation for a future product enhancement or modification.
- For production environments, there is low-to-no impact on business or the performance or functionality of the system.
- For development environments, there is a medium-to-low impact on business, but business continues to function, including by using a procedural workaround.

## SLA Breach Penalty

- SLA breach penalty shall be calculated on the basis of Service failure defined in section 4.10 and 4.10.1.
- SLA breach penalty will be in addition to LD for delay in delivery/installation mentioned in section 10.
- The penalty amount will be worked out on a quarterly basis and a demand letter will be sent to the bidder to deposit the same with CRIS within 15 days from the date of issue of the demand letter.
- In case the bidder does not deposit the penalty amount within the stipulated time, CRIS reserves the right to recover the due amount as under:
- a) From any other pending bills of the bidder in CRIS,
- b) From Security deposit/PBG Bond furnished for this contract or any other contract.

## SLA and Penalty for Total Service Failure

- SLA and Penalty shall be applied as per tables given below for the supplied components.

| S No | Type of Failure   | Minimum Uptime Required | Max Permissible Number of Failures per Month | Max Permissible Downtime without Penalty per Month | Penalty Charge |
|------|-------------------|------------------------|-----------------------------------------------|---------------------------------------------------|----------------|
| 1    | Total Service Failure | 99.9%                | 2                                             | Total 0.72 hours (43.2 minutes) together for all components which may disrupt overall services | Rs 5,00,000/- per hour or part thereof of downtime exceeding the defined SLA |

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 4.11.2. SLA Breach Penalty for software solutions products

- Response for service requests has to be provided as per clause 4.10.1, failing which penalty for service failures shall be deducted from the outstanding bills or PBG as under:

### SLA
- **Severity Level**: Production Support (Time from call logging with OEM)

#### Severity-1
- **Initial Response**: 30 minutes
- 1. Rs. 150,000 per hour (or part thereof) after 30 minutes from the time the same is advised to the Contractor by the Helpdesk/CRIS/IR to the designated e-mail advised by the Contractor for the purpose.
- 2. If persistence above exceeds two hours from the time the same is advised to the Contractor by the Helpdesk/CRIS/IR to the designated email advised by the Contractor for the purpose, then penalty beyond the first two hours of failure will be Rs. 2,50,000/- per hour or part thereof.

#### Severity-2
- **Initial Response**: 30 minutes
- 1. Rs. 150,000 per hour (or part thereof) after 30 minutes from the time the same is advised to the Contractor by the Helpdesk/CRIS/IR to the designated e-mail advised by the Contractor for the purpose.
- 2. If persistence above exceeds two hours from the time the same is advised to the Contractor by the Helpdesk/CRIS/IR to the designated email advised by the Contractor for the purpose, then penalty beyond the first two hours of failure will be Rs. 2,50,000/- per hour or part thereof.

#### Severity-3
- **Initial Response**: 4 hours
- 1. Rs. 10,000 per hour (or part thereof) after four hours from the time the same is advised to the Contractor by the Helpdesk/CRIS/IR to the designated e-mail advised by the Contractor for the purpose.
- 2. If persistence above exceeds eight hours from the time the same is advised to the Contractor by the Helpdesk/CRIS/IR to the designated e-mail advised by the Contractor for the purpose, then penalty beyond eight hours of failure will be Rs. 30,000/- per hour or part thereof.

#### Severity-4
- **Initial Response**: 1 day
- Rs. 5,000 per day (or part thereof) after 24 hours from the time the same is advised to the Contractor by the Helpdesk/CRIS/IR to the designated e-mail advised by the Contractor for the purpose.

## Additional Penalties
- Non-provision or non-performance as per SLA in section 4.12.2 of OEM manpower.
- Non-adherence to the RTO/RPO mentioned in section 4.8.1.
- Double the average per day remuneration as quoted by the bidder will be imposed as penalty for non-availability of manpower.
- Rs 2,00,000/- per hour or part thereof of downtime exceeding the defined SLA.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 4.11.3. Resident Engineer SLA and Penalty

- **S.N.**     **Measure**                                   **Measurement**     **Target Interval**                       **Penalty**

1. **Submission of Monthly Reports**
- All Reports for the previous month shall be submitted by the 7th of the next month
- **No Penalty**
- Delay beyond the date of submission:
- Rs.1000 for every day’s delay on an incremental basis.

2. **Manpower Absence of Resource**
- If equivalent skilled resource is deployed, then no penalty will apply.
- Otherwise, it would be treated as absence of resource and penalty will be applicable.
- **Absence Penalty**
- **S.N.**     **(Shifts in month)**     **Penalty Value (in Rs)**
1. For 0-2 Shift          Rs 9,000 per shift
2. For > 2 to 5 Shift    Rs 18,000 per shift
3. For > 5 Shift          Rs 27,000 per shift

- The Bidder must ensure the Man-power continuity. In case a resource leaves before completing six months, Penalty of Rs.10,000/- per such instance will be levied.

## 4.11.4. Security SLA and Penalty

- Security patches must be deployed for all software supplied by the bidder as per the below-mentioned category classification and SLAs from the time of the patches are being released:

|-------------------------|--------------------------|-------------------|------------------------|------------|---------|----------|
| Within 30 Days          | Within 45 Days           | Within 60 Days     | 100 %                  | For Critical severity Systems will be scanned on a weekly basis by the bidder for identifying missing security patches | Rs 3,000/- per missing security patch |  |

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Security Patches
- Security patches for high severity vulnerabilities will incur a penalty of Rs. 1,000/- per missing security patch.
- Penalty will not be charged for delays in approval of patch rollout by CRIS.

## SLA Breach Penalties
- All SLA breach penalties are independent and will be imposed separately.
- Multiple penalties may be imposed for any failure/breach of SLA.
- Cumulative penalty shall not exceed 10% of recurring charges (Subscription cost and 24x7 Support cost) including taxes.
- If total penalty exceeds the maximum limit, CRIS reserves the right to cancel the contract and forfeit the Performance cum Warranty Guarantee (PWG) Bond.

## Backend Support from OEMs
- Bidder must have back-to-back support from OEMs for all components listed in SoR (Annexure-II) for a period of 5 years.
- Documentary proof of backend support must include:
- **Technical Support**:
- 24x7 support via Phone, Email, or Site visit based on problem criticality.
- Provision to log complaints/open support cases directly with OEM for unlimited cases.
- **Upgrades and Updates**:
- Support for carrying out upgrades and updates to the latest versions of supplied software.
- **Performance Tuning**:
- Resolution of performance-related issues and tuning of all supplied system software.
- **Troubleshooting**:
- Assistance in case of critical failures, especially for failures extending beyond permissible downtime.
- **Root Cause Analysis (RCA)**:
- RCA of failures/incidents with an action taken report to prevent recurrence.
- **Project Management**:
- OEM must nominate a project manager and technical resources, and share the escalation matrix.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 4.12.2 OEM man-days of all supplied Software

- **a)** The Bidder should have minimum tie-up of:
- 35 man-days with OEM of Transactional Data store with supporting components
- 5 man-days with OEM of RDBMS
- 15 man-days with OEM of In Memory Data Grid (caching) for the first year for performance tuning and updates and upgrades of respective system software for Primary DC and DR DC.

- **b)** The Bidder should have minimum tie-up of:
- 20 man-days with OEM of Transactional Data store with supporting components
- 5 man-days with OEM of RDBMS
- 10 man-days with OEM of In Memory Data Grid (caching) for each second and third year for performance tuning and updates and upgrades of respective system software for Primary DC and DR DC.

- **c)** The commencement of OEM man-day support validity shall start from the successful commissioning of the entire solution, and second year validity will start after the end of the first year validity and so on.

- **d)** The OEM man-days services should be provided for a minimum of 1 man day (i.e., 8 hrs.).

- **e)** The man-days services should be provided by OEM professionals only.

- **f)** CRIS shall directly invoke services from the OEM as per the requirement, and these services could be invoked any time, i.e., beyond office hours, on weekends, or holidays depending on the criticality.

- **h)** The resource made available should have the following qualification criteria:
- i. 5+ years of experience on respective software solution platform.
- ii. Certified professionals on supplied software solutions.
- iii. Should have hands-on experience on supplied software solutions.
- iv. Understanding of performance tuning and knowledge of its relevant tools.
- v. Experience on software hardening.

- **i)** CRIS can utilize the man-days for the following technical work:
- i. Architect solution.
- iii. Root cause analysis of problem/failure and their resolution, health checkup, and onsite support.
- iv. Define and implement best practices in system administration for smooth running of the product.
- v. Implementation of patch updates, security, and new releases.

- **j)** For utilization of man-days, the scope of planned activity will be shared by the CRIS with the OEM, and the corresponding activity action plan with timeline will be shared by the OEM. On successful completion of the planned activity, a work completion report will be submitted by the OEM at the end of the activity.

Bidder should provide an undertaking from OEMs in this regard as per Annexure 8 of SBD1.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 4.13 Training

- a) Bidder shall arrange for OEM training for two batches of 12 engineers each for Transactional Data store and supporting components, one batch of 12 engineers for In-Memory data grid (Caching) Solution and one batch of 12 engineers for RDBMS (Administration) Software products.

- c) Training shall be provided by the OEM certified Trainers only. The resume of trainers proposed by the OEMs shall be provided to CRIS. Only the trainers selected and approved by CRIS shall be deputed as trainers for these training programs.

- d) Training should also cover hands on sessions along with Security hardening, monitoring for any Security Issues etc.

- e) Training material should be provided to all participants in form of electronic media/ paper documents.

## 5. Qualification (PQ) Criteria for Bidder

- 5.1. All the criteria given in table below are mandatory for qualification. Bids not meeting these parameters of the Qualification Criteria shall be summarily rejected.

- 5.2. The criteria must be met by the entity bidding for the project itself and that of the sister/associate companies shall not be considered.

- 5.3. Consortium/JV bidding is not allowed.

- 5.4. The bidder has to ensure that the requisite documents/details towards Qualification Criteria are submitted along with bid. Compliance of Qualification Criteria parameters and details of associated documents should be filled in the format as per Annexure-V. Bids not accompanied by all the required documents mentioned are liable to be considered only on the basis of the documents/details furnished with the bid. However, CRIS reserves the right to seek clarifications from the bidders wherever considered necessary.

- 5.5. Qualification Criteria Parameters

| S No. | Parameter                                   | Qualification Criteria                                                                 | Credentials to be provided |
|-------|---------------------------------------------|----------------------------------------------------------------------------------------|-----------------------------|
| 1     | Qualification Criteria: Existence of Bidding Entity: Registration Certificate | The Bidder must be a Private or Public Company or a Proprietorship, Partnership firm, LLP, or Society/ Trust. Based on the nature of entity | For Companies: Certificate of Incorporation under the Companies Act For Partnership Firms / Limited Liability Partnership (LLP): |

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Parameter Qualification Criteria Credentials to be provided

1. **Existence of Bidding Entity: Partnership Deed or Certificate of registration under the Indian Partnership Act / LLP Act**
- For Societies / Trust: Certificate of Registration with Registrar of Societies
- For Proprietorship Firms: Attested certificate from Bank(s) clearly indicating the date on which the Bank account was opened in the name of the Proprietorship firm which establishes the existence of the firm for the required period.
- (Mandatory)

2. **GST Certificate**
- Bidder must have a current / valid GST Certificate.
- (Mandatory)

3. **Financial Turnover**
- The Bidder's average annual turnover over the last three Financial Years preceding the Financial Year in which the tender has been published must be a minimum of Rs. 58 Crores.
- The bidder shall submit Certificate from a Chartered Accountant for Turnover of the Bidder for the stipulated financial years, as per ‘Annexure 2: Financial Turnover of Bidder’ of Standard Bid Document Part-I.
- Note:
- i. If the balance sheet for the immediately preceding financial year has not yet been audited, the same shall be certified by the CA in the above certificate, and in such a case the Financial Turnover for the fourth preceding year shall be mentioned in the CA certificate, and the same shall be considered for the eligibility criteria.
- ii. For the purpose of Annual Turnover, only the revenue from operations shall be considered. Other incomes such as interest, dividend etc. are excluded from the annual turnover.
- iii. Credentials of affiliated companies like Parent / Holding.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Parameter Qualification Criteria Credentials to be provided

- Company, Strategic Business Unit, Group Company, Subsidiary / Associate Company, Sister Company etc. will not be taken into consideration. (Mandatory)

### 4 OEM Undertaking
- The bidder shall be an original equipment manufacturer (OEM) or an authorized representative of the respective OEMs.
- Whenever an authorized Agent/Representative submits a bid on behalf of the OEM, the same agent/representative shall not submit a bid on behalf of another OEM in the same tender for the same item/product.
- **Credentials Required:**
- Authorization letter from the OEM specific to this tender as per sample Performa given in Annexure-XXI of RFP.
- In case OEM bids directly, self-certification and any other document for being OEM.
- The authorization should include details of Tender No., Name and address of the OEM and the bidder authorized, and details of the products for which the bidder has been authorized. (Mandatory)

### 5 Relevant Project/Work Experience
- The Bidder should have successfully completed / executed Similar Project / Work in India for the last five Financial Years preceding the Financial Year in which the tender has been published, and current financial year (up to and including the date of publishing of this tender).
- **Credentials Required:**
1. The Bidder shall submit CA certificate as per ‘Annexure XXIV’ detailing projects that meet the relevant Project Experience criteria.
2. Only those Contracts / Work Orders / Agreements shall be considered towards Project / Work Experience which have been issued by:
- Any entity (Department / Organization / Autonomous body / PSU/ Local Body/ Authority etc.) wholly or partially owned by State / Central Government.
- **Value Requirement:**
- At least one Purchase order or work order costing not less than Rs. 10 crores.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Qualification Criteria

- **Parameter No.**

- b) At least two Purchase orders or work orders each costing not less than Rs. 6.25 crores
- Or
- c) At least three Purchase orders or work orders each costing not less than Rs. 5 crores

### Similar Work is defined as under:

- Software/Hardware/Network equipment/IT Security equipment/telecom equipment/Services supporting IT equipment/Services for Network equipment/Services for IT security software and hardware/AMC/ATS/IT Helpdesk/IT manpower for support of IT equipment and any other software/IT hardware/IT network related service or equipment like training, installation, commissioning.

### Additional Criteria

1. Only those Contracts / Purchase Orders shall be accepted as Past experience wherein the contracts / purchase orders have been placed on the bidder directly by an entity belonging to one of the above categories.

2. In case the contract / purchase order / work order being presented is a composite contract (i.e. it contains items other than the ones defined in the qualification criteria as similar work), only such line items shall be considered which qualify as per the definition of similar work mentioned in the contract. In such cases, the value of such line items shall be indicated by the bidder as a separate attachment to annexure XXIV. If the value of contract / line items qualifying as per the definition of similar work is not mentioned separately in such composite contracts/ line items, such contracts / line items shall not be considered towards qualification.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Parameter Qualification Criteria Credentials to be provided

- Bidder shall submit the document/certificate issued by consignee/purchaser for the quantities supplied/activities/stages completed up to the end date of specified period.
- Value of successfully executed/commissioned work, up to the end date of specified period under the criteria, shall be considered as per payment terms stipulated in contract/tender for the item falling within the definition of similar work criteria.
- The bidder shall submit a CA Certificate for the detailed calculation of value as claimed by bidder, accordingly.

- If the purchaser seeks any clarification related to relevant project / Work experience certificates submitted by the bidder, the bidder shall not be permitted to submit any new Contract / Purchase order/ Work order, whose details are not already provided in the original bid.
- Any such new Contract / Purchase order/ Work order shall not be considered. (Mandatory)

### 5.1 Relevant Project / Work Experience:
- The Bidder shall submit Copies of Purchase Order(s) / Contract(s) / Work Order(s) (including all associated documents / Annexures) for all the projects/ works mentioned in the CA certificate. (Mandatory)

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Parameter Qualification Criteria Credentials to be provided

### 5.2 Relevant Project / Work Experience:
- The Bidder shall submit copies of Satisfactory Completion Certificate(s)/ Performance Certificate(s) issued by the Purchaser / Consignee for all the projects mentioned in the CA certificate submitted.
- (Mandatory)

### 6 Non-Blacklisting Declaration by Bidder
- The Bidder shall submit a self-declaration of non-blacklisting clause of Standard Bid Document Part-I as per ‘Annexure XXVI: Declaration of Non-Blacklisting by Bidder’.
- Additionally, the SIs/Bidders are required to submit the declaration/undertaking as per the Annexure XXVI on minimum INR. 100 stamp paper and duly notarized.
- (Mandatory)

### 7 Land Border with India Compliance
- The Bidder shall submit a self-declaration of compliance to Land Border clause of Standard Bid Document Part-I as per ‘Annexure 7: Certificate from Bidder for Compliance to GoI Order for Countries sharing Land Border with India’ of Standard Bid Document Part-I.
- (Mandatory)

### 8 Make in India
- The Bidder shall submit a self-certification of compliance to Make in India Policy as per ‘Annexure 6: Self Certification by Bidder for Make in India’ of Standard Bid Document Part-I.
- (Mandatory)

CRIS reserves the right to verify the authenticity of the documents submitted by the bidder.

## 5.6 Guidelines for Start-up Firms
- As per CRIS SBD-I (including modifications)

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 6. Technical Requirements

- All the technical criteria given in the table below are mandatory for qualification.
- Bids not meeting these parameters of the technical requirement shall be summarily rejected.
- The bidder is required to use the formats and guidelines provided in the Annexure VI to provide information on the technical requirement.
- The bidder/OEM must ensure that validity of certificates asked under technical specification of item quoted, if any, shall be valid on the date of closing of tender.
- Bids are liable to be considered only on basis of the documents/details furnished with the bid.
- However, CRIS reserves the right to seek clarifications from the bidders wherever considered necessary.

| S. No. | Parameter                                   | Technical Requirements                                                                 | Documents to be provided                                                                                                                                                                                                 |
|--------|---------------------------------------------|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1      | Solution                                    | Proposed solution along with deployment Architecture in accordance with the minimum requirement specified in deployment architecture defined in section 3 and related Annexures. | Bidders need to submit the solution document along with deployment architecture and also compliance to CRIS proposed architecture and sizing of Data layer (section 3.2) duly vetted by respective OEMs.
**Note:** The solution document should clearly present the deployment architecture, including detailed replication mechanisms, a high availability (HA) strategy to ensure zero data loss, backup strategy, comprehensive dashboard and monitoring capabilities, and any other relevant components necessary to fulfil the specified requirements. |
| 2      | Schedule of Requirements (Non-priced SOR) | Make/Version/Model of the offered products as per format given in Annexure II.       | Bidder need to clearly specify the Make/Model and details as per format given in Annexure II, for each Item in Schedule of Requirements and mention details of additional products offered to meet the requirements in the remark column of <non-priced> Schedule of Requirements provided in technical bid. No price element to be mentioned otherwise the bid will be summarily rejected. |</non-priced>

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 3. Technical Compliance
- Compliance from OEM for detailed technical specifications of all the Products are given in Annexure IV.
- The bidder must submit an item wise compliance for the technical specifications duly vetted by the respective OEMs specific to this tender.
- The Model and Make/Version of the offered products should be clearly specified in this compliance document.

## 4. Bill of Material (BoM)
- Bill of material (BOM) of offered products.
- The bidder must furnish the complete Bill of Material (BoM) of all the products on the letter head of the OEM duly vetted by the respective OEM.

## 5. Technical Use Case report for YCSB for transactional data store
- Proposed Solution should provide YCSB benchmark reports given in Annexure XI along with the product used to implement the solution.
- Bidder to submit documents for YCSB benchmark report for workload types (as per format given in Annexure XV) having the following information:
- Hardware utilization report based on nmon csv format for workload types.
- Product(s) used to implement the workload types for YCSB benchmark report.
- Compliance Certificate from the OEM(s) on their letterhead as per format given in Annexure XVI, whose product is used to implement the solution for the respective workload types.

- Refer Annexure XI for YCSB benchmarking Criteria, Workload types.
- CRIS reserves the right to ask for the demonstration of the YCSB benchmark to implement the workload types given in Annexure XI.

## 6. Product Support life cycle
- The bidder should submit valid letter from all the OEMs.
- Documentary evidence such as from all OEM/Vendors whose products are being quoted by the Bidder need to be submitted as per.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 7. Product Deployment
- Note: In case, the OEM is unable to share the Customer details due to binding of Non-Disclosure Agreement (NDA) signed with the Customer, the OEM needs to mention the same in the above undertaking and provide all other required information.

## 8. Quality Management System
- Bidder should have a valid ISO 9001:2015 Quality Management Certification on the date of closing of the Tender.
- Valid Certificate of each type from the certifying organization.

## 9. Bidder or OEM Support Offices Availability
- Bidder or OEM should have Customer Support offices in the Delhi / NCR region and Secunderabad.
- In case bidder does not have offices in these places, the bidder may give an undertaking to have offices in these places in case the tender is awarded.
- The office should be opened within four weeks from the date of awarding of the Tender.

## 10. Technical Resource Capability
- Bidder to ensure availability of OEM Certified Man-power if the contract is awarded.
- Declaration from bidder or details of certified Engineers along with supporting documents clearly giving the certification details, if engineers are available.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 11. Declaration of Inclusion of OEM Services
- The bidder should submit a letter as per Annexure-XVII specific to this tender.

## 12. Functional Requirement
- Compliance from Bidder for detailed functional requirement of all the Products given in Annexure III.
- The bidder must submit an item-wise compliance for the functional requirement.

## 7. Instructions to Bidders

### 7.1 Availability of Tender
- Bidding process will be on-line through E-Procurement System (www.ireps.gov.in).
- Bidder may please see instruction to Tenderers for E-Tender, CRIS SBD-I (Including modifications) and Tender Document etc. on www.ireps.gov.in before quoting the tender.
- The bidders shall be solely responsible for checking the website of e-procurement i.e., www.ireps.gov.in for any addendum/amendment/corrigendum issued subsequently to the bid document and take into consideration the same while preparing and submitting the bids/offers.

### 7.2 General Conditions
- **7.2.1.** The bidder should be registered with GST department of the Govt. of India. Copy of valid GSTIN number should be enclosed.
- **7.2.2.** The bidder must specify Item-wise Compliance to technical specification duly vetted by the respective OEMs. The Model and Make of the offered product should be clearly specified.
- **7.2.3.** The bidder/OEM must ensure that certificates, including certificates of technical specifications asked, are valid on the date of closing of tender.
- **7.2.5.** No request for change of rates / price shall be entertained after the bidder submits the offer.
- **7.2.6.** The bidder should quote the rates strictly in accordance with the columns /fields provided as per format available on IREPS i.e., www.ireps.gov.in.
- **7.2.8.** Incomplete, vague and conditional bid/offer shall not be accepted on any ground and shall be rejected straightway. If any clarification is required, the same should be obtained before submission of the bids.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 7.3 Compliant Offers / Completeness of Response
- Bidders are advised to study all instructions, forms, terms, requirements, and other information in the Tender documents carefully.
- Submission of the bid shall be deemed to have been done after careful study and examination of the Tender document with full understanding of its implications.
- Failure to comply with the requirements of this paragraph may render the offer noncompliant and the offer may be rejected. Bidder must:
- Comply with all requirements as set out within this RFP.

## 7.4 Submission of Bids
### 7.4.1
- The bids will be submitted electronically in two packets (Techno-Commercial Bid + Financial Bid) system.
- These two packets will be submitted together electronically before the date of tender closing.
- The bidder should follow the instructions to bidder document available on www.ireps.gov.in.

### 7.4.2
- Bid received without EMD will be rejected straightway unless it is established that they are exempted under the law.
- However, it is the responsibility of the bidder to establish through submission of documentary evidence that they are exempted from submission of EMD.

### 7.4.3
- Please note that prices should not be indicated in the Technical Bid but should only be specified in the Financial Bid.

## 7.5 Pre-bid Conference
- The pre-bid conference will not be conducted.

## 7.6 Site Visit
- Bidders may visit the site to obtain additional information before filling the tender at their own cost and responsibility.
- For that purpose, the bidders should intimate CRIS minimum two days in advance in writing.

## 7.7 Evaluation of offers
- This is a two-packet tender with e-RA.
- Bids shall be techno-commercial and financial.
- The bid evaluation process shall be as per Standard Bid Document Part-I.

## 7.8 Delivery schedule
- Delivery shall be made as per quantity mentioned in SoR for the Primary Data Centre and DR Data Centre within 4 weeks from the date of purchase order to consignee at the address given in section 7.9.
- All the supplied equipment and subscription should be in the name of the Centre for Railway Information System (CRIS).

## 7.9 Consignee, Delivery Address and Installation Location
- [Details to be provided in the relevant section]

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## S.N. Data Centre Location
- **1** New Delhi – Primary DC
- **Consignee**: GM/PRS
- **Tel**: 011-24104125

- **2** Secunderabad – DR DC
- **Consignee**: GM/PRS/SC

## 8. Performance cum Warranty Guarantee (PBG) Bond
- It will be applicable as per Standard Bid Document Part-I

## 9. Project Deliverables and Timelines
- The delivery schedule is distributed across PRS data centres (section 7.8 and 7.9).
- The work shall be executed as per timelines defined below. The following is the broad time Schedule in weeks:

| S.No. | Task Description                                      | Weeks from Schedule | Milestone Dependency | Related item No. of SoR (Annexure – II) |
|-------|------------------------------------------------------|---------------------|----------------------|-------------------------------------------|
| T1    | Supply of all Software components as specified in SoR for primary and DR site | D + 4               | NIL                  | Item no. 1 to 36                         |
| T2    | Installation, configuration of all supplied items at primary and DR site and setting up of Replication along with preparation of installation report along with application migration w.r.t supplied Transaction Data Store | D + 8               | T1                   | Item no. 37                              |
| T3    | Final Acceptance Test Procedure at primary and DR site deployment. | D + 10              | T2                   | Item no. 37                              |
| T4    | System go-live at primary and DR site                | D + 14              | T3                   | Item no. 37                              |
| T5    | Commissioning of the system at primary and DR site after 28 days of successful operations. | D + 14              | M1                   | Item no. 1 to 37                         |
| T6    | OEM Training                                         | D + 14              | M2                   | NIL                                       |

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Commencement of comprehensive maintenance services at
- **D + 14**
- **M3**
- **T5(M1)**
- **Item no. 39 to 41**

## Commencement of OEM man-day support at
- **D + 14**
- **M4**
- **T5(M1)**
- **Item no. 42 to 50**

## 9.1 Responsibility matrix
A broad-level responsibility assignment matrix is given below, where all key activities are mentioned. Each activity is mapped out every task, milestone or key decision involved in implementation of the Data Layer Solution for Next Generation Passenger Reservation System. Further, it also covers which roles are Responsible for each action item, which personnel are Accountable, and, where appropriate, who needs to be Consulted or Informed.

- **CRIS**: Customer who has floated the bid document.
- **SI**: Selected SI through the bid document.
- **OEM**: OEM of the Technology provided in the solution.

- **[R]esponsible**: This party oversees completing the task.
- **[A]ccountable**: This party endorses the result of the task.
- **[C]onsulted**: This party needs to be asked for feedback, and feedback needs to be considered.
- **[I]nformed**: This party needs to be kept up to date with the progress of the plan development.

| S.No. | Activity to be performed                                  | CRIS | SI   | OEM  |
|-------|---------------------------------------------------------|------|------|------|
| 1     | Signing of the Contract                                   | R,A  | R,A  | R,I  |
| 2     | Supply of all Software components as specified in SoR     | C,I  | R,A  | R,A  |
|       | for primary and DR site                                   |      |      |      |
| 3     | Submission of Project plan                                 | C    | R,A  | R,C  |
| 4     | Submission of the High-level Design document and          | C,I  | R,A  | R,C  |
|       | deployment architecture for all the supplied              |      |      |      |
|       | components and have it reviewed and approved by the      |      |      |      |
|       | OEMs in consultation with all the stakeholders            |      |      |      |
| 5     | Submission of Functional Requirement specification,       | C,I  | R,A  | R,C  |
|       | Software Requirement specification, HLD, and LLD, as     |      |      |      |
|       | per the bid document Scope of work for all Software      |      |      |      |
|       | components of PRS Data layer.                             |      |      |      |
| 6     | Traceability matrix for verification based on the        | C,I  | R,A  | R,C  |
|       | requirements in the Design Workshop, Scope of Work      |      |      |      |
|       | and Deliverables.                                        |      |      |      |

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- Software installation, configuration and Integration by OEM technical resources as per the approved project plan.
- Provisioning of Monitoring Dashboard for all the software components as per the bid document.
- Provisioning, management and administration for all security services as per the bid document.
- Provisioning and Management of Backup services as per the bid document.
- Configuration of DR replication and required processes for all supplied software components of PRS Data Layer.
- Final Acceptance Test Procedure at primary and DR site deployment.
- System go-live at primary and DR site.
- Commissioning of the system at primary and DR site after 28 days of successful operations.
- Technical training sessions of all software components for PRS Data layer to CRIS Tech Team.
- Commencement of comprehensive maintenance services including Resident Engineers (REs) at Primary and DR Site for 3 years.
- Commencement of OEM man-day support at Primary Site and DR Site for 3 years.

**Note:** N/A refers to Not Applicable.

**Note:** The week counts mentioned herein are inclusive of all types of non-working days (Central Government).

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 10. Liquidated damages in Delay in Delivery and Commissioning
Any delay by the bidder in the performance of the delivery obligations shall render him/her liable to Liquidated Damages as follows:

| S.No. | Task Description                                      | Schedule Weeks | Milestone Related item S | LD (In case of delay in delivery/execution) |
|-------|------------------------------------------------------|----------------|--------------------------|----------------------------------------------|
| (1)   | (2)                                                  | (3)            | (4)                      | (5)                                          |
| T1    | Supply of all Software components as specified in SoR for primary and DR site | D + 4          | Item no. 1 to 36        | NIL                                          |
| T2    | Installation, configuration of all supplied items at primary and DR site and setting up of Replication along with preparation of installation report along with application migration w.r.t supplied Transaction Data Store | D + 8          | Item no. 37             | NIL                                          |
| T3    | Final Acceptance Test Procedure at primary and DR site deployment. | D + 10         | Item no. 37             | NIL                                          |
| T4    | System go-live at primary and DR site                | D + 14         | Item no. 37             | NIL                                          |
| T5    | Commissioning of the system at primary and DR site after 28 days of successful operations. | D + 14         | M1                       | @ 0.5% of the total value of related SoR items in column (5) for each week or part thereof for each data center. |

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409) Page 49 of 124
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- Total LD shall not exceed 10% of the total value of related SoR items in column (5) for each data center.

## Milestones

- **T6 OEM Training**
D + 14 M2 Item no. 38 NIL

- **T7 Commencement of comprehensive maintenance services at Primary and DR Site for 3 years**
D + 14 M3 Item no. 39 to 41 NIL

- **T8 Commencement of OEM man-day support at Primary Site and DR Site for 3 years**
D + 14 M4 Item no. 42 to 50 NIL

* Total LD on all milestones put together shall not exceed 10% of the total contract value.

## Inspection and Acceptance Test Procedure (ATP)

- The inspection and acceptance procedure (ATP) for the item supplied as per SoR shall be carried out jointly by the consignee or its nominated representative and the vendor as per details given below.

### 11.1. Preliminary Testing

- **11.1.1.1.** Physical verification of equipment/components as per the Bill of Material (BoM) supplied against SoR.
- **11.1.1.2.** Physical inspection of the equipment/components for any physical damage.
- **11.1.1.3.** Physical verification of software media, licenses and documentation (which shall also include Installation tie-up and ATS certificates from OEM) as per tender.
- **11.1.1.4.** Preliminary Testing certificate (as per format in Annexure-X (31.1)) to be signed jointly by CRIS and the successful bidder.
- **11.1.1.5.** The date of issue of Preliminary test certificate shall be termed as date of Preliminary Testing.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 11.2. Final Acceptance Testing

Following are the activities completed, before starting the final acceptance testing process:

1. Design Workshop conducted by Bidder with OEM and CRIS for understanding Functional, Technical, security and migration requirements along with System Study and finalization of Deployment architecture for Primary and DR Site.

2. Submission of Low-level Design Document, Deployment Architecture, DR Replication (for Primary and DR Site), implementation Plan and Project Plan detailing each task with target date and assigned resource persons (OEM/Solution Provider) including the plan for installation of all supplied items and integration with existing infrastructure.

3. Supply of all Software components as specified in SoR for primary and DR site.

4. Application migration w.r.t supplied Transaction Data Store.

5. Installation and configuration of all supplied items at primary and DR site and setting up of Replication along with preparation of installation report.

The final acceptance testing shall be carried out jointly by CRIS and the bidder for all the items in the SoR to verify the following:

a) Verification of item-wise compliance on technical specifications from respective OEMs for all the items of SoR.

b) Technical specifications of all the Software and its supporting components from the SoR will be verified through physical inspection or verification from product brochure or manufacturer certification/document or Certificate/Report from respective regulatory agency or conducting a test as per Annexure.

c) Installation and configuration of complete solution as given in scope of work (section 4) and deployment architecture specified in section 3.2.

d) Installation and configuration of products supplied by vendor services as per finalized deployment architecture.

e) Verification of “No Single Point of Failure” in overall solution.

f) Verification of “No Data Loss” in overall solution.

g) Demonstration of functional requirements of all the Software and its supporting components (Annexure III).

h) Evaluation of Technical use cases of all the Software and its supporting components (Annexure XI).

i) The bidder will have to demonstrate with suitable tools the above defined performance level.

j) Compliance to Security Requirements as per section 4.5 and submission of report.

k) Configuration of Backup and restore process as specified in section (section 4.7).

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Post Final Acceptance Activities

- Application Deployment at primary and DR site and testing by CRIS with technical support by Bidder and OEM
- Fine tuning of supplied software w.r.t. Security and submission of the compliance report vis-à-vis the defined Security Architecture (SA) at primary and DR site
- System go-live at primary and DR site and commencement of comprehensive maintenance services at Primary and DR Site

## System Commissioning

### 11.3.1
- The System commissioning certificate shall be issued only after ascertaining that the system is performing satisfactorily for a continuous period of 4 weeks after Date of Final Acceptance.

### 11.3.2
- The entire system will be considered as commissioned once the acceptance testing has been completed successfully and the system performs satisfactorily for a continuous period of 1 month post completion of acceptance testing.

### 11.3.3
- Submission of a final Installation Report clearly indicating the installation, Detailed Connectivity Diagram, finalized deployment architecture etc.

### 11.3.4
- Re-Submission of documents/Reports submitted in Final Acceptance stage after incorporating CRIS review comments.

### 11.3.5

### 11.3.6
- A System commissioning certificate as per Performa given in Annexure-X (31.3)

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 12. Payment Terms
The Schedule of payments to the Successful bidder will be as under:

| S. No. | Payment Stage          | Project Implementation Milestone | Payments as % of total value | |
|--------|-----------------------|----------------------------------|------------------------------|---|
| 1      | System Commissioning   | M1                               | Payment will be made annually for first year, second year and third year of the cost of ICT Components (Software and Hardware) supplied at primary Site and DR Site (As per SoR, S No. 01 to 36). Following documents are required to be furnished for primary and DR Site: - 1. Successful completion of Preliminary Testing certificate (Annexure –X section 31.1). 2. Final Acceptance Certificate (Annexure –X section 31.2). 3. System Commissioning Certificate (Annexure –X section 31.3). 4. Consumption of OEM Man-days, if any (attendance sheet duly verified by CRIS). 5. Confirmation of the validity of PBG as per SBD-1 | 100 % of the Implementation cost (As per SoR, S. No. 37). |
| 2      | Training Cost         | M2                               | 100% of the training cost (As per SoR, S. No. 38) shall be paid after completion of training to the satisfactions of the consignee and upon furnishing the following documents: - 1. Training Completion certificate from CRIS team (Training should be initiated in parallel to implementation) 2. Confirmation of the validity of PBG as per SBD-1 |  |

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409) Page 53 of 124
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## S. No. Payment Stage
### Project Implementation Milestone
- **3 Comprehensive maintenance support for 03 years**
- Payments for comprehensive maintenance support cost will be made every quarter at the end of the quarter on submission of certificate of satisfactory maintenance.
- Payment will be calculated after deducting penalties if any.
- Payment will be made on quarterly basis on completion of Help desk support subject to submission of performance certificate (As per SoR, S No.39 to 41).
- Confirmation of the validity of PBG as per SBD-1.

- **4 OEM Man-days for First year, Second year and third year**
- On OEM man-day consumption basis to be paid half yearly on submission of OEM man-days consumption certificate.
- On submission of documentary proof for OEM Man-days consumption on half yearly basis (As per SoR, S No. 42 to 50) from solution provider.
- Confirmation of the validity of PBG as per SBD-1.

## 12.1. Enhancement and reduction of quantities
- The option clause allowing for the Enhancement and reduction of 30% quantities of procurement order (as per Para 21 of the CRIS SBD-I) will not be applicable for this tender.

## 13. Documentation
- Bidder shall submit the following documents during the lifecycle of the project:
- **13.1** Requirements document as per Design Workshop conducted by Bidder and OEM.
- **13.2** High Level Design Document.
- **13.3** Low level Design document including Deployment Architecture document with diagram as well as descriptions for both the Primary and DR DC.
- **13.4** Implementation Plan.
- **13.5** Testing Plan and Test Cases.
- **13.6** Traceability Matrix.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 13.7 Installation Reports
## 13.8 Documentation of complete setup including installation, configuration, customization, Administration, Maintenance.
## 13.9 Product Manuals.
## 13.10 Training Materials.
## 13.11 Document of Knowledge Transfer (KT)
## 13.13 Any other relevant document

* The equipment must be accompanied by original documentation and full set of accessories given by the manufacturer.

## 14. Role of CRIS
### 14.1
Shall provide the infrastructure as mentioned in section 3.2.5 for Installation of software products supplied by the bidder.
### 14.2
### 14.3
Review and finalization of the detailed Project implementation plan prepared by the bidder / OEMs shall be done by CRIS.
### 14.4
Review and finalization of the system deployment architecture prepared by the bidder / OEMs shall be done by CRIS.
### 14.5
Shall provide the queries for migration.
### 14.6
Development, deployment, performance tuning and maintenance of IR New age PRS Application deployed on this setup shall be done by CRIS.
### 14.7
Review and finalization of all training curriculum for CRIS team.
### 14.8

## 15. Make in India Compliance
As per CRIS SBD-I (including modifications).

## 16. Land Border with India Compliance
As per CRIS SBD-I (including modifications).

As per CRIS SBD-I (including modifications).

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

Following are the details of Physical servers that are available to be used in Next Generation PRS Data Layer Transactional data store (as mentioned in section 3.3.1). The 2.5 NVME SED SSD disk based SAN Storage will also be provided.

### A1-Hardware for Primary DC

| S no. | Item Description | Product Offered (Model/Version) | Quantity (Nos) |
|-------|------------------|----------------------------------|-----------------|
| 1     | Database Nodes with 3-year warranty for Primary DC | DELL PowerEdge R750 Server | 5 - Production Environment
1 – Staging Environment |

### A2-Hardware for DR DC

| S no. | Item Description | Product Offered (Model/Version) | Quantity (Nos) |
|-------|------------------|----------------------------------|-----------------|
| 2     | Database Nodes with 3-year warranty at DRDC | DELL PowerEdge R750 Server | 5 |

**Model:** Dell PowerEdge R750 Server
**Mother Board:** R750 Motherboard with Broadcom 5720 Dual Port 1Gb On-Board LOM
**Processor:** 2 * Intel Xeon Platinum 8358 2.6G, 32C/64T
**Memory:** 1 TB (16 * 64GB RDIMM, 3200MT/s, Dual Rank, 16Gb)

**Disk:**
```
2 * 1.92TB SSD SATA
4 * 3.84TB NVMe
```
**Network Card:** 6 * 25GbE (SFP28 SR Optic)
**HBA Card:**
```
1 * Emulex LPE 35002 Dual Port 32 Gb Fibre Channel HBA, PCIe Low Profile
1 * Emulex LPE 35002 Dual Port 32 Gb Fibre Channel HBA, PCIe Full Height
```

## 19. Annexure IB – List of Software and Hardware Components
Following are the list of Software and Hardware components that will be used in Next Generation PRS:

|---------|--------------------|---------|-------------------|------------------|------------------|
| 1       | Container orchestration Platform (Kubernetes) with capabilities of SDN, Backup capabilities of environment, Service Mesh (ISTIO) and Kubernetes Monitoring | Environment | Enterprise | Red Hat OpenShift Container Platform (Version 4.12 or higher) | Already Procured through separate RFP |
| 2       | Virtualization layer | Environment | Enterprise | (Redhat OpenStack 17.1 or higher) | Already Procured |

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Procurement Details

- **Operating System**
- **Environment**: Enterprise
- **Version**: RHEL 9.x
- **Status**: It will be procured through this RFP for Transactional data Store servers

- **Container Registry**
- **CI-CD**: Enterprise
- **Product**: Red Hat Quay
- **Status**: Already Procured through separate RFP

- **IAM (Open ID Connect)**
- **Authorization and Authentication**
- **Status**: Separate RFP

- **SAN Storage**
- **Environment**: Enterprise
- **Product**: Dell EMC PowerStore 5x00T
- **Status**: Already Procured through separate RFP

- **Hardware Load Balancer**
- **Environment**: Enterprise
- **Status**: Already Procured through separate RFP

- **Argo CD**
- **CI-CD**: Enterprise
- **Status**: Already Procured through separate RFP

- **HELM Chart**
- **CI-CD**: Community
- **Status**: Open Source product

- **GIT Gogs**
- **CI-CD**: Community
- **Status**: Open Source product

- **Tekton**
- **CI-CD**: Enterprise
- **Status**: Already Procured through separate RFP

- **MinIO**
- **Object Storage**: Community
- **Product**: Dell EMC ECS Storage EX500
- **Status**: Already Procured through separate RFP

- **Streaming platform - KAFKA**
- **Event**: Enterprise
- **Product**: Red Hat Application Foundations, Cluster Edition
- **Status**: Already Procured through separate RFP

- **AMQP (with Streaming Capabilities)**
- **Messaging and Streaming**: Enterprise
- **Status**: Already Procured through separate RFP

- **In Memory data Grid (IMDG)**
- **Caching**: Enterprise
- **Status**: It will be procured through this RFP

----

**File No.**: CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
**Page**: 57 of 124
**Generated by**: Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Software Components

- **RDBMS**
- Type: Static and Config DB
- License: Enterprise
- Procurement: It will be procured through this RFP

- **Backup Software**
- Type: Backup
- License: Enterprise
- Procurement: Separate RFP

- **ELK/EFK**
- Type: Application Logging
- License: Community
- Procurement: Open Source product

- **Prometheus**
- Type: Monitoring
- License: Community
- Procurement: Open Source product

- **Grafana**
- Type: Monitoring
- License: Community
- Procurement: Open Source product

- Type: Transactional DB
- License: Enterprise
- Procurement: Through this RFP

- **API Gateway**
- Type: Third party integration
- License: Enterprise
- Vendor: WSO2
- Procurement: Procured through separate RFP

- **External DNS**
- Type: PRS DNS
- License: Community
- Procurement: Open Source product

- **Cert-Manager**
- Type: Kubernetes certificate management controller
- License: Community
- Procurement: NA

- **Kafka Manager**
- Type: Kafka Management UI
- License: Community
- Procurement: NA

- **Goofys**
- Type: S3 File system
- License: Community
- Procurement: Open Source product

- **Zookeeper**
- Type: Distributed synchronization
- License: Community
- Version: 3.6
- Procurement: Open-Source product

- **Object Storage**
- Type: Object Storage
- License: Enterprise
- Vendor: Dell EMC ECS EX500 Storage
- Procurement: Procured through separate RFP

- **SAN storage**
- Type: SAN storage
- License: Enterprise
- Vendor: Dell EMC PowerStore
- Procurement: Procured through separate RFP

## Annexure IC – Details for DR Site Data Replication

The replication of required data will be configured in Next Generation PRS using the capability of the product deployed in the setup. Following are the details of the product to be deployed in the DR site along with replication requirement and its mechanism.

| Sl. No. | Software Component | Deployed at PR Site | Deployed at DR Site | Replication Required | Replication Mechanism | Responsibility |
|---------|--------------------|---------------------|---------------------|---------------------|-----------------------|----------------|
| 01      | RDBMS              | Y                   | Y                   | Y                   | Replication will be configured using product capability | Respective RFP - OEM/Bidder to configure the |

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Replication Mechanism

- **Data Store for Transactional Data**
- Y
- Y
- Y
- Replication will be configured using product capability
- Respective RFP - OEM/Bidder to configure the replication mechanism

- **In Memory Data Grid (caching)**
- Y
- Y
- Y
- Replication will be configured using product capability
- Respective RFP - OEM/Bidder to configure the replication mechanism

## Annexure ID – Backup Details

Following are the indicative details of Data Backup that need to be taken along with Methodology. Detail plan along with frequency of backup will be decided during the design phase as per the proposed solution.

| Sl. No. | Software Component                        | Backup Data Details       | Methodology                               |
|---------|------------------------------------------|---------------------------|-------------------------------------------|
| 2       | Data store for Transactional Data        | Configuration and Data    | To be configured as per proposed OEM methodology |
| 3       | In Memory Data Grid (caching)            | Configuration             | To be configured as per proposed OEM methodology |

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Annexure IE - Details of components of Overall System Deployment Architecture

The deployment of Next generation Passenger Reservation System is planned to be done by following the architecture given below:

```
EXTERNAL
G2G     B2C         B2BAGEN     DISPLAY    EXTERNAL SYSTEM FOR INTEGRATION
EXTERNAL GATEWAY                                    SYSTEMS

API GATEWAY                                                                     UIDAI

MANAGEMENT                     FIREWALL                           INTERNAL SYSTEMS
COUNTER       NGET
CONSUMER IDENTITY                                                  CALL CENTRES  WEBPRS
PROVIDER                   CRIS RIDC DMZ

ADC                                                              OTHERS

FIREWALL

Militarized Zone    SERVER LOAD BALANCER

ALERTING    Microservices
Application

APPLICATION
TELEMETRY    RDBMS  In-Memory Dat  Messaging / Event  Zookeeper    Transactional

DIAGNOSTICS
Kubernetes Cluster

Virtual Instances    Container Platform                            Bare Metal Host

Virtualisation Layer                                    Bare Metal Servers

Management Nodes    Storage    Compute
```

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409) Page 60 of 124
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Components of Next Generation Passenger Reservation System

### 22.1. Physical Servers

The next generation PRS is deployed using the x86 based commodity servers. These servers will be primarily classified as:

- Management Nodes
- Compute nodes for Application workload

### 22.2.1. Management Nodes

The Management nodes will be used for the deployment of the management components of various software products and its portals, offered in the bid. These management components need to be configured in high availability with active-active mode. Following are the indicative management components that need to be deployed on these nodes:

1) Infrastructure Services
- a) DHCP servers
- b) NTP servers, should be deployed in bare-metal servers
- c) DNS servers
- d) HTTP Proxy servers
- e) Air gaped mirror instances
2) Kubernetes Master Nodes along with etcd
3) Kubernetes monitoring related components e.g., Prometheus, Thanos, etc.
4) Kubernetes Dashboard
5) Kubernetes RBAC manager related components
6) Cluster Log shipping related components e.g., Fluentd etc.
7) Cluster Auto scalers to scale Kubernetes cluster nodes up and down
8) Hardware Load-Balancer Orchestrator related components to configure load balancing of Kubernetes service in hardware load balancer
9) Virtualization Management, Automation, Monitoring and its Components
10) Virtualization SDN Management, Automation, Monitoring and its Components
11) Container Platform Management, Automation, Monitoring and its Components
12) Container Platform SDN Management, Automation, Monitoring and its Components
13) Container Image Registry and its components
15) SAN Storage Management and its Components
16) LDAP and Identity and Access Management and its Components
17) Help Desk Management and its Components
18) Backup Management and its Components
19) Any Kind of Operations Management and its Components
20) And any other Management related Components

All logs will be preserved for 180 days for Network and Security equipment and for all other hardware and software, 1 year logs shall be kept.

### 22.2.2. Compute Nodes for Application Workload

```plaintext
File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm
```

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Compute Nodes
The Compute nodes will be used for running the application. These Nodes can be categorised as:
- Kubernetes Worker Nodes
- Transaction Database Nodes

### 22.2.2.1. Kubernetes Worker Nodes
These compute nodes will be the part of the Kubernetes cluster and these nodes will act as a worker node. On these servers, various micro-service applications will be deployed with their multiple layers like:
- Data layer (IMDG and Static DB)
- Business layer
- Service layer
- Presentation layer

These servers would be high compute capable, as application workload would be running on these servers.

### 22.2.2.2. Transaction Database Nodes
These compute nodes will be used to deploy the NoSQL Database used for online transaction processing purposes.

## 22.2. SAN Storage
The SAN Storage will be used as the Storage layer and all the application data, logs, and monitoring data will be stored on this layer. For high performance, a set of NVMe disk pool will also be configured in this layer. Additionally, SAN storage will be used for storing data for analytics purposes. SAN storage needs to provide Volumes to Bare-Metal, VMs, and Kubernetes workloads.

The SAN storage should have the capability to provide raw partition, shared partition, LUN to Bare-Metal servers and VMs.

## 22.3. Container Platform
The next generation PRS will use Kubernetes as a Container platform which will provide a framework to run distributed systems resiliently. Kubernetes will provide capabilities like:
- Service discovery and load balancing
- Storage orchestration
- Automated rollouts and rollbacks
- Automatic bin packing
- Self-healing
- Secret and configuration management

Multiple micro-services mapped to various business services will be deployed as a container on this setup and will scale-out as per the application load. To handle the peak load, Kubernetes setup will burst to cloud (on-prem and public) setup on need basis. The Kubernetes setup with the capability of deploying across multiple Datacentres will provide the benefits of Disaster Recovery Site.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 22.4. Service Mesh

A service mesh is a configurable, low-latency infrastructure layer designed to handle a high volume of network-based inter-process communication among application infrastructure services using application programming interfaces (APIs). A service mesh ensures that communication among containerized and often ephemeral application infrastructure services is fast, reliable, and secure. Service mesh reduces the complexity associated with a microservice architecture and provides functionalities like:

- Load Balancing
- Service discovery
- Health checks
- Authentication
- Traffic management and routing
- Circuit breaking and failover policy
- Security
- Metrics and telemetry
- Fault injection

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 22.5. Application Service Gateway

The services of Next generation PRS deployed over Kubernetes will be accessed by multiple client applications. These client applications can be primarily classified as:

### Internal Client Applications
- Applications that are deployed within the CRIS datacentre but outside the Kubernetes cluster. These applications will access the services over the CRIS internal network.
- Counters – Ticket booking counters located at Railway Premises or Non-Rail Head.
- NGET - Next Generation E-Ticketing (NGET) application is the enhanced internet ticketing Web Site for Rail ticket booking system.
- Others:
- i. PMS - PNR details, Dog cat booking.
- ii. NTES/ICMS - Train cancellation, delay.
- iii. WECRS - For TDR refund.
- iv. HHT - Web Service for Vacant Berth (Not turned up passenger) Release, FTP of chart files.
- v. HRMS - Integration with HRMS for pass booking.
- vi. GST - Integration using TIBCO.
- vii. Retiring Room - Integration during booking and cancellation, PNR enquiry is given to Retiring room.

### External Client Applications
- Third-party applications deployed outside the CRIS datacentre. These applications will access the services over the internet.
- a. Banks – CPG (POS, UPI, QR code), NCM card - POS, UPI during booking. Offline refund initiation next day.
- b. UIDAI - Aadhaar validation during user registration.
- c. Others:
- i. B2B - Business to Business Agents.
- ii. B2C - Business to Consumer Agents (e.g., Make My Trip, Yatra, etc.).
- iii. G2G - Government to Government (e.g., CGDA, CRPF, BSF, etc.).
- iv. G2C - Government to Consumer (G2C).

Following components will be deployed to provision access to the services to different client applications:

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 22.5.1. Ingress Controller

- In Kubernetes, an Ingress Controller is an object that allows access to your Kubernetes services from outside the Kubernetes cluster.
- Configure access by creating a collection of rules that define which inbound connections reach which services.

```
Incoming request

Cluster  Ingress

Service    Service

Pod      Pod        Pod
```

- The internal client application will access the next generation PRS services through Ingress Controller or Hardware Load-balancer.

## 22.5.2. API Gateway

- An API gateway takes all API calls from external clients coming over the internet, then routes them to the appropriate microservice with request routing, composition, and protocol translation.
- Typically, it handles a request by invoking multiple microservices and aggregating the results, to determine the best path.
- It can translate between web protocols and web-unfriendly protocols that are used internally.
- The API gateway will forward the request to Ingress controller or Hardware Load-balancer for service access.

## 22.5.3. Hardware Load Balancer

- Hardware based Load Balancer will forward all the south bound traffic to the Kubernetes clusters and to any other service provisioned to be load balanced.
- Hardware based Load Balancer should provision load-balancing for Kubernetes service of type “Load Balancer”, it should integrate with Container Management Platform for the same.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 22.6. Data Layer

- The data layer of Next Generation PRS will be polyglot and will depend on the requirements of the micro-service. Based on the performance, consistency and persistency needs, the following components will be present:

## 22.7.1. In-Memory Data Grid

- For services requiring faster data access, IMDG will be used for storing the service data and will be deployed in Kubernetes.

## 22.7.2. Database

- To maintain static and configurable data, a relational database will be used and will be deployed in Kubernetes.
- To manage the online transactional data, a NoSQL database will be used, deployed over the bare metal servers outside the Kubernetes Cluster. Configuration will be done to achieve optimum communication between this database and the application deployed over the Kubernetes cluster.

## 22.7. Event Broker Platform

Event Broker platform is required for the following functional requirements:

- **Main transaction flow**
- a. Saga pattern (Orchestration and Choreography)
- b. Chained request-response mechanism
- i. Controller microservice will initiate the booking transaction and post the transaction data in the event broker topic. Desired service will consume, process, and post the data in the desired topic.
- ii. Next service will consume from the topic and process. This flow will execute subsequently until the end of the transaction, with the final response being consumed by the Controller micro-service.
- To implement CQRS by updating the read query database through separate micro-services.
- Charting - Read multiple records from DB and send to the charting application through the event Broker platform.
- Data Change History / Journaling - for post facto analysis.
- Add-on services - like
1. SMS
2. Mail
3. Catering, etc.

----

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 22.9. Logging and Diagnostics
- For logging and diagnostics, ELK (Elasticsearch, Logstash, Kibana) or EFK (Elasticsearch, Fluentd, Kibana) stack will be implemented.

## 22.10. Identity Access Management
- An Identity and access management solution will be used for authentication and authorization of underlying infrastructure, virtualization platform, and container platform.
- Bidder needs to integrate with the existing IAM and PIAM solution (details mentioned in Annexure XIX).
- In case the provided container or virtualization platform does not integrate with the existing solution, then the bidder needs to provision the required solution.

## 22.11. Data Backup
- Backup of Configuration and application Data in a specific frequency needs to be configured in the system.
- The indicative list of Configuration and application Data is defined in Annexure ID.

## 23. Annexure – II: Schedule of Requirements

| S. No. | Item Description                     | Technical Spec | UoM | Qty | Line item | Product offered | Remarks |
|--------|--------------------------------------|----------------|-----|-----|-----------|-----------------|---------|
| A1     | Data layer for Primary DC - Mandatory| S-1            | Solution | 1   | Clause 3 and 4 | Provide breakup details of Solution (Software component) as per format given in Annexure XIV |         |
| 1      | Transactional Data Store - with supporting components and underlying Operating System for Production environment - Annual Subscription Cost for first year - for Primary DC | | | | | | |

----

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Transactional Data Store

- **S-1 Solution**
- **Clause 3 and 4**: Provide breakup details of Solution (Software component) as per format given in Annexure XIV
- **Annual Subscription Cost**:
- **Second Year** - for Primary DC
- **Third Year** - for Primary DC
- **First Year** - for Staging environment
- Note: If the bidder does not require Subscription for Staging for solution then fill cost as Rs. 1.
- **Second Year** - for Staging environment
- Note: If the bidder does not require Subscription for Staging for solution then fill cost as Rs. 1.

----

**File No.**: CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
**Generated by**: Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Transactional Data Store

- **S-1 Solution**
- **Clause 3 and 4**: Provide breakup details of Solution (Software component) as per format given in Annexure XIV
- **Annual Subscription Cost for Staging environment - Third Year - for Primary DC**
- Note: If the bidder does not require Subscription for Staging for solution then fill cost as Rs. 1.

- **S-1 Solution**
- **Clause 3 and 4**: Provide breakup details of Solution (Software component) as per format given in Annexure XIV

- **S-1 Solution**
- **Clause 3 and 4**: Provide breakup details of Solution (Software component) as per format given in Annexure XIV

- **S-1 Solution**
- **Clause 3 and 4**: Provide breakup details of Solution (Software component) as per format given in Annexure XIV

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- **RDBMS - with supporting components**
- **Annual Subscription Cost for first year - for Primary DC**
- Note: In case of node-based solution, bidder should calculate the price of total nodes offered and divide it by 12 to quote its equivalent price per core.

- **RDBMS - with supporting components**
- **Annual Subscription Cost for second year - for Primary DC**
- Note: In case of node-based solution, bidder should calculate the price of total nodes offered and divide it by 12 to quote its equivalent price per core.

- **RDBMS - with supporting components**
- **Annual Subscription Cost for third year - for Primary DC**
- Note: In case of node-based solution, bidder should calculate the price of total nodes offered and divide it by 12 to quote its equivalent price per core.

- **IMDG (Cache Software) - with supporting components for Production environment**
- **Annual Subscription Cost for first year - for Primary DC**
- Provide breakup details of Solution (i.e. node details) as per format given in Annexure XIV.

- **IMDG (Cache Software) - with supporting components for Production environment**
- **Annual Subscription Cost for second year - for Primary DC**
- Provide breakup details of Solution (i.e. node details) as per format given in Annexure XIV.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- **15 IMDG (Cache Software) - S-3 Solution**
- Provide supporting components for Production environment
- Annual Subscription Cost for third year - for Primary DC
- Clause 3 and 4 breakup details of Solution (i.e. node details) as per format given in Annexure XIV

- **16 IMDG (Cache Software) - S-3 Solution**
- Provide supporting components for Staging environment
- Annual Subscription Cost for first year - for Primary DC
- Clause 3 and 4 breakup details of Solution (i.e. node details) as per format given in Annexure XIV

- **17 IMDG (Cache Software) - S-3 Solution**
- Provide supporting components for Staging environment
- Annual Subscription Cost for second year - for Primary DC
- Clause 3 and 4 breakup details of Solution (i.e. node details) as per format given in Annexure XIV

- **18 IMDG (Cache Software) - S-3 Solution**
- Provide supporting components for Staging environment
- Annual Subscription Cost for third year - for Primary DC
- Clause 3 and 4 breakup details of Solution (i.e. node details) as per format given in Annexure XIV

- **19 IMDG (Cache Software) - S-3 Solution**
- Annual Subscription Cost for first year - for Primary DC
- Clause 3 and 4 breakup details of Solution (i.e. node details) as per format given in Annexure XIV

----

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- **20 IMDG (Cache Software) -**
- **S-3 Solution**
- Clause 3 and 4
- Provide breakup details of Solution (i.e. node details) as per format given in Annexure XIV
- Annual Subscription Cost for second year - for Primary DC

- **21 IMDG (Cache Software) -**
- **S-3 Solution**
- Clause 3 and 4
- Provide breakup details of Solution (i.e. node details) as per format given in Annexure XIV
- Annual Subscription Cost for third year - for Primary DC

- **B - Data layer for DR DC-Mandatory**

- **22 Transactional Data Store -**
- **S-1 Solution**
- Clause 3 and 4
- Provide breakup details of Solution (Software component) as per format given in Annexure XIV
- Annual Subscription Cost for first year - for DR DC

- **23 Transactional Data Store -**
- **S-1 Solution**
- Clause 3 and 4
- Provide breakup details of Solution (Software component) as per format given in Annexure XIV
- Annual Subscription Cost for second year - for DR DC

- **24 Transactional Data Store -**
- **S-1 Solution**
- Clause 3 and 4
- Provide breakup details of Solution (Software component) as per format given in Annexure XIV
- Annual Subscription Cost for third year - for DR DC

- **25 Transactional Data Store -**
- **S-1 Solution**
- Clause 3 and 4
- Provide breakup details of Solution (Software component) for Staging environment - Annual Subscription Cost

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- Subscription Cost for first year - for DR DC
- Note: If the bidder does not require Subscription for Staging for solution then fill cost as Rs. 1.

- Transactional Data Store - with supporting components for Staging environment
- Annual Subscription Cost for second year - for DR DC
- Note: If the bidder does not require Subscription for Staging for solution then fill cost as Rs. 1.

- Transactional Data Store - with supporting components for Staging environment
- Annual Subscription Cost for third year - for DR DC
- Note: If the bidder does not require Subscription for Staging for solution then fill cost as Rs. 1.

- RDBMS - with supporting components
- Annual Subscription Cost for first year - for DR DC
- Note: In case of node-based solution, bidder should calculate the price of total nodes offered and divide it by 12 to quote its equivalent price per core.

- RDBMS - with supporting components
- Annual Subscription Cost for second year - for DR DC
- Note: In case of node-based solution, bidder should calculate the price of total nodes offered and divide it by 12 to quote its equivalent price per core.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- **30** RDBMS - with supporting components - Annual Subscription Cost for third year - for DR DC
- Note: In case of node-based solution, bidder should calculate the price of total nodes offered and divide it by 12 to quote its equivalent price per core.

- **31** IMDG (Cache Software) - with supporting components for Production environment - Annual Subscription Cost for first year - for DR DC
- Provide breakup details of Solution (i.e. node details) as per format given in Annexure XIV

- **32** IMDG (Cache Software) - with supporting components for Production environment - Annual Subscription Cost for second year - for DR DC
- Provide breakup details of Solution (i.e. node details) as per format given in Annexure XIV

- **33** IMDG (Cache Software) - with supporting components for Production environment - Annual Subscription Cost for third year - for DR DC
- Provide breakup details of Solution (i.e. node details) as per format given in Annexure XIV

- **34** IMDG (Cache Software) - with supporting components for Staging environment - Annual Subscription Cost for first year - for DR DC
- Provide breakup details of Solution (i.e. node details) as per format given in Annexure XIV

- **35** IMDG (Cache Software) - with supporting components for Staging environment - Annual Subscription Cost for second year - for DR DC
- Provide breakup details of Solution (i.e. node details) as per format given in Annexure XIV

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Installation, Support and Services - Mandatory

- **IMDG (Cache Software)**
- **Solution**: S-3
- **Annual Subscription Cost for third year**: 1
- **Clause**: 3 and 4
- **Details**: Provide breakup details of Solution (i.e. node details) as per format given in Annexure XIV

- **Installation and commissioning Charges of supplied products at primary and DR DC**
- **Charges**: Lumpsum
- **Quantity**: 1
- **Clause**: 4.1 to 4.8

- **Training Charges**
- **Clause**: 4.13

- **Bidder Charges for Comprehensive support charges for first year**
- **Clause**: 4.1 to 4.12

- **Bidder Charges for Comprehensive support charges for second year**
- **Clause**: 4.1 to 4.12

- **Bidder Charges for Comprehensive support charges for third year**
- **Clause**: 4.1 to 4.12

- **OEM Man days charges for First year for Transactional Data Store**
- **Charges**: man-days
- **Quantity**: 35
- **Clause**: 4.12

- **OEM Man days charges for Second year for Transactional Data Store**
- **Charges**: man-days
- **Quantity**: 20
- **Clause**: 4.12

- **OEM Man days charges for Third year for Transactional Data Store**
- **Charges**: man-days
- **Quantity**: 20
- **Clause**: 4.12

- **OEM Man days charges for First year for RDBMS**
- **Charges**: man-days
- **Quantity**: 5
- **Clause**: 4.12

- **OEM Man days charges for Second year for RDBMS**
- **Charges**: man-days
- **Quantity**: 5
- **Clause**: 4.12

- **OEM Man days charges for Third year for RDBMS**
- **Charges**: man-days
- **Quantity**: 5
- **Clause**: 4.12

- **OEM Man days charges for First year for IMDG (Cache Software)**
- **Charges**: man-days
- **Quantity**: 15
- **Clause**: 4.12

----

**File No.**: CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
**Generated by**: Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- **OEM Man days charges**
- **for Second year for IMDG (Cache Software)**
- Quantity: 10 man-days
- Clause: 4.12

- **OEM Man days charges**
- **for Third year for IMDG (Cache Software)**
- Quantity: 10 man-days
- Clause: 4.12

## D - Optional Items for Primary DC

- **Transactional Data Store**
- **with supporting components and underlying Operating System for Production environment**
- Quantity: 1 Solution
- Clause: 3 and 4
- Ref: SOR item No. 1
- Subscription for 4th year - for Primary DC

- **Transactional Data Store**
- **with supporting components and underlying Operating System for Staging environment**
- Quantity: 1 Solution
- Clause: 3 and 4
- Ref: SOR item No. 4
- Subscription for 4th year - for Primary DC

- **Transactional Data Store**
- Quantity: 1 Solution
- Clause: 3 and 4
- Ref: SOR item No. 7
- Subscription for 4th year - for Primary DC

- **RDBMS - with supporting components**
- **Subscription for 4th year - for Primary DC**
- Quantity: 12 Number of cores
- Clause: 3 and 4
- Ref: SOR item No. 10
- Note: In case of node-based solution, bidder should calculate the price of total nodes offered and divide it by 12 to quote its equivalent price per core.

- **IMDG (Cache Software) - with supporting components for Production environment**
- **Subscription for 4th year - for Primary DC**
- Quantity: 1 Solution
- Clause: 3 and 4
- Ref: SOR item No. 13

----

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- **IMDG (Cache Software) - with supporting components for Staging environment**
- Solution: 1
- Subscription for 4th year - for Primary DC
- Clause: 3 and 4
- Ref: SOR item No. 16

- Solution: 1
- Subscription for 4th year - for Primary DC
- Clause: 3 and 4
- Ref: SOR item No. 19

- **Transactional Data Store - with supporting components and underlying Operating System for Production environment**
- Solution: 1
- Subscription for 5th year - for Primary DC
- Clause: 3 and 4
- Ref: SOR item No. 1

- **Transactional Data Store - with supporting components and underlying Operating System for Staging environment**
- Solution: 1
- Subscription for 5th year - for Primary DC
- Clause: 3 and 4
- Ref: SOR item No. 4

- Solution: 1
- Subscription for 5th year - for Primary DC
- Clause: 3 and 4
- Ref: SOR item No. 7

- **RDBMS - with supporting components**
- Number of cores: 12
- Subscription for 5th year - for Primary DC
- Clause: 3 and 4
- Ref: SOR item No. 10
- Note: In case of node-based solution, bidder should calculate the price of total nodes offered and divide it by 12 to quote its equivalent price per core.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- **62 IMDG (Cache Software)**
- Solution: 1
- Clause: 3 and 4
- Ref: SOR
- Item No: 13
- Supporting components for Production environment
- Subscription for 5th year
- For Primary DC

- **63 IMDG (Cache Software)**
- Solution: 1
- Clause: 3 and 4
- Ref: SOR
- Item No: 16
- Supporting components for Staging environment
- Subscription for 5th year
- For Primary DC

- **64 IMDG (Cache Software)**
- Solution: 1
- Clause: 3 and 4
- Ref: SOR
- Item No: 19
- Subscription for 5th year
- For Primary DC

## Optional Items for DR DC

- **65 Transactional Data Store**
- Solution: 1
- Clause: 3 and 4
- Ref: SOR
- Item No: 22
- Supporting components and underlying Operating System for Production environment
- Subscription for 4th year
- For DR DC

- **66 Transactional Data Store**
- Solution: 1
- Clause: 3 and 4
- Ref: SOR
- Item No: 25
- Supporting components for Staging environment
- Subscription for 4th year
- For DR DC

- **67 RDBMS**
- Number of cores: 12
- Clause: 3 and 4
- Ref: SOR
- Item No: 28
- Supporting components
- Subscription for 4th year
- For DR DC
- Note: In case of node-based solution, bidder should calculate the price of total nodes offered and divide it by 12 to quote its equivalent price per core.

- **68 IMDG (Cache Software)**
- Solution: 1
- Clause: 3 and 4
- Ref: SOR
- Supporting components for Production environment

----

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- Subscription for 4th year
- for DR DC
- No. 31
- IMDG (Cache Software) - with supporting components for Staging environment
- Solution: S-3
- Clause: 3 and 4
- Ref: SOR
- Subscription for 4th year
- for DR DC
- No. 34
- Transactional Data Store - with supporting components and underlying Operating System for Production environment
- Solution: S-1
- Clause: 3 and 4
- Ref: SOR
- Subscription for 5th year
- for DR DC
- No. 22
- Transactional Data Store - with supporting components for Staging environment
- Solution: S-1
- Clause: 3 and 4
- Ref: SOR
- Subscription for 5th year
- for DR DC
- No. 25
- RDBMS - with supporting components
- Number of cores: 12
- Subscription for 5th year
- for DR DC
- Ref: SOR
- Note: In case of node-based solution, bidder should calculate the price of total nodes offered and divide it by 12 to quote its equivalent price per core.
- item No. 28
- IMDG (Cache Software) - with supporting components for Production environment
- Solution: S-3
- Clause: 3 and 4
- Ref: SOR
- Subscription for 5th year
- for DR DC
- No. 31
- IMDG (Cache Software) - with supporting components for Staging environment
- Solution: S-3
- Clause: 3 and 4
- Ref: SOR
- Subscription for 5th year
- for DR DC
- No. 34
- Optional OEM Man days for 4th and 5th Year

----

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- **OEM Man days charges**
- Days: 20
- For 4th year for Transactional Data Store

- **OEM Man days charges**
- Days: 20
- For 5th year for Transactional Data Store

- **OEM Man days charges**
- Days: 5
- For 4th year for RDBMS

- **OEM Man days charges**
- Days: 5
- For 5th year for RDBMS

- **OEM Man days charges**
- Days: 10
- For 4th year for IMDG (Cache Software)

- **OEM Man days charges**
- Days: 10
- For 5th year for IMDG (Cache Software)

## Note:
2. The bidder has to provide breakup details of Solution (Software component) including operating system as per format given in Annexure XIV.

## Annexure – III: Functional Requirement
### 24.1. Transactional Datastore Solution Functional Requirements

1. Transactional datastore solution will consist of two clusters: one in Primary Data Centre (DC) and the other in Disaster Recovery (DR) DC.

2. The deployment of the transactional datastore solution will utilize all the five physical servers provided by CRIS in the Primary Data Centre (DC) (Annexure IA). If any additional software resources are deemed necessary for the successful implementation of the solution, it is expected that the bidder responding to the RFP will be responsible for furnishing these resources.

3. Both DC and DR cluster of the transactional datastore solution must be configured for zero data loss and maintain consistent write operations.

4. Both the clusters present at primary and DR DC will be up at all times with asynchronous bi-directional replication configured between Primary DC and DR DC. All the services of the transactional datastore solution will be available at both data centres simultaneously with the required capability of read and write.

5. The bidder should demonstrate addition and removal of bare-metal node from both clusters.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

6. The ANSI SQL querying features, provided by a distributed query engine, are used by the CRIS application to generate real-time ticket transaction reports based on various parameters such as payment mode, journey details, passenger type, and other financial transactions from the transactional datastore.

The functional requirements of data processing and aggregation in a transactional datastore solution using these ANSI SQL features, powered by a distributed query engine:

- **Data Aggregation** - using functions like SUM, MAX, MIN, CEILING, ROUND, COUNT etc.
- **Conditional Data Processing** - using CASE WHEN expressions.
- **Data Grouping** - by using GROUP BY clause to support multiple levels of grouping and aggregation for different financial and passenger categories.
- **Nested Queries and Derived Tables** - The application can use nested queries (subqueries) to pre-process and derive intermediate results before final aggregation. The querying mechanism shall allow complex calculations inside derived tables for improved query efficiency.
- **Filtering and Data Selection** - using the WHERE clause to filter records based on multiple conditions.
- **String and Numeric Data** - using CASE WHEN for categorization, shall support string concatenation, string and numeric comparison operations.
- **Conditional Aggregation** – using SUM with CASE WHEN expression.
- **Aliasing for Readability** - shall use aliasing (AS) to rename columns for better readability in reports and query results.
- **Numeric Calculations** - shall support arithmetic operations (+, - , *, /) in query calculations for accurate financial and passenger data processing.
- **Multi-Level Aggregation** - shall perform nested aggregation at different levels of processing (inside subqueries and final queries).
- **Joins** – shall support INNER, LEFT OUTER, RIGHT OUTER, FULL OUTER, CROSS and LATERAL joins.

Note: The Transactional Data Store solution consisting of components required to comply with the technical specification either through the Transactional Data Store product or by integrating with a third-party tool. The complete supplied solution shall be supported as defined in the section 4.9 of the RFP.

7. The bidder should implement all the technical use cases mentioned in annexure XI.

8. A monitoring dashboard should be provided to monitor both the clusters. This dashboard will include but is not limited to the following critical metrics:
- a. Storage - Total, Usage, Free
- b. Memory - Total, Usage, Free
- c. Replication factor of different namespaces/databases
- d. IOPS (Input/Output Operations Per Second)

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- TPS (Transactions Per Second)
- P99 response time for read and write transactions
- Throughput
- User administration
- User role-based access control
- RTO (Recovery Time Objective)
- RPO (Recovery Point Objective)

9. Configuration of the backup and restoration process for the transactional datastore solution.

10. The transaction datastore OEM needs to provide verification of datastore models and adherence to development best practices as it is essential for creating reliable and scalable data-driven applications. The following support needs to be provided but not limited to:
- Schema Validation
- Data Integrity
- Indexing
- Scalability
- Code Review
- Security
- Performance Optimization
- Testing and Test Automation
- Backups and Disaster Recovery Plan and process
- Maintenance Plans

## RDBMS Solution Functional Requirements

1. The RDBMS Solution will be deployed on the container platform.
2. The RDBMS solution should be based on the enterprise version of open source or community version to avoid vendor lock-in.
3. In the primary data centre (DC), the RDBMS solution will be deployed in primary and stand-by mode with synchronous replication.
4. The replication between multiple instances of RDBMS in the same data centre should be in synchronous and writes should be consistent.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## RDBMS Solution Requirements
1. The RDBMS solution in both DC and DR should be configured in High Availability (HA).
2. The storage for the RDBMS solution will be configured through Kubernetes Persistence Volume Claim (PVC).
3. The RDBMS solution should define read-write service, to connect the application to only primary server of the cluster.
4. The RDBMS solution should define read-only service, to connect the application to any of the instances for reading workloads.
5. The RDBMS solution must implement connection pooling for database scalability and transparent application connection to one or more database instances.
- Database instances status
- CPU stats
- Disk status - Total, Usage, Free
- Memory - Total, Usage, Free
- Replication status
- Statements
- Table locks
- Dead lock transactions
- User administration
- User role-base access control
- RTO (Recovery Time Objective)
- RPO (Recovery Point Objective)

## In Memory Data Grid (Caching) Solution Functional Requirements
1. The IMDG cache need to be deployed in a container platform (Redhat Openshift).
2. The IMDG deployed on container platform should adhere to CPU and RAM “request” and “limit” values of the resource management for pods.
3. The IMDG should provide performance monitoring dashboards.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Submission Requirements
- Submission of final installation report to be done by the bidder.
- The bidder should implement all the technical use cases mentioned in annexure XI.

## Annexure – IV: Technical Specification

### 25.1. Transactional Data Store

| Sr. No. | Technical Specification                                                                 | Compliance (Yes/No) |
|---------|-----------------------------------------------------------------------------------------|----------------------|
| 1       | The data-store technology should be developed on the open standards of NoSQL or NewSQL technology. |                      |
| 2       | The data-store technology should be based on enterprise version of open source or community version to avoid vendor lock-in. |                      |
| 3       | The data-store should have capability to get deployed on-premises, Public/Private cloud, or in a hybrid model. |                      |
| 4       | The data-store should have zero data loss feature.                                     |                      |
| 5       | The data-store should allow for active/active reads and writes across multiple geo-separated data centres. |                      |
| 6       | The data-store solution MUST be able to push data to open-source databases platform for online and offline analytics using BI/Analytics tools. The technology should be based on open source to avoid vendor lock-in. |                      |
| 7       | The data-store solution should be a masterless or equivalent share nothing distributed solution. |                      |
| 8       | The proposed data-store should support distributed architecture i.e. data should be distributed across multiple nodes. |                      |
| 9       | The data-store need to be able to scale linearly as you add servers to the cluster.    |                      |
| 10      | The data-store should be able to support general Commodity Hardware, Virtual machines, Containers. |                      |
| 11      | The data-store when scaling by adding servers, no re-sharding on the user side should be necessary, and should automatically be done transparently on the data-store side. |                      |

----

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Data-Store Requirements

- The data-store should scale to multiple data centres with an ability to seamlessly scale.
- The data-store solution should have search and indexing capability. It must provide capability to create primary and secondary indices.
- The data-store should natively support TTL of data so that it can be purged after a specified period of time.
- The data-store must support strong, immediate consistency to prevent any conflicting writes and ensure that reads the most recently committed data.
- The enterprise support is required for all the connectors used for technical compliance of the solution.

## Replication

- The data-store should be capable of allowing real-time replication (in milliseconds) of data within and across data centres to provide redundancy and high availability.
- The data-store should have provision for cross geo, cross data centre replication in asynchronous/synchronous modes.
- The data-store should provide consistency of data and it must be across distributed geographical regions, across data centre in synchronous/asynchronous mode based on the requirement.
- The data-store should provide automated node/availability zone failover across multiple geo-separated data centres.
- The data-store replication and consistency of data has to be flexible and tuneable based on various business requirements.

- The data-store should have pre-built library for various programming languages like C, C#, C++, Go, Java, JavaScript (Node.js), Python, R, Spring Boot and Java Clients.
- The offered data-store should have a supported library to integrate with Spring Boot and Spring Data.
- The data-store should have feature for bulk data loading and integrated stream processing capability to ensure data portability.
- The data-store should offer robust support for various Data Models, allowing developers to work seamlessly with a wide range of NoSQL and NewSQL data models.
- The data-store solution should have ability to store and query (full-text search, faceting, and geospatial search) existing data in the data-store in a relationship or graph oriented way.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Learning Curve
- The offered solution should reduce learning curve for getting productive through the abstraction of data-store specific concepts by supporting popular API options such as REST, GraphQL, and schema-less JSON out of the Box.

## SQL Querying
- The data-store should have SQL or SQL-like quarriable capability for querying through command line interface.
- The data-store solution should also provide supported UI based ANSI SQL based querying tools.

## Performance
- The data-store should support partitioning of storage for faster write and read of data.
- The data-store must be optimized for high-availability, ensuring continuous operation and data accessibility. It should consistently maintain 2 millisecond or less latency for read and 3 millisecond or less latency for write operations (P99 latency), demonstrating efficiency and reliability, even under peak load conditions.
- The data-store solution should have capability to support 1 million transactions per second.
- The data-store should support zero data loss while scaling down the cluster.
- Proposed data-store technology must support hybrid storage architecture i.e. able to store data on DRAM, SSDs, Flash Drives, NVMe, PMEM etc.
- The data-store should support rack aware cluster to know which rack has the available data.
- The data-store should have dynamic cluster management feature to handle node membership management, handling node management trigger at network fault, node addition or removal.
- In case of node failure, system should have capability to automatically rebalance the objects and data to other nodes without impacting required performance.
- In case of services in the node stops, system should not lose the data in RAM and quickly restart as and when the services are restarted.
- The data-store should support zero data loss while scaling down the cluster.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Data Store Requirements
- The data-store should have capability for compression algorithms like LZ4, Snappy, Zstandard for data storage.
- The data-store should provide high availability with uptime of 99.9 or more.
- The data-store system should smartly distribute data evenly across all the nodes.

## CDC and Real-time Streaming
- The data-store solution should be able to natively de-duplicate the data and send it to downstream application for further processing like search, analytics, backup, etc.
- The data-store solution should provide tools to bring in and out the change data capture (CDC) into data platform on real-time basis.
- The data-store should provide integrated solution to transform, join, merge, etc., data in real-time bases.
- The data-store should support Kafka integration for both upstream and downstream data in real time.
- The data-store should integrate pub-sub tools to provide stream data into and out of underlying data store.

## Analytics Requirements
- Should integrate with Spark analytics that allows for hybrid transactional/analytical transaction processing and Spark streaming.
- Should support integrating with an external Spark system.
- Native capability to Spark stream and spark batch without requiring multiple drivers to be installed.

## Security Requirements
- Secure data and protect privacy using encryption, role-based access control, and single sign-on.
- Detect and prevent potential breaches through configurable auditing and log scanning and filtering.
- Should support role based authentication (RBAC).
- Should support integration with LDAP.
- Provide the ability to audit data-store operations.
- Provide data-store level transparent data encryption.
- Proposed data-store must support data encryption in motion (TLS 1.2) and encryption at rest (AES - 126 and AES 256).
- Data-store should also support TLS/SSL features.

## Manageability
- [Content not provided in the OCR text]

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Monitoring and Management
- Should include a comprehensive monitoring dashboard for centralized cluster monitoring and offer a set of dashboard or command-line tools for efficient cluster management.
- Should support provision, upgrade, Backup/Restore and manage the cluster through a central dashboard or command-line.
- The data-store should support rolling upgrades so that system should not be down while troubleshooting, upgrade or applying patches.
- The data-store solution should provide central dashboard to perform real-time monitoring at different levels such as data-store cluster, data-store instances, CPUs, Disk Storages, Memory, Clients.
- The data-store central dashboard for monitoring system should be able to generate alerts when a certain set threshold is crossed and should be able to generate notifications about alerts.

## Backup
- The data-store solution should provide full/snapshot and incremental backup features.
- The data-store solution should also provide backup restoration feature.
- Users should be able to take complete data-store backup online and in parallel. The restoration of the complete data-store should also be possible in parallel.
- The data-store solution should have a feature of backup to a S3 compliant object store and full recovery of the backup from an existing backup in an object store.

## Performance Requirements for Day One
- The data-store must demonstrate the capability to sustain high throughput, supporting up to 1,50,000 read transactions per second. Each transaction should be processed with a P99 latency of 2 milliseconds or less for reads operations. It must also ensure high availability and fault tolerance, maintaining consistent performance and data integrity in various operational scenarios.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Data-Store Requirements

- The data-store must excel in handling write-intensive workloads, capable of managing up to 25,000 write transactions per second with a P99 latency of less than 3 milliseconds or less for writes.
- It must also ensure high availability and fault tolerance, maintaining consistent performance and data integrity in various operational scenarios.

- The data-store must have capacity to provide usable storage for 6TB of unique data.
- The data-store must meet all the criteria mentioned in points 71, 72, and 73.

## Scalability in Performance

- The data-store must have the capability to sustain high throughput, supporting up to 2,50,000 read transactions per second.
- Each transaction should be processed with a P99 latency of less than 2 milliseconds or less for read operations.
- It must also ensure high availability and fault tolerance, maintaining consistent performance and data integrity in various operational scenarios.

- The data-store must excel in handling write-intensive workloads, capable of managing up to 40,000 write transactions per second with a P99 latency of less than 3 milliseconds.
- It must also ensure high availability and fault tolerance, maintaining consistent performance and data integrity in various operational scenarios.

- The data-store must have capacity to provide usable storage for 12TB of unique data.

## Case Studies

- At least two live case studies of large scale implementation in the travel/transport/finance industry in the OLTP environment worldwide.

## RDBMS Compliance

| Sr. No. | Technical Specification                                   | Compliance (Yes/No) |
|---------|----------------------------------------------------------|----------------------|
| 1       | The RDBMS should be an open source RDBMS or based on an Open Source Stack. |                      |

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## RDBMS Solution Requirements
- The RDBMS solution should have capability to get deployed using Helm charts and Kubernetes Operators CRD's.
- Databases should have built-in capabilities necessary to integrate and manage other data sources for structured, unstructured and NoSQL/NewSQL databases and deploy rapidly across multiple environments.

## Compliance and Features
- The RDBMS system should conform to the ANSI-SQL:200n standard.
- The RDBMS should have fundamental database features such as full ACID compliance, referential integrity, triggers, functions, procedures.
- The RDBMS should have all standard relational data types as well as native storage for: JSON, XML, TEXT, Document, Images, Audio, Video, Location Data and Complex Spatial Data.
- The RDBMS should be available to function in Redhat Linux and OpenShift Container Platform.
- RDBMS should be Fully SQL compliant.

## Load Balancing and Security
- The RDBMS should have provision for automatic read load balancing.
- The RDBMS should provide controlled data access down to the row-level so that multiple users with varying access privileges can share the data within the same physical database or table.
- The RDBMS should have an in-built mechanism to prevent from SQL Injection attacks and should not be dependent on application.
- The RDBMS should have obfuscate server side code, protecting proprietary algorithms, data handling procedures, or intellectual property.

## GeoSpatial Capabilities
- The RDBMS should provide for spatial data formats within the database.
- The RDBMS should be OGC compliant for Simple Features specification of SQL.

## Container Platform Integration
- Direct integration with Kubernetes API server for High Availability, without requiring an external tool.
- Self-Healing capability, through:
- a) failover of the primary instance by promoting the most aligned replica.
- b) automated recreation of a replica.
- Planned switchover of the primary instance by promoting a selected replica.
- Scale up/down capabilities.
- Definition of an arbitrary number of instances (minimum 1 - one primary server).

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Features

- Definition of the read-write service, to connect your applications to the only primary server of the cluster
- Definition of the read-only service, to connect your applications to any of the instances for reading workloads
- Declarative management of RDBMS configuration through CRD's
- Declarative management of RDBMS roles, users and groups
- Support for Local Persistent Volumes with PVC templates
- Reuse of Persistent Volumes storage in Pods
- Support for PVC
- Support for Separate volume for transaction log files for replication and crash recovery ensuring data integrity
- Rolling updates for minor versions
- In-place or rolling updates for operator upgrades
- TLS connections and client certificate authentication
- Support for custom TLS certificates (including integration with cert-manager)
- RDBMS deployments across multiple Kubernetes clusters, enabling private, public, hybrid, and multi-cloud architectures
- RDBMS must support connection pooling for database scalability and transparent application connection to one or more database instances
- Support for node affinity via nodeSelector
- Native customizable exporter of user defined metrics for Prometheus through the metrics port (9187)
- Automatically set readOnlyRootFilesystem security context for pods

## Performance

- The RDBMS solution should have capability of examining a database's activity through a native GUI tool and help diagnosing the long running SQL commands and frequently running SQL commands.
- The RDBMS should have High performance tools to do bulk data loading and should have an option of loading data in parallel.
- The RDBMS should have a resource manager for CPU and I/O to manage different workloads based on the priority.
- The RDBMS should have options of different partitioning schemes within the database (for ex. Range, List, Hash etc) to split large volumes of data into separate pieces or partitions, which can be managed independently. The partitioning should enhance the performance, manage huge volumes of data.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## RDBMS Features

### Partitioning
- The RDBMS should provide a rich variety of partitioning schemes to address the business requirement of the application.
- Partitioning should be embedded tightly into the core database engine and supported by many administrative tools.
- From an application perspective, it should be completely transparent which means no or minimal changes should be needed to be made to the application or to the SQL statements in order to use it.

### High Availability
- The RDBMS should provide Active-Active clustering across datacenters.
- Should also have provision for automatic failover between two database instances in Active-Active configuration.
- The RDBMS should have synchronous replication of data feature i.e. a transaction commit should wait at the primary database server/site till it is written on secondary database server/site.
- The RDBMS should have feature of replicating data Asynchronously.

### Backup
- Users should be able to take Complete Database Backup Online and in Parallel.
- The restoration of the Complete Database should also be possible in Parallel.
- The RDBMS solution should have a feature of continuous backup to a S3 compliant object store and full recovery and Point-In-Time recovery from an existing backup in an object store.

### Disaster Recovery
- The RDBMS should have native disaster recovery capability without any third party support using cost effective option of automatically synchronizing the transaction logs to disaster site, which in case of failover should provide the availability of all data.
- The RDBMS should have built-in DR solution to replicate the changes happening in the database across multiple DR Sites with an option to run real-time reports from DR Sites without stopping the recovery mechanism.

### Manageability
- The RDBMS should provide automatic patch and security updates mechanism for the database and associated components such as replication tools, database servers etc.
- The RDBMS should have tools to perform real-time monitoring at different levels such as databases, instances, CPUs, Disk Storages, Memory, Statements in application including dynamic SQL, tables, locks, connection, deadlock, transactions.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- The RDBMS monitoring system should be able to generate alerts when a certain set threshold is crossed and should be able to generate notifications about alerts.
- The RDBMS should provide in-built auditing for allowing database administrators, security administrators, auditors, and operators to track and analyze database activities. These activities should include database access and usage along with data creation, change, or deletion.

## Case studies
- At least two live Case studies of large-scale implementation in the travel/Transport/finance industry in the OLTP environment worldwide.

## In Memory Data Grid (caching)

### Technical Specification for In Memory Data Grid (caching) solution

| Sl. No. | Software Specification                                                                 | Compliance (Yes/No) | Remarks (if any) |
|---------|----------------------------------------------------------------------------------------|---------------------|------------------|
| 1       | The Caching software to be on open standards-based platform and participant in the JSR 107 and well defined roadmap for JSR 107 compliance |                     |                  |
|         | Minimize Amount of Refactoring                                                         |                     |                  |
|         | The cache product should integrate with the following application servers and frameworks: |                     |                  |
|         | a. Spring Boot                                                                         |                     |                  |
|         | c. Hibernate                                                                           |                     |                  |
| 2       | d. JPA (Java Persistence API) - with async back store scenario                        |                     |                  |
|         | e. webLogic Application Server                                                          |                     |                  |
|         | f. JBoss Application Server                                                             |                     |                  |
|         | g. Web Sphere Application Server (including the Virtual Enterprise edition)            |                     |                  |
| 3       | Product should be compatible to run over Kubernetes based container setup for server and client instances. |                     |                  |
| 4       | Product shall be able to support application data models without requiring any changes given the data meets Java serialization requirements. |                     |                  |
| 5       | Product shall enable a continuous integration development environment.                  |                     |                  |
| 6       | Product should minimize vendor lock-in.                                                |                     |                  |

----

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Distributed Data Structures and Utilities

### The product should have the following distributed data structures and concurrency utilities:
a) **Map** - is the distributed implementation of `java.util.Map`
b) **Queue** - is the distributed implementation of `java.util.concurrent.BlockingQueue`
c) **Ringbuffer** - is implemented for reliable circular queue system.
d) **Set** - is the distributed and concurrent implementation of `java.util.Set`
e) **List** - similar to above set the only difference is that it allows duplicate elements and preserves their order
f) **Multimap** - is a distributed data structure where you can store multiple values for a single key
g) **Replicated Map** - it does not spread data to different cluster members. Instead, it replicates the data to all members
h) **Distributed Lock** - is the distributed implementation of `java.util.concurrent.locks.Lock`
i) **Distributed Semaphore** - is the distributed implementation of `java.util.concurrent.Semaphore`
j) **Distributed Atomic Long** - is the distributed implementation of `java.util.concurrent.atomic.AtomicLong`

## Performance at Steady State
- Product should be able to deliver consistent throughput and latency under peak load scenario and circumvent execution environment specific issues like GC.

## Scalability
- Product must allow an unlimited number of nodes to scale horizontally in support of an individual cache.
- Product must have the ability to scale vertically and perform equally as well with a single node installation, if provided sufficient CPU, memory, and I/O as a multi-node deployment.
- Product should be able to scale horizontally and handle more application throughput and larger data size by runtime augmentation of additional computers/nodes.
- Product should have the ability to maximize the available RAM utilization and remain agnostic to Java GC issues.

## Performance during Warm-up
- The product should perform well as the cache is warming up.

## Cache Startup Time
- [Details not provided in the text]

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Product Startup and Data Affinity
- The product shall startup quickly, so that clients are able to use it very soon after it is launched.
- Product shall have the ability to locate data as close to where it is needed as possible, and in an efficient format for where it is needed.

## Support for Large Data Sets
- The product shall support data affinity when total cached data size is very large.
- The product should support in memory access time of microsecond latencies for a very large distributed data set without impacting the JVM GC behavior.
- The product shall guarantee the cluster wide consistency of data that is having affinity with application nodes. It should do so with no/minimal impact on performance.

## Cache Synchronization
- The product in process cache should always be in sync with latest updates in cluster.

## Component Failure and Recovery
- Product shall have the capability to automatically detect and recover from failure. Caching infrastructure should allow tunable SLAs against different kind of infrastructure failure.
- Product shall have the capability to dynamically add new servers/cache instances to the system and rebalance data across the cache instances while the system is running.
- While the system is recovering from a modification to its configuration, performance as seen by cache clients should be minimally affected for a minimal duration.
- Addition of new cache nodes to a running cache environment should also minimally impact cache clients.
- The product shall allow clients to be dynamically switched to an alternate server, if the server they are communicating with has a high processing load or becomes unavailable.
- Product must handle split brain issues (where a network or switch break causes the system to split into two “networks” that temporarily cannot communicate with each other but can communicate with some subset of client applications).

## Data Distribution and Consistency
- The product shall efficiently distribute data across the cache for high performance and robustness.
- The product should be fully JTA standard compliant.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- The product shall support replicating a cache across a LAN/WAN.
- The replication should be highly available and should support network outages or network slowdowns.
- The product should support both Active-Passive and Active-Active multisite.
- The product shall guarantee data safety and availability during unplanned/planned data center shutdown.
- The data stored inside Distributed cache should be able to recover without dependency on any external data source.
- This feature should be configurable for specific caches (use cases like train static data, availability, etc).

## Cache Techniques and Access Methods

- The product shall have the ability to support clustering and caching of web sessions.
- The product shall facilitate uploading of data in bulk to the distributed cache.
- While data is being uploaded, performance of the cache should be minimally affected so clients can use the cache.
- This feature should also include the ability to bulk update or bulk delete cache data.
- The product shall allow “trigger-like” notification for create/update/delete operations.
- Notifications could be sent out to either servers or clients as a cache entry is created, updated, or deleted.
- The product shall allow querying of cached objects using multiple value elements and/or keys and/or metadata simultaneously.
- The product shall support queues and topics for persistence (asynchronous write to backend).
- The product should support asynchronous write to backend persistence store.
- The product shall support multiple API calls simultaneously (multi-threading).
- The product shall support versioning of objects in the cache.
- The product shall support assignment of running embedded code in specific cache nodes or with specific objects in the cache.

## Support for Caching Standard

- The product should participate and conform to JSR 107 caching standards.

## Database / Data source integration

- [Additional details may follow in subsequent sections]

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- The product should be readily integrated with the major ORM frameworks like Hibernate.

- The product should be capable of acting as second level caches in Hibernate.
- Cache Aside
- Read Through
- Write Through
- Write Behind

- The product should have write behinds that will guarantee updates going to the database irrespective of failures.

- The product should not have any dependency on external database management systems.
- The product should support near cache in the client, backed by a distributed cache. Whenever the cache entries in the distributed cache are updated, the near cache in all the clients should also be updated.

## Development IDE
- The product must support the Eclipse IDE (Spring Source Tool Suite in particular).

## Availability of features in the product
- The product should provide all the specifications out of the box/configuration/OEM build custom code to provide the feature.

- The product should support both cloud-based as well as non-cloud (standalone) based deployment.

## Admin, Operations and Maintenance
- The product should provide separation of duties across administrator types using role-based security and authorization features.
- The product shall support:
- Viewing cache activity and metrics. For example, when a node has been added or removed, an administrator should be able to tell when rebalancing is complete.
- Altering cache contents
- Security administration

- The product should be compatible with Application performance monitoring tools. These should not negatively impact the operation of the cache.

- The product should be patched without a major outage to the distributed cache.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- The product shall provide tools capable of troubleshooting problems, provisioning storage, and managing the configuration.
- The tools should have a GUI as well as command line utilities.
- The command line utilities should allow scripts to be written to perform repetitive administration tasks, or tasks that must be applied across many cache nodes and components.
- The product shall expose the monitoring capabilities through standard interfaces so that caching solution can be monitored and managed through customer own monitoring and management tools.
- Monitoring should have minimal impact on the runtime performance of the application.

## Console Overview Panel
- Should display summarized information of cache nodes with the following columns:
- **Node** – The address of the client where the current Cache Manager is running.
- **Caches (Use Cases)** – The number of caches resident on the client.
- **Enabled** – The number of caches that are available to the application. Get operations will return data from an enabled cache or cause the cache to be updated with the missing data. Get operations return null from disabled caches, which are never updated.
- **Statistics** – The number of caches from which the console is gathering statistics. Viewing cache statistics by day, week, month, quarter, and year.

## Cache Statistics Usage Graphs
- **Cache Hit Ratio** – The ratio of cache hits to get attempts. A ratio of 1.00 means that all requested data was obtained from the cache (every put was a hit). A low ratio (closer to 0.00) implies a higher number of misses that result in more faulting of data from outside the cache.
- **Cache Hit/Miss Rate** – The number of cache hits per second (colored) and the number of cache misses per second (colored).

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Cache Update Rate
- The number of updates to Objects in the cache, per second.
- A high number of updates implies a high eviction rate or rapidly changing data.

## Cache Put Rate
- The number of cache puts executed per second.

## Console should display Cache Statistics Table
- **Name** – The name of the cache as it should be configured in the Cache Manager configuration resource.
- **Hit Ratio** – The aggregate ratio of hits to gets.
- **Hits** – The total number of successful data requests.
- **Misses** – The total number of unsuccessful data requests.
- **Puts** – The total number of new (or updated) elements added to the cache.
- **Expired** – The total number of expired cache Objects.
- **Removed** – The total number of evicted cache Objects.
- **In-Memory Size** – The total number of Objects in the cache on the client selected in Select View. This statistic is not available in the cluster-wide view.

## Console should display Cache Statistics Search Graphs
- The search-related historical graphs provide a view into how quickly cache searches are being performed.
- The search-rate graph displays how many searches per second are being executed.

## Console should display Cache Statistics JTA Graphs
- The JTA historical graphs display the transaction commit and rollback rates as well as the current values for those rates.

## Write-Behind Statistics
- **Total number of writes** in the write-behind queue.
- **Maximum number of pending writes**, or the number of Objects that can be stored in the queue while waiting to be processed.

## Console should display Size of Cache
- The cache solution should display the Size of all caches in local as well as server tier.

## Editing Cache Configuration
- The cache solution should provide the following editable configuration properties for each cache:
- **Cache** – The name of the cache as it is configured in the System configuration resource.
- **Time-To-Idle (TTI)** – The maximum number of seconds an Object can exist in the cache without being accessed.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Cache Cluster Run Time Statistics
- **Time-To-Live (TTL)**: The maximum number of seconds an Object can exist in the cache regardless of use.

### Real-Time Performance Monitoring
- Tool allows to spot issues as they develop in the cluster.
- **Client Flush and Fault Rate Graphs**: Client flush and fault rates are a measure of shared data flow between Cache servers and clients. These graphs can reflect trends in the flow of shared objects in a Cache cluster.
- **Cache Miss Rate Graph**: The Cache Miss Rate measures the number of client requests for an object that cannot be met by a server's cache.

## Compression and Monitoring Features
- Product should have the option for selectively applying compression feature while storing the objects in memory and during network transfer.
- In case of using multiple cache instances for storing huge data in cache, Product provides a common/single monitoring console to manage the entire cluster.
- Product has the feature to automatically increase the cache data size of any magnitude without any downtime and manual intervention.
- Product provides the option to control the number of instances for storing data in cache.
- Product provides a feature for multi-value hash maps in which we can put more than one value for the same key.
- Product provides a web-based monitoring console for all the requirements, so that there will be no need to install the same at all monitoring locations.
- Monitoring console of the product should be able to provide the data present (in key-value format) in cache.
- Product should have a proper security mechanism for accessing the cache data.

## Compliance and Support
- Product is compliant with all mentioned technical specifications out of the box without customization.
- The product vendor should have L1-L3 support team/development office in India.

## Performance Requirement
- **Day one performance requirement**.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Performance Requirements
- The solution must fulfill the day one performance:
- Requirement of handling 1.5 million transactions per second
- 70% read operations
- 30% write operations
- Data capacity of 1 terabyte

## Scalability
- Scalability in performance to meet future demands with additional Hardware and Software:
- Capable of accommodating future increases in load up to 3 million transactions per second
- Maintaining a ratio of 70% read operations and 30% write operations
- Supporting a data capacity of 2 terabytes

## Case Studies
- At least two live case studies of large scale implementation in the travel/transport/finance industry in the OLTP environment involving dynamic cache worldwide.
- The OEM to certify that the case studies submitted handle 1 million cache operations per second including get and put.

## Note
- For scalability in performance to meet future demands with additional hardware and software: As per the future demand for 3 million TPS, the additional hardware, software, and subscription will be procured in a separate RFP by CRIS.

## Annexure – V: Format for Submission of Details of Credentials/Documents Furnished Towards Compliance of Qualification Criteria
| S No. | Parameter | Details of Credentials/Documents Furnished | |
|-------|-----------|-------------------------------------------|---|
|       | Description of Credential | No. and Other Details | File name of the corresponding document attached with the bid on ireps |

----

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# Annexure – VI: Checklist for submission of Technical Evaluation

## S. No. Parameter
- Details of credentials/documents furnished
- Documents to be provided
- File name of the corresponding document attached with the bid on ireps

----

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 28. Annexure – VII: Support Office Details in Delhi/NCR and Secunderabad
- Refer Annexure 15 of Standard Bid Document part-1

## 29. Annexure – VIII: OEM Product Deployment Undertaking
- Details of credentials/documents furnished towards undertaking of product deployment

| SNO | Product Name | OEM | Project completion year | Details of product deployed | Customer Name | File name of OEM undertaking attached with the bid on IREPS |
|-----|--------------|-----|------------------------|----------------------------|---------------|----------------------------------------------------------|
| 1   |              |     |                        |                            |               |                                                          |
| 2   |              |     |                        |                            |               |                                                          |
| 3   |              |     |                        |                            |               |                                                          |

## 30. Annexure – IX: Final Acceptance Testing Procedure
### 30.1. Transactional Datastore
- Submission of a detailed installation report clearly indicating the installation of Transactional Datastore, configuration of replication, configuration of servers, operating system parameters, detailed deployment diagram, details of all supplied software installation with key parameters in accordance with the finalized deployment architecture of both the DC and DR cluster.

- These test cases need to be performed on both the DC and DR cluster of transaction datastore:
1. Put data on the datastore for testing.
2. Query data that have been added.
3. Use test application (CRIS to provide) to continuously write and query the datastore.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 30.1. Transactional Datastore Testing
- Pull one instance out of the transactional datastore cluster:
- The test application should continuously write and query the datastore cluster without any failure and no loss of data should be observed.

- Put the above instance back to the cluster:
- The test application should continuously write and query the datastore cluster without any failure and no loss of data should be observed.

- Pull one physical machine out of the transactional datastore cluster:
- The test application should continuously write and query the datastore cluster without any failure and no loss of data should be observed.

- Put the above physical machine back to the cluster:
- The test application should continuously write and query the datastore cluster without any failure and no loss of data should be observed.

- Power off any one machine of transactional datastore cluster:
- The test application should continuously write and query the datastore cluster without any failure and no loss of data should be observed.

## 30.2. Transactional Datastore DR
- These test cases need to be performed in addition to those defined in section 30.1 on DR Site:
- From the above test case check whether data is available in the DR site.
- Showcase how to migrate to DR site.
- Showcase how to switch back to DC site from DR site.
- No loss of data should be there while performing the above test cases.

## 30.3. RDBMS
- Submission of detailed installation report clearly indicating the installation of RDBMS, configuration of replication, configuration of RDBMS containers, details of all supplied software installation with key parameters in accordance with the final deployment architecture of both the DC and DR cluster.

- These test cases need to be performed on both the DC and DR cluster of RDBMS:
- Load data on RDBMS for testing.
- Query the loaded data.
- Check application connectivity to the database using JDBC.
- Use test application (CRIS to provide) to continuously write and query the database.
- Delete one of the RDBMS pod:
- The test application should continuously write and query the RDBMS cluster without any failure and no loss of data should be observed.

- Power off the physical machine where RDBMS pod is running:
- The test application should continuously write and query the RDBMS cluster without any failure and no loss of data should be observed.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## RDBMS DR
These test cases need to be performed in addition to those defined in section 30.3 on the DR Site:

1. From the above test case, check whether data is available in the DR site.
2. Showcase how to migrate to the DR site.
3. Showcase how to switch back to the DC site from the DR site.
4. No loss of data should occur while performing the above test cases.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 30.5. In Memory Data Grid (caching)

The final ATP shall be carried out jointly by CRIS and the bidder for verification of the following:

- Submission of detailed installation report clearly indicating the installation of Caching software and configuration of Caching software containers, Kubernetes parameters, detailed deployment diagram, details of all supplied software installation with key parameters in accordance with the final deployment architecture of both the DC and DR cluster.

1. Technical specifications of Caching software and its supporting components from the SoR will be verified through physical inspection or verification from product brochure or manufacturer certification/document or Certificate/Report from respective regulatory agency or conducting a test as per Annexure IX.
2. Installation and configuration of complete solution as given in scope of work (section 4) and deployment architecture specified in section 3.2.
3. Installation and configuration of products supplied by vendor services as per finalized deployment architecture.
4. Verification of “No Single Point of Failure” in overall solution.
5. Verification of “No Data Loss” in overall solution.
6. Demonstration of functional requirements of Caching software (Annexure III).
7. Evaluation of Technical use cases of Caching software (Annexure XI).
8. Compliance to Security Requirements and submission of report.
9. The above points from 30.5.1 to 30.5.8 should also apply to DR setup too.

## 31. Annexure – X: Test Certificates

### 31.1. Preliminary Test Certificate

**SUB:** Preliminary Test Certificate

**PURCHASE ORDER NO:** _______________                      **Dated:** ____________
**Bidder Name:** _______________

**Name of consignee:** ___________

**Name of site:** _______________

Against the above mentioned purchase order, the items detailed below have been received on ___________.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Item Details

|--------|----------------|------|------|----------------------------------|------------|--------------------------|------|---------|
|        |                |      |      |                                  |            |                          |      |         |

## Certification

It is certified that the above mentioned items confirm the specifications/requirements of the purchase order and all the items required as per purchase order, have been delivered to consignees as per terms and conditions of purchase order.

## Signatures

**Bidder Representative**
Signature:
Name:
Designation:
Date:

**CRIS Representative**
Signature:
Name:
Designation:
Date:

----

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
Page 107 of 124
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 31.2. Final Acceptance Testing Certificate

### SUB: Final Acceptance Test Certificate

- **PURCHASE ORDER NO:** _______________
- **Dated:** ____________

- **Bidder Name:** _______________

- **Name of consignee:** ___________

- **Name of site:** _______________

- **Date of Final Acceptance:** _________________

Against the above mentioned Purchase Order, the items detailed below have been successfully completed the final acceptance testing.

### For each item supplied as per SOR

| S. No. | PO Item No. | Item Name Description | Qty. | Installation Status | Acceptance Testing Status | Performance Tuning Done | Date of Installation |
|--------|-------------|-----------------------|------|---------------------|--------------------------|------------------------|----------------------|
|        |             |                       |      |                     |                          |                        |                      |

It is certified that the above-mentioned items confirm the specifications/requirements of the purchase order and all the items required as per purchase order have been successfully installed, configured, tested, and made operational as per requirements of the purchase order.

The Vendor has successfully demonstrated:

a. Functional requirements (Annexure III).
b. Technical use cases (Annexure XI).
c. Configuration of Backup and restore process as specified in section (section 4.7).
d. DR process (Only for Final acceptance testing of DR Site at Secunderabad)(Section 4.8).

The vendor has submitted a detailed installation report, Acceptance Test, security compliance report, and all relevant documents as specified in the tender.

### Bidder Representative                CRIS Representative
- **Signature:**
- **Name:**
- **Designation:**
- **Date:**

----

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
Page 108 of 124
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 31.3. System Commissioning Certificate

### SYSTEM COMMISSIONING CERTIFICATE

Sub: System commissioning certificate for release of payment of 100% of the cost of software items supplied for SoR Item for First year and 100 % of the Implementation cost as per SoR, S. No. 37).

**PURCHASE ORDER NO:** _______________                             **Dated:** ____________

**Name of site:** CRIS, New Delhi                                         **Name of client:** CRIS/PRS

**Date of Final acceptance:** ________________
**Vendor Name:**________________
**Date of System Commissioning:** _____________________

| For PO - Item No. | Item description | Qty. | System Commissioning Status | Status after 1 month | Remarks |
|--------------------|------------------|------|----------------------------|----------------------|---------|
| Software supplied as per SORS. No. |                  |      |                            |                      |         |

The Vendor has successfully done knowledge transfer session of the implementation of entire solution.

**Bidder Representative**
**Signature:**
**Name:**
**Designation:**
**Date:**

----

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
Page 109 of 124
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Annexure – XI: Technical Use Cases

#### 32.1.1 Technical use case report for YCSB
- The transactional datastore OEM should provide YCSB benchmark reports.
- The YCSB report should be based on the same version of the software being offered in this RFP.

- The benchmark report should be based on the following workload types:
1. Workload A – 50% read and 50% write.
2. Workload B – 80% read and 20% write.
3. Workload C – 90% read and 10% write.

#### 32.1.2 Benchmarking criteria
a. The report should clearly state the hardware and software configuration details used in the YCSB benchmark.
b. The report should provide the YCSB client hardware and runtime configuration details used in the benchmark.
c. The server-side hardware configuration should be based on the server specification mentioned in Annexure – IA.
d. Minimum five physical servers or virtual instances, equivalent to minimum 320 physical cores/640 vCPUs and minimum 5 TB RAM should be used in the YCSB benchmarking.
e. The execution time for all the workloads with client request should be 4 hours.
f. The report should clearly state the start time of each workload (A, B and C) so that it can be correlated with nmon reports of the servers and clients.
g. Data size for all the above workloads should be of 6 TB.
h. The report should provide operations/sec. chart in the following manner.

```
Workload Operation/sec.
6000
5000
Operations/sec
4000
3000
2000
1000
0
Workload A  Workload B  Workload C
Workloads
```

- The report should provide hourly based operations/sec. chart in the following manner.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Operations/sec.
- 14000
- 12000
- 10000
- 8000
- 6000
- 4000
- 2000
- 0

### Time
- 1 hr
- 2 hr
- 3 hr
- 4 hr

- Workload A
- Workload B
- Workload C

## Response Time - Write
- 3.5
- 3
- 2.5
- 2
- 1.5
- 1
- 0.5
- 0

- Workload A
- Workload B
- Workload C

### Metrics
- Average
- 95th Percentile
- 99th Percentile

## Hardware Utilization Report
- The report should provide the hardware utilization report based on nmon csv format (batch mode with 60 seconds frequency). For all the hardware used in the YCSB benchmark (client and server both).

## YCSB Report Requirements
- Minimum 1,50,000 Reads per second and minimum 25,000 Writes per second
- Response time of P99 of 2 milliseconds or less for reads and 3 milliseconds or less for writes operations for 6 TB of unique data in a DC, maintaining a Read/Write ratio of 80% reads to 20% writes (Workload B).

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 32.2 Technical Use cases for In Memory Data Grid (caching)

### 32.2.1 Technical use case
It is planned to carry out the test cases which shall demonstrate the product features and capability and also the Application specific business cases. The details of the test cases planned to be performed under this category are listed in the table below.

| ID | Feature       | Test case                                                                 | Remarks                                                                 |
|----|---------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------|
| 1  | Capability    | Data stored by client on one instance of Spring Boot Application is available to another instance of Application, although the instances are not in application server cluster |                                                                         |
| 2  | Capability    | Ability to store the existing application data structures in cache       |                                                                         |
| 3  | Capability    | Once data brought into local machine, it is served all the request from local machine till the time of update in central cache or TTL/TTI |                                                                         |
| 4  | Capability    | Latest updated data is available on local machines (data updated from any machine is universally available on local machine) |                                                                         |
| 5  | Capability    | Option to dynamically change the cache configuration (modify TTL at run time) |                                                                         |
| 6  | Capability    | Ability to control the size of local cache based on application needs.   |                                                                         |
| 7  | Capability    | Write-behind or other database integration features should be available   |                                                                         |
| 8  | Monitoring    | Real time monitoring of the system (for faults at local machine/size of elements/TPS/client connections/machine Id's/server status etc (complete list shall be shared before carrying out the POC) |                                                                         |
| 9  | Performance   | Performance achieved after Use of cache solution does not breach the Application benchmarking defined by CRIS. | Benchmarking                                                          |
| 10 | Performance   | Application throughput of 35000 (24000 gets/sec, 11000 put/sec) no of requests it can handle simultaneously. | Benchmarking                                                          |
| 11 | Performance   | Increase in Memory usage (size) after implementing the cache solution is not more than 10 to 20%. | Benchmarking                                                          |
| 12 | High Availability – JVM | JVM Stopped - Cache contents still available (All the data elements stored in central cache by application are available) |                                                                         |
| 13 | High Availability | Cache contents are available and application working seamlessly even after stopping one of the nodes of central cache server |                                                                         |
| 14 | High Availability | Entire cluster failure - Cache contents are still available after cluster restart |                                                                         |

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## 32.2.2 Benchmarking Criteria
During performance benchmarking activity, following two types of tests shall be performed.

- **a) Application performance test**
- This shall be performed as per workload profile defined by CRIS.
- The results of this run should match the SLA’s achieved by CRIS during the benchmarking activity of the application.
- The resource utilization on server should not exceed the resource utilization achieved during benchmarking activity.

- **b) Sample application benchmarking for throughput and performance**
- In this, a sample application without any business logic/user interface and which shall have only API calls for accessing the cache to simulate the following cases shall be executed.

```plaintext
Test Case 1: Search of the value with a key from Huge data pool to check response time behaviour of the cache solution.

Test Case 2: To check concurrency of cache product, Multiple Gets or reads can be done.

Test Case 3: To check concurrency of cache product, Multiple Puts or writes can be done.

Test Case 4: If big object is updated at central cache then how the product will send same objects from central cache to local cache.
```

## 33. Annexure XII: Certificate from Bidder for Compliance to GoI Order for Countries sharing Land Border with India
Refer Annexure 7 of Standard Bid Document Part-I

## 34. Annexure-XIII: NON-DISCLOSURE AGREEMENT (NDA)
Refer Annexure 14 of Standard Bid Document Part-I

## 35. Annexure-XIV: Data layer Solution (Software component) – Breakup Detail Format
Please refer Annexure – II: Schedule of Requirements for the S-1, S-2 and S-3 and provide the following information against each of the product.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Software Components

### S. No. 1
- **Software Component Name**:
- **Complied Tech Spec No. of S-1**:
- **UoM**:
- **License Type (Subscription)**:
- **Qty**:
- **Product Offered (Model/make)**:
- **Remarks**:

**Total**:

### S. No. 2
- **Software Component Name**:
- **Complied Tech Spec No. of S-2**:
- **UoM**:
- **License Type (Subscription)**:
- **Qty**:
- **Product Offered (Model/make)**:
- **Remarks**:

**Total**:

### S. No. 3
- **Software Component Name**:
- **Complied Tech Spec No. of S-3**:
- **UoM**:
- **License Type (Subscription)**:
- **Qty**:
- **Product Offered (Model/make)**:
- **Remarks**:

**Total**:

----

**Note**: For Transactional data store, the details of all the components including the Operating system of the solution should be provided in the table above.

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Annexure-XV: Format for Bidder to submit solution for each technical use case solution

- **TUC No.**
- **Use Case**
- **Component(s) Used**
- S. No.
- Component
- Product Offered/Used
- OEM Name (Model/Make/Version No.)

## Detail Design

----

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
Page 115 of 124
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Annexure-XVI: Format for OEM compliance certificate for technical use case solution

To be provided by OEM on their letter head

| TUC No. | Use Case Name | Component (Model/Make/Version No.) | OEM Compliance and certification of usage of their product to implement the solution |
|---------|---------------|-------------------------------------|--------------------------------------------------------------------------------------|
|         |               |                                     |                                                                                      |

----

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
Page 116 of 124
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Annexure-XVII: Declaration of inclusion of OEM Services by the Bidder

**Declaration Letter, On Company letterhead**
Dated : __________

To,
GM/PRS
CRIS, Chanakyapuri,
New Delhi – 110021.

**Tender Reference:** _________________________

Dear Sir/Madam,

We M/s _________________ declare that we have included the services of the OEMs as per the table given below:

| Sr. No. | OEM | RFP clause Number |
|---------|-----|-------------------|
| 1.      |     |                   |
| 2.      |     |                   |
| 3.      |     |                   |

We ensure that we have included all the costs w.r.t to products and their respective services as per the conditions mentioned in the tender.

Yours faithfully,

(Signature, Name, designation, Contact information)

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

already deployed in CRIS PRS Primary DC, Chanakyapuri, New Delhi.

|--------|------------------|--------------|
| 2      | NMS              | MicroFocus NMS (NNMi10, OMi, Network Automation version 10, Site Scope version 11) |
| 3      | SIEM             | McAfee ESM 5600, ERC 3450 |
| 4      | VA Tool          | McAfee MVM-3200 |
| 5      | IAM/PIAM         | MicroFocus NET IQ |

| Component                                              | Minimum OEM Man-Days |
|-------------------------------------------------------|-----------------------|
| RDBMS                                                 | 10                    |
| In Memory Data Grid (caching) Solution                | 30                    |

## Annexure XXI: OEM's Authorisation to Bidder and Undertaking for Backend Support

### Centre for Railway Information Systems

#### Annexure 8: OEM's Authorisation to Bidder and Undertaking for Backend Support

(To be submitted on the OEM's letterhead along with the bid)

**Date:** // - - - - - - -

To
Managing Director,
CRIS, Chanakyapuri,
New Delhi - 110021.

Ref: Tender No...............................

For•........................................................................................................................Name of Work.........................................

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

Sir/Madam,

We, (Name of OEM), having our registered office at [Address of OEM], are an established and reputed manufacturer of below tabled components having factory(s) at [Address of OEM Factory] do hereby declare/undertake as under:

1. We hereby authorize (Name of Bidder)*, having registered office at [Address of Bidder], to bid, negotiate and conclude the Contract on our behalf with CRIS, for the tender under reference for the items listed below.

(*In case OEM is participating in this tender as a bidder, OEM shall fill "self" in place of bidder's name for products that are manufactured by them)

2. We hereby confirm that the software and tools provided with the offered goods are fully licensed and will be supported for the entire duration of the Contract.

3. We further commit to providing backend support including software updates, upgrades and ensure availability of spares, for the entire contract period (including Warranty/AMC period).

Below is the list of Components, for which this authorization/undertaking is being issued: #
```
Component                                 Make                Model

1.

2.

3.
```

Important: The specific make/model of the offered products should be mentioned. Expressions like 'to be decided', 'standard make', 'reputed brand', etc. shall not be accepted.

4. We shall be providing our service support to (Name of Bidder) from all our service centres located across India. We assure you that, in the event, (Name of Bidder) is not able to fulfil its obligations as the service provider for our products, we will continue to provide OEM warranty / ATS services through an alternate suitable arrangement.

5. We shall ensure that the supplied components do not suffer end of life or end of support during the validity of the contract (including Warranty / AMC period). In case the same cannot be ensured, we shall ensure performance of all contractual obligations, through alternate means (with prior approval of CRIS), for the entire contract period (including Warranty/AMC period).

Note: OEM(s) are required to provide Power of Attorney / certified Board Resolution, confirming the authority of their authorised signatory to act on behalf of their firm. It shall be the responsibility of the Bidder to verify these details/documents before submission of their bids.

Declaration by the signatory:                           119

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)                                                           Page 119 of 124
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

I hereby declare that I am duly authorised to make this representation on behalf of my organisation.

Yours faithfully,

[Name of the OEM's authorized Signatory]
[Designation of the OEM's authorized Signatory]
[Name of the OEM]

## 42. Annexure – XXII: Self Certification by Bidder for Make in India

Refer Annexure 6 of Standard Bid Document Part-I

## 43. Annexure-XXIII: Installation and configuration – Breakup Detail Format

```
S. No.    Category (Bidder/OEM Professional Service)    UoM    Company Name    Qty    Remarks
Total
```

## 44. Annexure XXIV: Past Performance Details of Bidder

Past performance details of the bidder to be submitted along with the offer on the letter head of Statutory Auditor or Chartered Accountant of the bidder.

Date: _ _/_ _/_ _ _ _
To
Managing Director,
CRIS, Chanakyapuri,
New Delhi – 110021.
Ref: Tender No. …………………….
For : …………………………………………………………
Name of Work…………………………………………………

Sir/Madam,
After conducting a thorough examination of the project experience details of [Name of Bidder] having their registered office at [Address of Bidder], it is hereby certified that [Name of Bidder] has successfully completed the following Contracts / Purchase Orders

1. Past Performance Details - I                         120

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)
Page 120 of 124
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

- Contract Issuing Authority – Name – Type *
- Project Name
- Role of Bidder in the Project **
- %age share of bidder in the above contract
- Total Value of the Contract (INR)
- Total Quantity ordered
- Quantity Supplied / commissioned during the relevant period
- Current Status of the Contract
- Copy of Purchase Order Attached (Yes/ No)
- Copy of Completion Certificate (Yes / No)

## 2. Past Performance Details - II

- Contract Issuing Authority – Name – Type *
- Project Name
- Role of Bidder in the Project **
- %age share of bidder in the above contract
- Total Value of the Contract (INR)
- Total Quantity ordered
- Quantity supplied / commissioned during the relevant period
- Current Status of the Contract
- Copy of Purchase Order Attached (Yes/ No)
- Copy of Completion Certificate Attached (Yes / No)

(More blocks may be added for additional project experience details, if needed).

## Important Notes:

1. *Contract Issuing Authority Type shall be one of the following:
- Type 1) Any entity (Department / Organization / Autonomous body / PSU/ Local Body/ Authority etc.) wholly or partially owned by State / Central Government
- Type 2) A Private sector organization which is:
- i. Listed in the National Stock Exchange (NSE) or Bombay Stock Exchange (BSE) in India,

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

## Important
- Only those Contracts / Purchase Orders shall be accepted as Past experience wherein the contracts / purchase orders have been placed on the bidder directly by an entity belonging to one of the above types.

## Role of the Bidder
- The role of the bidder in the project shall be selected from one of the following options:
- Sole Bidder

## Relevant Period
- Relevant Period shall be as mentioned in the tender document.
- In case any contract / purchase order is a composite contract (i.e. it contains items other than the ones defined in the qualification criteria as similar work), the quantity supplied / commissioned and the value of the same shall also be indicated separately.

----

## Declaration by the Signatory
- I hereby certify that the past performance details provided above have been verified and are accurate.

- Name:
- CA Registration Number:
- UDIN:
- Date:

## Annexure XXV: Declaration of Non-Blacklisting for OEM
- To be submitted along with the bid separately by all OEMs of Key Components on their Letterheads

### Date: _ _/_ _/_ _ _ _
To
Managing Director,                                      122

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409)                                                           Page 122 of 124
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

CRIS, Chanakyapuri,
New Delhi 110021.

Ref: Tender No. …………………….

## Name of Work/Tender Title
………………………………………………………

Sir/Madam,

In response to the above mentioned tender, I/We as an authorised signatory of [Name of the OEM] having our registered office at [Address of the OEM], hereby declare that I/We is / are not blacklisted or debarred by CRIS, or Ministry of Railways or any other Ministry / Department of the Govt. of India from participation in tenders, on the date of submission of bids, either in individual capacity, or as HUF, or as a member of the partnership firm / LLP/ Joint Venture / Society / Consortium / Trust etc.

If this declaration/undertaking is found to be incorrect, CRIS/IR shall have the right to take legal/administrative action against us, including but not limited to blacklisting/debarment/ recovery of pecuniary losses, or any other recourse available under the Law.

## Declaration by the signatory:
I hereby declare that I am duly authorised to make this representation on behalf of my organisation.

```

[Name of the authorized Signatory]

[Designation of the authorized Signatory]

[Name of the OEM]
```

## Annexure XXVI: Declaration of Non-Blacklisting by Bidder
(To be submitted along with the bid on minimum INR. 100 stamp paper, duly notarized)

This declaration is to be signed by any / all persons / entities indicated below as per the nature of the bidding entity:
- Authorized signatory of Company / Proprietor of Proprietorship firm / Karta of HUF/ All partners of Partnership firms and LLP / All members of a JV/Consortium

Date: _ _/_ _/_ _ _ _

To
Managing Director,
CRIS, Chanakyapuri,
New Delhi 110021.

Ref: Tender No. …………………….
Name of Work/Tender Title …………………………………………………

Sir/Madam,

# TENDER FOR PROCUREMENT OF DATA LAYER SOLUTION FOR NEXT GENERATION PASSENGER RESERVATION SYSTEM (PRS) OF INDIAN RAILWAYS

In response to the above mentioned tender, I/We [Name of Bidder] having my/our registered office at…[Address of Bidder]…., hereby declare that I/We is/are not blacklisted or debarred by CRIS, or Ministry of Railways or any other Ministry / Department of the Govt. of India from participation in tenders/contracts as on the date of submission of bid either in individual capacity, or as HUF, or as a member of the partnership firm / LLP/ Joint Venture / Society / Consortium / Trust etc.

I/We also certify that none of our OEMs for this tender are blacklisted or debarred by CRIS, or Ministry of Railways or any other Ministry / Department of the Govt. of India from participation in tenders/contracts as on the date of submission of bid either in individual capacity, or as HUF, or as a member of the partnership firm / LLP/ Joint Venture / Society / Consortium / Trust etc.

I/ We understand and accept that If this declaration is found to be incorrect then without prejudice to any other action that may be taken by the Purchaser, my/ our EMD/ Security Deposit/ BG may be forfeited in full, my/our offer against the tender may be ignored, and the tender if any to the extent accepted may be cancelled.

## Declaration by the signatory:
I hereby declare that I am duly authorised to make this representation on behalf of my organisation.

```

[Name of the authorized Signatory]

[Designation of the authorized Signatory]

[Name of the Bidder]
```

File No. CRIS/HQ/PRJT/200/2023-PRS (Computer No. 1409) Page 124 of 124
Generated from eOffice by Ranjeet Kumar, ASST MGR/PURC/RK, ASST MGR/PURC/3, HQ Chankyapuri on 21/06/2025 10:40 pm