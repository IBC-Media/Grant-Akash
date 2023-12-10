from selenium import webdriver
from selenium.webdriver.common.by import By

import time

def initPush(driver):
    time.sleep(3)

    buttonmenu = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/main/div/div[1]/div[2]/div')
    buttonmenu.click()
    time.sleep(2)
    accname = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/main/div/div[1]/div[2]/div/div[2]/div[2]')
    accname.click()

    time.sleep(2)
    pname = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/main/div/div[2]/div[1]/div/div/div/div[1]/div/i')
    pname.click()

    time.sleep(2)
    tpallet = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/main/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div[6]')
    tpallet.click()

def dataPush(driver,key: str, val: str):
    keyinput = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/main/div/div[2]/div[2]/div/div[1]/div/div/div/div/input')
    keyinput.clear()
    time.sleep(3)
    keyinput.send_keys(key)

    valinput = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/main/div/div[2]/div[2]/div/div[2]/div/div/div/div/input')
    valinput.clear()
    time.sleep(3)
    valinput.send_keys(val)
    time.sleep(2)

    submittxn  = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/main/div/div[4]/button[2]')
    submittxn.click()
    time.sleep(2)
    
    approvebtn = driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[3]/div/button')
    approvebtn.click()

    time.sleep(3)

def dataRetrieve(driver,key: str)  -> str:
    pname = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/main/section/div[1]/div[1]/div/div/div/div[1]/div/i')
    pname.click()
    time.sleep(2)

    tpallet = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/main/section/div[1]/div[1]/div/div/div/div[1]/div/div[2]/div[8]')
    tpallet.click()
    time.sleep(2)

    keyinput = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/main/section/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div/input')
    keyinput.clear()
    time.sleep(3)
    keyinput.send_keys(key)
    time.sleep(2)

    send = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/main/section/div[2]/button')
    send.click()
    time.sleep(4)

    obtval = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/main/section[2]/div/div[1]/div/div/div/pre/div')
    result = obtval.text
    time.sleep(2)

    close = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/main/section[2]/div[1]/div[2]/button')
    close.click()

    return result