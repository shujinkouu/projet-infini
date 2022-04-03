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

#getting to the locally saved webdriver here geckodriver
def getdriver():
    cwd = os.getcwd()
    driver = webdriver.Firefox(executable_path=cwd+"//geckodriver.exe")
    return driver

