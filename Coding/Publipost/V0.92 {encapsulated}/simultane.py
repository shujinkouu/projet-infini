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

#let's import our new package
import instagram
import linkedin
import gab
import facebook
import twitter

#instagram is in construction but priority is now making the prototype
#prototype is done and working 
#actually number one priority is making sure we are updating the right version, the right version has access to linkedin,facebook,twiiter and gab and waits for element to load before clicking
#it aso has a failsafe builtin for twitter
#next priority is now making instagram function

"""
text posting services:
parler.com                      
minds.com
instagram.com*
mastodon.com
#patreon.com
#youtube.com
#tumblr
gab.com*
facebook.com*
twitter.com*


video posting service:
youtube
bitchute
gloria.tv
rumble
"""

def databaseinit():
    os.getcwd()
    path = os.getcwd() + "\\database"
    try:
        os.mkdir(path)
    except:
        pass
        #print("we already have a database")

##we out of the individal login section and into the logic :) enjoy your trip down the spagetti code land 
#here is one of our most interesting specimen of spagetti code down bellow
def logcredentialsindt(service, credential_list, key):
    print('il semble que certain credentials sois manquant')

    [gab_pass ,gab_email ,twitter_email ,twitter_pass ,facebook_email ,facebook_pass ,insta_email ,insta_pass, linkedin_email, linkedin_pass] = credential_list

    if service.find('g') != -1:
        if gab_email == 'None':
            email_gab = input('courriel pour gab?\n')
            saveindt(crypto(email_gab, key), 'email pour gab:')
        else: 
            email_gab = gab_email
        if gab_pass == 'None':
            pass_gab = input('mot de passe pour gab?\n')
            saveindt(crypto(pass_gab, key), 'password pour gab:')
        else:
            pass_gab = gab_pass
        [emailgab,passwordgab] = email_gab,pass_gab

    if service.find('t') != -1:
        if twitter_email == 'None':
            email_twitter = input('courriel pour twitter?\n')
            saveindt(crypto(email_twitter, key), 'email pour twitter:')
        else:
            email_twitter = twitter_email
        if twitter_pass == 'None':
            pass_twitter = input('mot de passe pour twitter\n')
            saveindt(crypto(pass_twitter, key), 'password pour twitter:')
        else:
            pass_twitter = twitter_pass
        #another field should be added for id_twitter to deal with our contingency :)                                                                                
        [emailtwitter,passwordtwitter] = email_twitter,pass_twitter

    if service.find('f') != -1:
        if facebook_email == 'None':
            email_facebook = input('login pour facebook?\n')
            saveindt(crypto(email_facebook, key), 'email pour facebook:')
        else:
            email_facebook = facebook_email
        if facebook_pass == 'None':
            pass_facebook = input('mot de passe pour facebook?\n')
            saveindt(crypto(pass_facebook, key), 'password pour facebook:')
        else:
            pass_facebook = facebook_pass
        [email,password] = email_facebook,pass_facebook

    if service.find('i') != -1:
        if insta_email == 'None':
            email_insta = input('login pour instagram?\n')
            saveindt(crypto(email_insta, key), 'email pour instagram:')
        else:
            email_insta = insta_email
        if facebook_pass == 'None':
            pass_insta = input('mot de passe pour instagram?\n')
            saveindt(crypto(pass_insta, key), 'password pour instagram:')
        else:
            pass_insta = insta_pass
        [emailinsta,passwordinsta] = email_insta,pass_insta

    if service.find('l') != -1:
        if linkedin_email == 'None':
            email_linkedin = input('login pour linkedin?\n')
            saveindt(crypto(email_linkedin, key), 'email pour linkedin:')
        else:
            email_linkedin = linkedin_email
        if linkedin_pass == 'None':
            pass_linkedin = input('mot de passe pour linkedin?\n')
            saveindt(crypto(pass_linkedin, key), 'password pour linkedin:')
        else:
            pass_linkedin = linkedin_pass
        [linkedinemail, linkedinpass] = email_linkedin, pass_linkedin

    #We had a problem with \n at the end of the database since the way the string is inserted in the dt the first chars are \n then the service used:encrypted(password)
    #this line simply checks the end of the file to see it there is a \n there and if there is not it simply adds it to prevent our script that chops the \n from chopping a bit of the ecrypted message
    checkendofdt()
    #this fishes the credentials and stores them in the credential_list for direct use on this session
    credential_list = fishfromdt(key, service)
    #then the list is derived from credential_list
    [gab_pass,gab_email,twitter_email,twitter_pass,facebook_email,facebook_pass,insta_email,insta_pass,linkedin_email,linkedin_pass] = credential_list
    #which is then sent to be saved back in credential_list we do it this way because the other way caused some problem earlier
    #this should be investigated as it will render the code less overly complicated
    return [gab_pass,gab_email,twitter_email,twitter_pass,facebook_email,facebook_pass, insta_email, insta_pass, linkedin_email, linkedin_pass]

