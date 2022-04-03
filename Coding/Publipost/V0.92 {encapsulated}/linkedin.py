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

def init():
    driver = getdriver()
    driver.get('https://www.linkedin.com/')
    return driver
    
def injectcredentials(driver, linkedinemail, linkedinpass):
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, 'session_key')))    
    a = driver.find_element_by_id('session_key')
    a.send_keys(linkedinemail)
    #password access:
    b = driver.find_element_by_id("session_password")
    b.send_keys(linkedinpass)
    #login btn:
    c = driver.find_element_by_class_name("sign-in-form__submit-button")
    c.click()
    
def post(driver, msg):
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/div[1]/div/div[1]/button/span')))    
    d = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div[2]/div/div/main/div[1]/div/div[1]/button/span')
    d.click()
    print('here we are!')
    sleep(2)
    box = driver.switch_to.active_element
    box.send_keys(msg)    
    #posting:
    d = driver.find_element_by_class_name('share-box_actions')
    sleep(1)
    d.click()                     


def ex_linkedin(linkedinemail, linkedinpass, msg):
    try:
        driver = init()
    except:
        print('failed linkedin init')
    try:
        injectcredentials(driver, linkedinemail, linkedinpass)
    except:
        print('failed linkedin injectcredentials')
    try:
        post(driver, msg)
    except:
        print('linkedin post failed')