from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

from tkinter.filedialog import askopenfilename
from time import sleep
import base64
import os, sys
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from getdriver import *
#import simultane

##This section controls the twitter browser and can post a message to the timline
def inittwitter():
    driver = getdriver()
    driver.get('https://twitter.com/')
    
    #the login btn used to be at xpath as of 12_2_2021:
    #/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div/span/span

    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/div[5]/a/div")))
    #sleep(5)
    #click on the login button
    button = driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/div[5]/a/div")
    button.click()
    return driver

"""
def getcredentialstwitter():
    a = input("what is you email/phone for twitter?\n")
    b = input("what is your password for twitter?\n")
    return a,b
"""

def login(driver,emailtwitter,passwordtwitter):
    #sleep(3)
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]")))
    
    driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]").click()
    sleep(0.2)
    atwitter = driver.switch_to.active_element
    atwitter.send_keys(emailtwitter)
    btn = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div/span')
    btn.click()

        
    btwitter = driver.switch_to.active_element
    btwitter.send_keys(passwordtwitter)
    
    ctwitter = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div")
    ctwitter.click()

def logintwitter(emailtwitter,passwordtwitter,atwitter,btwitter,ctwitter,driver):
    btwitter.send_keys(passwordtwitter)
    ctwitter.click()
    sleep(3)
    url = driver.current_url
    #print(url)
    if url.find("email_disabled") != -1:
        atwitter,btwitter,ctwitter = getfieldtwitter(driver)
        print("contingency")
        username = input("twitter failed I am gonna need your @username please!")
        #print("I have the username now I should be able to send it")
        atwitter.send_keys(username)
        #print("username sent")
        btwitter.send_keys(passwordtwitter)
        ctwitter.click()

def postingtwitter(driver):
    WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span")))
    button = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span')       
    #button = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span')
    button.click()
def tweet(driver,msg):
    sleep(2)
    post_box=driver.switch_to.active_element
    post_box.send_keys(msg)

def posttweet(driver):
    WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span")))                                                                                                                                                                                                                        
    tweetbutton = drivertwitter.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]/div/span/span')
    #tweetbutton = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]/div/span/span')                       
    tweetbutton.click()


    
#This is a new piece it links alldef ex_tw():
def ex_tw(emailtwitter, passwordtwitter, msg):
    try:
        driver = inittwitter()
    except:
        try:
            print('fail twitter init waiting 5 sec')
            sleep(5)
            driver = inittwitter()
        except:
            print('second fail executed with success')                            
            pass
    try:
        login(driver, emailtwitter, passwordtwitter)
        #[atwitter,btwitter,ctwitter] = getfieldtwitter(driver)
    except:
        try:
            print('fail twitter getfield waiting 5 sec')
            sleep(5)
            [atwitter,btwitter,ctwitter] = getfieldtwitter(driver)
        except:
            print('second fail executed with success')                            
            pass
    try:
        #print("logging in")
        pass
        #logintwitter(emailtwitter,passwordtwitter,atwitter,btwitter,ctwitter,driver)
    except:
        try:
            print('fail twitter login waiting 5 sec')
            sleep(5)
            logintwitter(emailtwitter,passwordtwitter,atwitter,btwitter,ctwitter,driver)
        except:
            print('second fail executed with success')                            
            pass
    try:
        postingtwitter(driver)
    except:
        try:
            print("fail twitter postbox opening waiting 5 sec")
            sleep(5)
            postingtwitter(driver)
        except:
            print('second fail executed with success')                            
            pass
    try:
        tweet(driver,msg)
    except:
        try:
            print('fail twitter msg waiting 5 sec')
            sleep(5)
            tweet(driver,msg)
        except:
            print('second fail executed with success')                            
            pass
    try:
        print('trying to post tweet')
        posttweet(driver)
    except:
        try:
            print('fail twitter msgposting waiting 5 sec')
            sleep(5)
            posttweet(driver)
        except:
            print('second fail executed with success')                            
            pass