def logpass():
    cwd = os.getcwd()
    d = open(cwd + "\Database\\" + "credentials.txt", 'a')
    print('it seems you have no password yet')
    password = input('what\'s your password?\n')
    password = password.encode('UTF-8')
    key = keygen(password)
    f = Fernet(key)
    secret = password
    token = f.encrypt(secret)
    token = token.decode('UTF-8')
    d.write("your password:"+token)
    d.close()
    #This print is often useful to troubleshoot an error in the decrypting of the credentials
    #print("the key is "+ key.decode('UTF-8'))
    return key

def comparepass():
    databaseinit()
    cwd = os.getcwd()

    #trys to open it if it doesn't open simply creates one and then opens it
    try:
        d =  open(cwd+ "\Database\\" + "credentials.txt", "r+")
    except:
        d =  open(cwd+ "\Database\\" + "credentials.txt", "x")
        d.close()
        d = open(cwd+"\Database\\"+"credentials.txt", "r+")
    d = list(d)
    #if d is an empty list it means this is the first use of the app the user is then prompted to log his password which is gonna be used to encrypt his credentials if not it asks the user for his password and then generated the key from his typed password
    if d == []:
        key = logpass()
        return key
    else:
        password = input("what is your password?\n")    
        key = keygen(password.encode('UTF-8'))

    #I personally don't understand how this works even on first use yet I think it does, should be investigated
    passcrypted = d[0]
    passcrypted = passcrypted[passcrypted.find(':')+1:]
    #print("passcrypted is: "+passcrypted)

    f = Fernet(key)
    try:
        decrypt = f.decrypt(passcrypted.encode('UTF-8'))
    except:
        print("wrong password this will close shortely")
        sleep(3)
        exit()
    if decrypt == password.encode('UTF-8'):
        return key

def saveindt(a, service_name):
    cwd = os.getcwd()
    d = open(cwd + "\Database\\" + "credentials.txt", 'a') 
    d.write('\n'+service_name+a)
    d.close()

#This is an extra piece of code which solve a very specific problem it might not be needed in the future
def checkendofdt():
    cwd = os.getcwd()
    d = open(cwd + "\Database\\" + "credentials.txt", 'a') 
    drea = open(cwd + "\Database\\"+ "credentials.txt",'r')
    dread = list(drea)
    drea.close()
    length = len(dread)
    last_line = dread[length-1]
    length_last_line = len(last_line)
    if last_line[length_last_line-1] == "=" and last_line[length_last_line-2] == "=":
        d.write('\n')
    d.close()

def fishfromdt(key, service):
    cwd = os.getcwd()
    d = open(cwd + "\Database\\" + "credentials.txt", 'r')
    d = list(d)
    n = len(d)
    #sets default value so that if the credential doesn't exist it is equal to none in our list
    gab_email = gab_pass = twitter_email = twitter_pass = facebook_email = facebook_pass = instagram_pass = instagram_email = linkedin_pass = linkedin_email = str(None)

    for n in d:
        n = n[:n.find('\n')]
        if n.find('your password:') == 0:
            pass
        if service.find('g') != -1:
            if 'gab' in n and 'email' in n:
                gab_email = n[n.find(':')+1:]
            if 'gab' in n and 'password' in n:
                gab_pass = n[n.find(':')+1:]
        if service.find('t') != -1:
            if 'twitter' in n and 'email' in n:
                twitter_email = n[n.find(':')+1:]
            if 'twitter' in n and 'password' in n:
                twitter_pass = n[n.find(':')+1:]
        if service.find('f') != -1:
            if 'facebook' in n and 'email' in n:
                facebook_email = n[n.find(':')+1:]
            if 'facebook' in n and 'password' in n:
                facebook_pass = n[n.find(':')+1:]
        if service.find('i') != -1:
            if 'instagram' in n and 'email' in n:
                instagram_email = n[n.find(':')+1:]
            if 'instagram' in n and 'password' in n:
                instagram_pass = n[n.find(':')+1:]
        if service.find('l') != -1:
            if 'linkedin' in n and 'email' in n:
                linkedin_email = n[n.find(':')+1:]
            if 'linkedin' in n and 'password' in n:
                linkedin_pass = n[n.find(':')+1:]
    return [gab_pass ,gab_email ,twitter_email ,twitter_pass ,facebook_email ,facebook_pass ,instagram_email , instagram_pass, linkedin_email, linkedin_pass]

