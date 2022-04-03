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
from getdriver import *


def init():
    #thanks to @Hawlett on this post "https://stackoverflow.com/questions/46771456/how-to-automate-firefox-mobile-with-selenium" for the insight
    #so this opens a special firefox driver which is on mobile
    
    user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", user_agent)
    driver = webdriver.Firefox(profile)
    driver.set_window_size(360,640)
    
    #driver = getdriver()
    driver.get("https://www.instagram.com/")
    return driver

def injectcredentials(driver, emailinsta, passwordinsta):
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/section/main/article/div/div/div/div[3]/button[1]")))    
    btn = driver.find_element_by_xpath('/html/body/div[1]/div/div/section/main/article/div/div/div/div[3]/button[1]')
    btn.click()
    #skipbtnxpath = "/html/body/div[1]/section/main/article/div/div/div/div[3]/button[1]"
    #skipbtn = driver.find_element_by_xpath(skipbtnxpath)
    #skipbtn.click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input")))
    loginfieldxpath = "/html/body/div[1]/div/div/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input"
    loginfield = driver.find_element_by_xpath(loginfieldxpath)
    loginfield.send_keys(emailinsta)
    passwordfieldxpath = "/html/body/div[1]/div/div/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input"
    passwordfield = driver.find_element_by_xpath(passwordfieldxpath)
    passwordfield.send_keys(passwordinsta)
    skipbtnxpath = "/html/body/div[1]/div/div/section/main/article/div/div/div/form/div[1]/div[6]/button/div"
    skipbtn = driver.find_element_by_xpath(skipbtnxpath)
    skipbtn.click()
    try:
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/section/main/div/div/div/button")))    
        btn = driver.find_element_by_xpath('/html/body/div[1]/div/div/section/main/div/div/div/button')
        btn.click()
    except:
        pass

def post(driver, imagepath, msg):
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/section/nav[2]/div/div/div[2]/div/div/div[3]")))    
    xpath = "/html/body/div[1]/div/div/section/nav[2]/div/div/div[2]/div/div/div[3]"
    btn = driver.find_element_by_xpath(xpath)
    btn.click()
    sleep(1)
    #print(imagepath)
    keyboard.write(imagepath)
    sleep(3)
    press('enter')
    sleep(0.2)
    press('enter')
    WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/section/div[1]/header/div/div[2]")))        
    btn_suivant = driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div[1]/header/div/div[2]')
    btn_suivant.click()
    sleep(6)
    WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/section/div[2]/section[1]')))        
    post_box = driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div[2]/section[1]')
    #post_box=driver.switch_to.active_element
    post_box.click()
    sleep(1)
    keyboard.write(msg)
    #print('msg should be written')
    sleep(3)
    keyboard.press('tab')
    #sleep(1)
    WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/section/div[1]/header/div/div[2]")))        
    share_btn = driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div[1]/header/div/div[2]')
    share_btn.click()



#instagram
def ex_insta(emailinsta, passwordinsta, imagepath, msg):
    try:
        try:
            driver = init()
        except:
            print('driver initialization failed')
        try:
            injectcredentials(driver, emailinsta, passwordinsta)
        except:
            print('failed credential injection')
        try:
            post(driver, imagepath, msg)
        except:
            print('failed message posting')
    except:
        import instagram_desktop
        instagram_desktop.ex_insta(emailinsta, passwordinsta, imagepath, msg)



