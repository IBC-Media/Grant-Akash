import sys
from selenium import webdriver
import time

# seleniumHelper Module Contains all the actual code for data Pushing and retrieval Functions
import seleniumHelper

def pushData(filename: str, cid: str):
    try:
        driver = webdriver.Chrome()

        # Connects To Polkadtot JS for Data Entry
        driver.get('https://polkadot.js.org/apps/?rpc=ws%3A%2F%2F127.0.0.1%3A9944#/extrinsics')
        driver.maximize_window()
        time.sleep(3)

        # Initiates the data pushing by account configuration
        seleniumHelper.initPush(driver)

        # Pushes File and Cid used for encryption
        seleniumHelper.dataPush(driver,filename,cid)

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
