# Introduction
**RESILIENT DECENTRALISED COMMUNICATION & DATA STORAGE IN SWARM TROOPS**
UAVs and drone swarms play most crucial role in Defence operations like reconnaissance, spying, critical information sensing, Attack & rescue operations. Out of which the data that they sense acts as linchpin. The sensed data is not for a one time use, it will also be preserved by the defence forces for further utilizations in their operations. Therefore it is very much important to gather & store the sensed data in a very secure way. And the below architecture helps you understand how can achieve this using blockchain technology. 

# Business Solutioning overview
- Indian defence forces do use UAVs, drones & swarm drones for several critical operations like spying, reconnaissance, Attack & rescue operations. 
- When swarm troops are deployed for any of spying, reconnaissance or attack operations, they mutually co-ordinate with each other via p2p communications (i.e. data transactions) 
- Therefore the data that they gather & communicate is that critically important too. 
- Storing these data transactions(i.e. Ledger data) & sensed data(i.e. Data to be stored in file coin like architectures) in a Centralized database is insecure. 
- Therefore this project aims to gather the data from swarm troops using Oracles to ensure data integrity & store the p2p troops communication(i.e. data txns) in to the DLT & stored the troops sensed data into file coin like architectures
![de-da](https://user-images.githubusercontent.com/91232198/236419934-f59984a2-6605-43f9-8cb1-8c3118f59f66.png)

## User Journey
The user journey for this project involves the Indian defence forces using unmanned aerial vehicles (UAVs), drones, and swarm drones for critical operations. The swarm troops are deployed for spying, reconnaissance, attack, and rescue operations, and they communicate with each other via P2P communication. The data they gather needs to be stored securely. Therefore, they’ll use this solution architecture to gather data from the swarm troops using oracles to ensure data integrity and store the data on a DLT and file coin-like architectures.

## Business Application Components
- Distributed ledger technology( DLT ) 
- Decentralized storage architecture like filecoin, ipfs, arweave
- A basic UI for the defence users

## Users Authentication
- As this project involves sensitive and critical information, user authentication is an essential component. The Indian defence forces will have to authenticate their personnel and ensure that only authorized personnel can access the data gathered by the swarm troops. 
- This can be achieved through various authentication mechanisms, such as user ID and password, biometric authentication, or two-factor authentication. The authentication process will ensure that the data remains secure and confidential, and only authorized personnel can access it.

# Solution Architecture 
## Part 1 : Web 2.0 Components : 
- Database: A database is required to store the P2P communication (data transactions) between the swarm troops. A centralized database is insecure, so a distributed database such as Apache Cassandra or MongoDB can be used instead. These databases provide high availability, scalability, and fault tolerance, which are important for critical operations.
- Cloud: The solution can be deployed on a cloud infrastructure such as Amazon Web Services (AWS), Microsoft Azure, or Google Cloud Platform (GCP). Cloud infrastructure provides flexibility, scalability, and security benefits.
- Load Balancer: A load balancer is needed to distribute the incoming traffic across multiple servers to improve performance and ensure high availability. Load balancers such as NGINX, HAProxy, or Amazon Elastic Load Balancer can be used.

## Part 2 : Web 3.0 Components
- Command-line wallets: These wallets can be controlled through the command line interface (CLI), making them suitable for use in machines like drones  that do not have a graphical user interface (GUI). Command-line wallets can be designed using frameworks like Geth, Parity, or Nethermind.
- Decentralized Storage: Swarm is a decentralized storage platform which is a DLT based decentralized storage network which can capture both the ledger data & sensed data  in to the same database. Swarm provides high scalability, privacy, and security benefits.
- Consensus: Proof-of-Authority(PoA) or Proof-of-Stake(PoS) could be a well fit for this architecture. However, we’re researching more on the most compatible for this solution. As it involves the defence forces in validation processes.We will use Aura of substrate if it’s a well fit.

# Database Design and Decentralised Storage
## Need of Decentralized storage : 
- Immutable and secure storage: Since the data being stored is critical and sensitive, it needs to be stored in an immutable and secure manner to prevent any unauthorized tampering or access.
- High availability: The data needs to be available at all times for real-time decision making, which requires a high availability storage solution.
- Scalability: With large amounts of data being generated by the swarm drones, the storage solution needs to be scalable to accommodate the increasing amount of data.
Please see the database design here : https://www.notion.so/RESILIENT-DECENTRALISED-COMMUNICATION-DATA-STORAGE-IN-SWARM-TROOPS-RELATIONAL-DATA-BASE-DESIGN-d01d66bf9a5f4b1a9ffde2b250e15b5a

# Pallets needed 
## Substrate pallets
- Balances: This pallet can be used to manage token balances. We can be customized to fit our needs.
- Identity: This pallet can be used to manage identity on the blockchain. It can be used to verify the identity of swarm UAVs and their operators.
- Timestamp: This pallet can be used to manage the timestamp of blocks on your blockchain. This can be useful for tracking the time of drone operations and transactions.
- Transaction Payment: This pallet can be used to manage transaction fees and payments for the blockchain. 
- Grandpa: This pallet can be used to manage the finality of blocks on the blockchain.  

## Custom pallets 
- Drone: This pallet could be used to manage the identity and behavior of swarm UAVs on the blockchain. It could include fields for the drone's ID, location, status, and other relevant information.
- Sensor Data: This pallet could be used to store and manage sensor data from the swarm UAVs. It could include fields for the type of sensor, the data itself, and the time it was recorded.
- Mission: This pallet could be used to manage the details of each mission carried out by the swarm UAVs. It could include fields for the mission's ID, location, objectives, and status.
- Authorization: This pallet could be used to manage the authorization of swarm UAVs to participate in the network. It could include fields for the drone's public key, - authorization status, and other relevant information.

## Frontend stack
- HTML
- CSS
- JAVASCRIPT
- REACT.JS

## Backend Technology stack
- Apache Cassandra or MongoDB
- Polkadot JS API
- Substrate API Sidecar
- Substrate RPC Client

# Building milestones
![miles](https://user-images.githubusercontent.com/91232198/236421906-a16a1908-3668-4721-bba0-308a920353e5.png)

# Testing
![testing](https://user-images.githubusercontent.com/91232198/236421943-858ec5a3-818a-42ee-b9d0-9a6db557029c.png)

# MVP Stage - 2 Month plan
![MVP](https://github.com/IBC-Media/Team-Akash/assets/91232198/978c04c2-4b16-475f-aed7-b98d18315d19)

