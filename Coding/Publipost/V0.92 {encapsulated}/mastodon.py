from selenium import webdriver
from getdriver import *
from time import sleep
import keyboard

def init():
    driver = getdriver()
    driver.get("https://mastodon.social")
    return driver

def connect(driver, password, email):
    #declaring the id for the email field and the id for the password field
    id1 = "login_user_email"
    id2 = "login_user_password"
    #Select the email field
    login = driver.find_element_by_id(id1)
    login.send_keys(email)
    #Select the password field
    pw = driver.find_element_by_id(id2)
    pw.send_keys(password)
    #select the button
    btn = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/form/div[2]/button')
    btn.click()

def post(driver, msg):
    postbox = driver.find_element_by_class_name('autosuggest-textarea__textarea')
    postbox.send_keys(msg)
    btn = driver.find_element_by_class_name('compose-form__publish-button-wrapper')
    btn.click()

def ex_mastodon():
    




