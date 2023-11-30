import sys
from selenium import webdriver
import time
import json
from datetime import datetime

# Main Module Contains all the actual code for data Pushing and retrieval Functions
import main

try:
    driver = webdriver.Chrome()

    # Connects To Polkadtot JS for Data Entry
    driver.get('https://polkadot.js.org/apps/?rpc=ws%3A%2F%2F127.0.0.1%3A9944#/extrinsics')
    driver.maximize_window()
    # time.sleep(5)

    # datadict = dict()
    # datadict['0x_devid_0000000001_t_11694546301'] = '0x0000000000000000000000000000001'
    # datadict['0x_devid_0000000001_t_11694546302'] = '0x0000000000000000000000000000011'
    # datadict['0x_devid_0000000001_t_11694546303'] = '0x0000000000000000000000000000111'

    # main.initPush(driver)

    # for key,val in datadict.items():
    #     main.dataPush(driver,key,val)



    file_path = "C:/Users/ram/Documents/drx-auto/out.json"
    with open(file_path, 'r') as file:
        data = json.load(file)

    main.initPush(driver)
    for file in data.values():
        
        timestamp = file["timestamp"]
        CID = file["CID"]

        unix_timestamp = int(datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').timestamp())
        ut = str(unix_timestamp).zfill(16)[:16]
        cid = CID[:16].ljust(16, '0')

        if ut and cid :
            main.dataPush(driver, ut, cid )
        else:
            print(f"Skipping data for {file} as timestamp or CID is missing.")


    # Connects To Polkadtot JS for Data Retrieval
    driver.get('https://polkadot.js.org/apps/?rpc=ws%3A%2F%2F127.0.0.1%3A9944#/chainstate')
    time.sleep(5)

    for file in data.values():
        unix_timestamp = int(datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').timestamp())
        ut = str(unix_timestamp).zfill(16)[:16]
        
        retreived = main.retrieveData(driver,ut)
        print(ut,' :' , retreived)


    print('Data Storing & Retrieval Sucessfull')

except Exception as exceptionobj:
    print("Exception Occured , Info of Exception: ")
    traceback = sys.exc_info()
    print("At Line No:- ",traceback[2].tb_lineno)
    print("Reason: ", traceback[0])
    choice = input("Press 1 To know more , else press 0 to exit")
    if choice:
        print("StackTrace: \n", exceptionobj)

finally:
    print("Exiting Program...")