def logservice():
    cwd = os.getcwd()
    d = open(cwd + "\Database\\" + "service.txt", 'a')
    service = input("quels services utiliser? gab(g), twitter(t), facebook(f), linkedin(l)")
    d.write("your services:"+service)
    d.close()
    return service

def checkservice():
    cwd = os.getcwd()
    try:
        d =  open(cwd+ "\Database\\" + "service.txt", "r+")
    except:
        d =  open(cwd+ "\Database\\" + "service.txt", "x")
        d.close()
        d = open(cwd+"\Database\\"+"service.txt", "r+")
    d = list(d)
    if d == []:
        service = logservice()
    else:
        d = d[0]
        service = d[d.find(":")+1:]
    return service

def checkcredentials(credential_list,gab_pass ,gab_email ,twitter_email ,twitter_pass ,facebook_email ,facebook_pass ,instagram_email , instagram_pass, linkedin_email, linkedin_pass):
    #This check if there are missing credential and ask the user for them if any services are missing them, this probably don't work so good it needs more testing (investigated as it is now the keyword for this search)
    if service.find('g') != -1:
        if gab_pass == "None" or gab_email == "None":
            credential_list = logcredentialsindt(service, credential_list, key)
            [gab_pass ,gab_email ,twitter_email ,twitter_pass ,facebook_email ,facebook_pass ,instagram_email , instagram_pass, linkedin_email, linkedin_pass] = credential_list
    if service.find('t') != -1:
        if twitter_email == "None" or twitter_pass == "None":
            credential_list = logcredentialsindt(service, credential_list, key)
            [gab_pass ,gab_email ,twitter_email ,twitter_pass ,facebook_email ,facebook_pass ,instagram_email , instagram_pass, linkedin_email, linkedin_pass] = credential_list
    if service.find('f') != -1:
        if facebook_email == "None" or facebook_pass == "None":
            credential_list = logcredentialsindt(service, credential_list, key)
            [gab_pass ,gab_email ,twitter_email ,twitter_pass ,facebook_email ,facebook_pass ,instagram_email , instagram_pass, linkedin_email, linkedin_pass] = credential_list
    if service.find('i') != -1:
        if instagram_email == "None" or instagram_pass == "None":
            credential_list = logcredentialsindt(service, credential_list, key)
            [gab_pass ,gab_email ,twitter_email ,twitter_pass ,facebook_email ,facebook_pass ,instagram_email , instagram_pass, linkedin_email, linkedin_pass] = credential_list
    if service.find('l') != -1:
        if linkedin_email == "None" or linkedin_pass == "None":
            credential_list = logcredentialsindt(service, credential_list, key)
            [gab_pass ,gab_email ,twitter_email ,twitter_pass ,facebook_email ,facebook_pass ,instagram_email , instagram_pass, linkedin_email, linkedin_pass] = credential_list
    return [gab_pass ,gab_email ,twitter_email ,twitter_pass ,facebook_email ,facebook_pass ,instagram_email , instagram_pass, linkedin_email, linkedin_pass]

def postonallservices():
    if service.find('g') != -1:
        #Gab
        try:
            gab.ex_gab(emailgab, passwordgab, msg)
        except:
            pass
    if service.find('f') != -1:    
        #facebook    
        try:
            facebook.ex_fb(email, password, msg)
        except:
            pass
    if service.find('t') != -1:
        #twiter
        try:
            twitter.ex_tw(emailtwitter, passwordtwitter, msg)
        except:
            pass
    if service.find('i') != -1:
        #instagram
        try:
            instagram.ex_insta(emailinsta, passwordinsta, imagepath, msg)
        except:
            pass
    if service.find('l') != -1:
        #linkedin
        try:
            linkedin.ex_linkedin(linkedinemail, linkedinpass, msg)
        except:
            pass

