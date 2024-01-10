# Data RelayX 
We Team Aakash, built the prototype of the product Data RelayX to provide Resilient Decentralized Data communications & Data Storage in swarm troops. Aiming to enhance the security & resiliency of most sensitive & confidential UAV data. We aim to solve the most unique challenges faced by swarm troops in handling the most confidential Unmanned Aerial Vehicle (UAV) data.

## Low Level Design
![DataRelayX](https://github.com/Ram-lankada/IBC-Project-BlockChain/assets/91232198/6f74a8c9-2547-498e-bc02-306c2ad9224b)

## Prototype Low Level Design
![IDEA_1 (1) vpd](https://github.com/Ram-lankada/IBC-Project-BlockChain/assets/91232198/b322d7b9-6e27-4e8f-ac2f-97cf0bdef7d7)

## User Interface 
![about](https://github.com/IBC-Media/Grant-Akash/assets/91232198/67fa0247-b182-4110-ba3c-a0ba25f879fb)
### Image push interface
![image](https://github.com/IBC-Media/Grant-Akash/assets/91232198/be62aed2-91a6-4db1-9b0d-a45fd3cc9346)

## Video Demonstration 
- video link : https://youtu.be/Ax-Jtip6ewQ
- more brief explanation : https://youtu.be/PQDiutClegI

## Technology Stack 
### Frontend Stack 
- HTML
- CSS
- JavaScript
- React ( Later ) 

### Backend Stack
- Polkadot's Substrate node template
- My SQL Database
- IPFS
- Data serialization algorithms
- Selenium
### Cloud Services
- AWS Lambda Serverless application models
- Amazon Keyspaces apache Cassandra

## Prerequisites:
OS: Ubuntu (>ver 20) in WSL2.
-  Applications: (All In WSL2)
1. google-chrome and it's web driver
2. python3 and Selenium
3. git
4. rustc and cargo ( for rust and cargo configuration follow : 'https://docs.substrate.io/install/windows/' )

## How to run 

1. First Install WSL then install rustc and cargo in wsl  follow : 'https://docs.substrate.io/install/linux/' then in wsl Clone the repo using
```
git clone https://github.com/IBC-Media/Grant-Akash.git
```
And run the chain using : 
```
cd Grant-Akash
```
```
cargo update
```
```
cargo build --release
```
```
./target/release/node-template --dev
```
Interact with the Blockchain :
```
https://polkadot.js.org/apps/?rpc=ws%3A%2F%2F127.0.0.1%3A9944
```
2. In Windows Install XAMPP server & paste the `blob1` in the below path :
```
C:\xampp\htdocs
```
3. Run XAMPP server & start `Apache` & `My SQL` services
4. Create a Database named `test_blob1` & the table named `table1` in phpMyAdmin
5. Run the application to encrypt, store & push the Drone generated images to substrate's DLT
```
localhost/blob1/index.php
```
6. An automated selenium script will push the `Time stamp` & `CID` into the substrate's DLT by accessing polkadotjs extrinsics
7. You can also run the selenium script manually to push & retrieve the data
```
cd drx
python test.py
```

This Contains a Custom Pallet named telemetryPallet that has 2 important functions: </br>
Data Pushing: Store A Key-Value Pair onto Blockchain.</br>
Data Retrieval: Retrieve value based on given key.

## References 
This is the code for running a local Blockchain using Polkadot Substrate Framework.
The code has been cloned from :- "https://github.com/substrate-developer-hub/substrate-node-template" and all the credit goes to the respective owners.
We as a team modified the code to integrate it to our Project Data-Relay-X.
