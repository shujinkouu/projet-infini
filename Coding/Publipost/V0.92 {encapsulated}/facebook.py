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

from getdriver import getdriver
#Needed: 




#import simultane
#This is outdated was a terminal tool to post on from tkinter.filedialog import askopenfilename
##This section controls the facebook browser and can post a message to the timline
def init():
    driver = getdriver()
    driver.get('https://www.facebook.com/')
    return driver

"""
#I don't think this is getting used in the current ver
def credentials():
    email = input('what is your email or phone number for facebook?\n')
    password = input('what is your password for facebook?\n')
    return email,password
"""

def getcontrol(driver):
    a = driver.find_element_by_xpath(".//*[@id='email']")
    b = driver.find_element_by_xpath(".//*[@id='pass']")
    c = driver.find_element_by_name("login")
    return a,b,c

def injectcredentials(a,b,c,email,password):
    a.send_keys(email)
    b.send_keys(password)
    c.click()

def posting(driver,msg):
    
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div")))
    
    #import keyboard
    #keyboard.press('tab')
    #sleep(0.3)
    #keyboard.press('tab')
    #sleep(0.3)
    #keyboard.press('tab')
    #sleep(0.3)
    #keyboard.press('enter')
    #sleep(0.3)
    #sleep(9)
    ##a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7
    ##m9osqain a5q79mjw jm1wdb64 k4urcfbm
    #comment = driver.find_element_by_xpath("//*[@class='m9osqain a5q79mjw jm1wdb64 k4urcfbm']")
    
    
    #This used to be the comment xpath before 12_2_2021
    #/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]
    
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    comment = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div")
    comment.click()
    
    #remains to be done
    sleep(3)
    post_box=driver.switch_to.active_element
    post_box.send_keys(msg)
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div/div[1]/div/span/span")))
    sleep(2)
    #publish = driver.find_element_by_xpath("//*[@class='oajrlxb2 s1i5eluu gcieejh5 bn081pho humdl8nn izx4hr6d rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys d1544ag0 qt6c0cv9 tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l beltcj47 p86d2i9g aot14ch1 kzx2olss cbu4d94t taijpn5t ni8dbmo4 stjgntxs k4urcfbm tv7at329']") 
    publish = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div/div[1]/div/span/span") 
    publish.click()
    #sleep(5)
    
#This is a new piece it links all the other pieces of the gab posting process together with failsafe in place so that it can fail a step and then retry in case the wait period wasn't long enough and can fail a second time and then simply continue to run the script this makes the whole app in it's current form work way better    
def ex_fb(email, password, msg):
    try:
        driver = init()
    except:
        try:
            print('fail facebook init waiting 5 sec')
            sleep(5)
            driver = init()
        except:
            print('second fail executed with success')                            
            pass
    try:
        [a,b,c] = getcontrol(driver)
    except:
        try:
            print('fail facebook getcontrol waiting 5 sec')
            sleep(5)
            [a,b,c] = getcontrol(driver)
        except:
            print('second fail executed with success')                            
            pass
    try:
        injectcredentials(a,b,c,email,password)
    except:
        try:
            print('fail facebook credentials inject waiting 5 sec')
            sleep(5)
            injectcredentials(a,b,c,email,password)
        except:
            print('second fail executed with success')                            
            pass
    try:
        posting(driver,msg)
    except:
        try:
            print('fail facebook msgposting waiting 5 sec')
            sleep(5)
            posting(driver,msg)
        except:
            print('second fail executed with success')                            
            pass