#cypto engine
#Those are all pieces which enables us to run an encrypted database with the salt saved as salt.txt and the ecrypted credentials as well as the ecrypted password saved in credential.txt
#Generates the key used to encrypt or decrypt
def keygen(password):
    #Try to fish the salt in dt
    try:
        cwd = os.getcwd()
        d = open(cwd + "\Database\\" + "salt.txt", 'r+')
        l = list(d)
        d.close()
        #This bit we are chopping there's probably a better way to go about thing
        #didn't found it yet, should be investigated
        l = str(l[0])[4:]
        l = l[:-1]
        salt = l.encode('UTF-8')

    #if the salt isn't in dt it creates it and saves it as salt.txt in dt
    except:
        salt = os.urandom(16)
        d = open(cwd + "\Database\\" + "salt.txt", 'a')

        #This is where we are then forced to chop the salt it is because it is saved as bytes converted to string using str() which makes it so that the string has extra b'' which is then chopped before use if we could convert it to str first which would remove the b'' it would be the best the example with the print was supposed to demonstrate it didn't work I left it there after trying for a while to patch this problem this is what I have settled on in the mean time. This should deffinitely be investigated further
        #after looking for five minutes this is what the same process looks like other places in this code (logpass())
        #token = token.decode('UTF-8')
        #d.write("your password:"+token)

        saltp = str(salt)
        #saltp = salt.decode('UTF-8')
        #print(saltp)

        d.write(saltp)
        d.close()
        #again the chopping to make it useable for this session
        saltp = saltp[4:]
        saltp = saltp[:-1]
        salt = saltp.encode('UTF-8')

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    #This print is often useful to troubleshoot an error in the decrypting of the credentials
    #print("the key is "+ key.decode('UTF-8'))
    return key

#encrypts the input
def crypto(input, key):
    f = Fernet(key)
    input = input.encode('UTF-8')
    encrypted_output = f.encrypt(input)
    return encrypted_output.decode('UTF-8')

#decrypts the input
def decrypt(crypted, key):
    f = Fernet(key)
    decrypted = f.decrypt(crypted.encode('UTF-8'))
    decrypted = decrypted.decode('UTF-8')
    return decrypted

#used to decrypt all the credentials at once to be used #needs to be changed when adding services
def decryptall():
    #decrypts the credential for the services we are gonna use
    emailgab=passwordgab=email=password=emailtwitter=passwordtwitter=emailinsta=passwordinsta=linkedinemail=linkedinpass = None
    if service.find('g') != -1:
        [emailgab,passwordgab] =  decrypt(gab_email, key),decrypt(gab_pass, key)
    if service.find('f') != -1:
        [email,password] = decrypt(facebook_email, key),decrypt(facebook_pass, key)
    if service.find('t') != -1:
        [emailtwitter,passwordtwitter] = decrypt(twitter_email, key),decrypt(twitter_pass, key)
    if service.find('i') != -1:
        [emailinsta,passwordinsta] = decrypt(instagram_email, key),decrypt(instagram_pass, key)
    if service.find('l') != -1:
        [linkedinemail,linkedinpass] = decrypt(linkedin_email, key),decrypt(linkedin_pass, key)
    return [emailgab,passwordgab,email,password,emailtwitter,passwordtwitter,emailinsta,passwordinsta,linkedinemail,linkedinpass]


key = comparepass()

#service = input("quels services utiliser? gab(g), twitter(t), facebook(f), linkedin(l)")
service = checkservice()

#service = input("quels services utiliser? gab(g), twitter(t), facebook(f), instagram(i)\n")

credential_list = []
credential_list = fishfromdt(key, service)
[gab_pass ,gab_email ,twitter_email ,twitter_pass ,facebook_email ,facebook_pass ,instagram_email , instagram_pass, linkedin_email, linkedin_pass] = credential_list

credential_list = checkcredentials(credential_list,gab_pass ,gab_email ,twitter_email ,twitter_pass ,facebook_email ,facebook_pass ,instagram_email , instagram_pass, linkedin_email, linkedin_pass)
[gab_pass ,gab_email ,twitter_email ,twitter_pass ,facebook_email ,facebook_pass ,instagram_email , instagram_pass, linkedin_email, linkedin_pass] = credential_list
credential_list = decryptall()
[emailgab,passwordgab,email,password,emailtwitter,passwordtwitter,emailinsta,passwordinsta,linkedinemail,linkedinpass] = credential_list

msg = input('quel message post tu aujourd\'hui?\n')

if service.find('i') != -1:
    print('please select an image')
    import imgpath
    imagepath = imgpath.imgpath()

postonallservices()

#video about one of the first versions running this is our goal the less amount of input possible
#ideally the thing already knows the social you want to post on as well as your credentials
#and like in the video only ask you what you want to post, one question that's it!
#https://youtu.be/QjVAZzlAvLo



