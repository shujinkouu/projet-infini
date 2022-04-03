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
#This is outdated was a terminal tool to post on from tkinter.filedialog import askopenfilename
import keyboard
from keyboard import press


from selenium import webdriver
from time import sleep
import keyboard
from getdriver import getdriver


##This section controls the gab browser and can post a message to the timline
def initgab():
    driver = getdriver()
    driver.get('https://gab.com/')
    a = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/div/div[2]/a[1]/span")
    a.click()
    return driver

"""
#I think credentialservice functions are outdated and never called
def credentialsgab():
    email = input('what is your email or phone number for gab?\n')
    password = input('what is your password for gab?\n')
    return email,password
"""

def getcontrolgab(driver):
    WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.ID, "user_email")))                                               
    a = driver.find_element_by_id('user_email')
    b = password = driver.find_element_by_id('user_password')
    c = driver.find_element_by_name("button")
    return a,b,c

def injectcredentialsgab(a,b,c,email,password):
    #sleep(3)
    a.send_keys(email)
    b.send_keys(password)
    c.click()

def postinggab(driver,msg):
    #sleep(2)
    WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/main/div/div[1]/div/section/div/div/div[1]/div[2]/div/div")))
    comment = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/main/div/div[1]/div/section/div/div/div[1]/div[2]/div/div")
    comment.click()
    #remains to be done
    sleep(4)
    post_box=driver.switch_to.active_element
    post_box.send_keys(msg)
    WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/main/div/div[1]/div/section/div/div/div[3]/div/div/button/span")))
    #sleep(3)
    publish = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/main/div/div[1]/div/section/div/div/div[3]/div/div/button/span") 
    publish.click()
    #sleep(5)

#This is a new piece it links all the other pieces of the gab posting process together with failsafe in place so that it can fail a step and then retry in case the wait period wasn't long enough and can fail a second time and then simply continue to run the script this makes the whole app in it's current form work way better    
def ex_gab(emailgab, passwordgab, msg):
    try:
        drivergab = initgab()
    except:
        try:
            print('fail gab init waiting 5 sec')
            sleep(5)
            drivergab = initgab()
        except Exception as ex:
            print(ex)
            pass
    try:
        [agab,bgab,cgab] = getcontrolgab(drivergab)
    except:
        try:
            print('fail gab getcontrol waiting 5 sec')
            sleep(5)
            [agab,bgab,cgab] = getcontrolgab(drivergab)
        except:
            print('second fail executed with success')
            pass
    try:
        injectcredentialsgab(agab,bgab,cgab,emailgab,passwordgab)
    except:
        try:
            print('fail gab credentialinjection waiting 5 sec')
            sleep(5)
            injectcredentialsgab(agab,bgab,cgab,emailgab,passwordgab)
        except:
            print('second fail executed with success')
            pass                
    try:
        postinggab(drivergab,msg)
    except:
        try:
            print('fail gab posting waiting 5 sec')
            sleep(5)
            postinggab(drivergab,msg)
        except:
            print('second fail executed with success')
            pass
