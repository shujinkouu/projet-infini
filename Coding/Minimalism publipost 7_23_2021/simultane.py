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

#prototype is done and working 
#actually number one priority is making sure we are updating the right version, the right version has access to linkedin,facebook,twiiter and gab and waits for element to load before clicking
#it aso has a failsafe builtin for twitter
#next priority is now making instagram function

"""
text posting services:
minds.com
instagram.com* (requires a picture in every post no all text allowed)
mastodon.com
patreon.com
youtube.com
tumblr
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

#getting to the locally saved webdriver here geckodriver
def getdriver():
    cwd = os.getcwd()
    driver = webdriver.Firefox(executable_path=cwd+"//geckodriver.exe")
    return driver

#instagram
def ex_insta():
    #thanks to @Hawlett on this post "https://stackoverflow.com/questions/46771456/how-to-automate-firefox-mobile-with-selenium" for the insight
    #so this opens a special firefox driver which is on mobile
    user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", user_agent)
    driver = webdriver.Firefox(profile)
    driver.set_window_size(360,640)
    
    driver.get("https://www.instagram.com/")
    
    magicnumber = 2
    sleep(magicnumber)    
    
    skipbtnxpath = "/html/body/div[1]/section/main/article/div/div/div/div[3]/button[1]"
    skipbtn = driver.find_element_by_xpath(skipbtnxpath)
    skipbtn.click()
    
    #emailinsta,passwordinsta
    #we here !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    loginfieldxpath = "/html/body/div[1]/section/main/article/divdriver./div/div/form/div[1]/div[3]/div/label/input"
    loginfield = driver.find_element_by_xpath(loginfieldxpath)
    loginfield.send_keys(emailinsta)
    #
    passwordfieldxpath = "/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input"
    passwordfield = driver.find_element_by_xpath(passwordfieldxpath)
    passwordfield.send_keys(passwordinsta)

    #I don't know what's up with them but they are in the notes so here they are
    skipbtnxpath = "/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]/button"
    skipbtn = driver.find_element_by_xpath(skipbtnpath)
    skipbtn.click()
    skipbtnxpath = "/html/body/div[1]/section/main/div/div/div/button"
    skipbtn = driver.find_element_by_xpath(skipbtnpath)
    skipbtn.click()
    postbtnxpath = "/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]"
    postbtn = driver.find_element_by_xpath(postbtnxpath)
    postbtn.click()
    next = driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/header/div/div[2]/button")
    next.click()
    
    #post
    postbox = driver.find_element_by_xpath("/html/body/div[1]/section/div[2]/section[1]/div[1]/textarea")
    postbox.send_keys(msg)
    #this is for the last button
    post = driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/header/div/div[2]/button")
    post.click()


##This section controls the gab browser and can post a message to the timline
def initgab():
    driver = getdriver()
    driver.get('https://gab.com/')
    a = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/div/div[2]/a[1]/span")
    a.click()
    return driver

#I think credentialservice functions are outdated and never called
def credentialsgab():
    email = input('what is your email or phone number for gab?\n')
    password = input('what is your password for gab?\n')
    return email,password

def getcontrolgab(driver):
    a = driver.find_element_by_id('user_email')
    b = password = driver.find_element_by_id('user_password')
    c = driver.find_element_by_name("button")
    return a,b,c

def injectcredentialsgab(a,b,c,email,password):
    sleep(3)
    a.send_keys(email)
    b.send_keys(password)
    c.click()

def postinggab(driver,msg):
    sleep(2)
    comment = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/main/div/div[1]/div/section/div/div/div[1]/div[2]/div/div")
    comment.click()
    sleep(4)
    post_box=driver.switch_to.active_element
    post_box.send_keys(msg)
    sleep(3)
    publish = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/main/div/div[1]/div/section/div/div/div[3]/div/div/button/span") 
    publish.click()
    sleep(5)

#This is a new piece it links all the other pieces of the gab posting process together with failsafe in place so that it can fail a step and then retry in case the wait period wasn't long enough and can fail a second time and then simply continue to run the script this makes the whole app in it's current form work way better    
def ex_gab():
    try:
        drivergab = initgab()
    except:
        try:
            print('fail gab init waiting 10 sec')
            sleep(5)
            drivergab = initgab()
        except Exception as ex:
            print(ex)
            pass
    try:
        [agab,bgab,cgab] = getcontrolgab(drivergab)
    except:
        try:
            print('fail gab getcontrol waiting 10 sec')
            sleep(5)
            [agab,bgab,cgab] = getcontrolgab(drivergab)
        except:
            print('second fail executed with success')
            pass
    try:
        injectcredentialsgab(agab,bgab,cgab,emailgab,passwordgab)
    except:
        try:
            print('fail gab credentialinjection waiting 10 sec')
            sleep(5)
            injectcredentialsgab(agab,bgab,cgab,emailgab,passwordgab)
        except:
            print('second fail executed with success')
            pass                
    try:
        postinggab(drivergab,msg)
    except:
        try:
            print('fail gab posting waiting 10 sec')
            sleep(5)
            postinggab(drivergab,msg)
        except:
            print('second fail executed with success')
            pass



##This section controls the facebook browser and can post a message to the timline
def init():
    driver = getdriver()
    driver.get('https://www.facebook.com/')
    return driver

def credentials():
    email = input('what is your email or phone number for facebook?\n')
    password = input('what is your password for facebook?\n')
    return email,password

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
    sleep(9)
    ##a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7
    ##m9osqain a5q79mjw jm1wdb64 k4urcfbm
    comment = driver.find_element_by_xpath("//*[@class='m9osqain a5q79mjw jm1wdb64 k4urcfbm']")
    comment.click()
    sleep(5)
    post_box=driver.switch_to.active_element
    post_box.send_keys(msg)
    sleep(2)
    publish = driver.find_element_by_xpath("//*[@class='oajrlxb2 s1i5eluu gcieejh5 bn081pho humdl8nn izx4hr6d rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys d1544ag0 qt6c0cv9 tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l beltcj47 p86d2i9g aot14ch1 kzx2olss cbu4d94t taijpn5t ni8dbmo4 stjgntxs k4urcfbm tv7at329']") 
    publish.click()
    sleep(5)
    
#This is a new piece it links all the other pieces of the gab posting process together with failsafe in place so that it can fail a step and then retry in case the wait period wasn't long enough and can fail a second time and then simply continue to run the script this makes the whole app in it's current form work way better    
def ex_fb():
    try:
        driver = init()
    except:
        try:
            print('fail facebook init waiting 10 sec')
            sleep(5)
            driver = init()
        except:
            print('second fail executed with success')                            
            pass
    try:
        [a,b,c] = getcontrol(driver)
    except:
        try:
            print('fail facebook getcontrol waiting 10 sec')
            sleep(5)
            [a,b,c] = getcontrol(driver)
        except:
            print('second fail executed with success')                            
            pass
    try:
        injectcredentials(a,b,c,email,password)
    except:
        try:
            print('fail facebook credentials inject waiting 10 sec')
            sleep(5)
            injectcredentials(a,b,c,email,password)
        except:
            print('second fail executed with success')                            
            pass
    try:
        posting(driver,msg)
    except:
        try:
            print('fail facebook msgposting waiting 10 sec')
            sleep(5)
            posting(driver,msg)
        except:
            print('second fail executed with success')                            
            pass


##This section controls the twitter browser and can post a message to the timline
def inittwitter():
    driver = getdriver()
    driver.get('https://twitter.com/')
    sleep(5)
    #click on the login button
    button = driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div/span/span")
    button.click()
    return driver

def getcredentialstwitter():
    a = input("what is you email/phone for twitter?\n")
    b = input("what is your password for twitter?\n")
    return a,b

def getfieldtwitter(driver):
    sleep(3)
    atwitter = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
    btwitter = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
    ctwitter = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span")
    return atwitter,btwitter,ctwitter

def logintwitter(emailtwitter,passwordtwitter,atwitter,btwitter,ctwitter,drivertwitter):
    atwitter.send_keys(emailtwitter)
    btwitter.send_keys(passwordtwitter)
    ctwitter.click()
    sleep(6)
    button = drivertwitter.find_element_by_xpath('/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span')
    button.click()

def tweet(drivertwitter,msg):
    post_box=drivertwitter.switch_to.active_element
    post_box.send_keys(msg)

def posttweet(drivertwitter):
    tweetbutton = drivertwitter.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]/div/span/span')
    tweetbutton.click()
    sleep(2)

    
#This is a new piece it links all the other pieces of the gab posting process together with failsafe in place so that it can fail a step and then retry in case the wait period wasn't long enough and can fail a second time and then simply continue to run the script this makes the whole app in it's current form work way better    
def ex_tw():
    try:
        drivertwitter = inittwitter()
    except:
        try:
            print('fail twitter init waiting 10 sec')
            sleep(5)
            drivertwitter = inittwitter()
        except:
            print('second fail executed with success')                            
            pass
    try:
        [atwitter,btwitter,ctwitter] = getfieldtwitter(drivertwitter)
    except:
        try:
            print('fail twitter getfield waiting 10 sec')
            sleep(5)
            [atwitter,btwitter,ctwitter] = getfieldtwitter(drivertwitter)
        except:
            print('second fail executed with success')                            
            pass
    try:
        logintwitter(emailtwitter,passwordtwitter,atwitter,btwitter,ctwitter,drivertwitter)
    except:
        try:
            print('fail twitter login waiting 10 sec')
            sleep(5)
            logintwitter(emailtwitter,passwordtwitter,atwitter,btwitter,ctwitter,drivertwitter)
        except:
            print('second fail executed with success')                            
            pass
    try:
        tweet(drivertwitter,msg)
    except:
        try:
            print('fail twitter msg waiting 10 sec')
            sleep(5)
            tweet(drivertwitter,msg)
        except:
            print('second fail executed with success')                            
            pass
    try:
        posttweet(drivertwitter)
    except:
        try:
            print('fail twitter msgposting waiting 10 sec')
            sleep(5)
            posttweet(drivertwitter)
        except:
            print('second fail executed with success')                            
            pass


##we out of the individal login section and into the logic :) enjoy your trip down the spagetti code land 
#here is one of our most interesting specimen of spagetti code down bellow
def logcredentialsindt(service, credential_list, key):
    print('il semble que certain credentials sois manquant')

    [gab_pass ,gab_email ,twitter_email ,twitter_pass ,facebook_email ,facebook_pass ,insta_email ,insta_pass] = credential_list

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
    #new but should work
    if service.find('i') != -1:
        if insta_email == 'None':
            email_insta = input('login pour instagram?\n')
            saveindt(crypto(email_insta, key), 'email pour instagram:')
        else:
            #cannot adapt I would have to figure out what it does on the other lines like this one
            #those are in module for other service (facebook or gab for example) it has something to do with the var names!
            email_insta = insta_email
        if facebook_pass == 'None':
            pass_insta = input('mot de passe pour instagram?\n')
            saveindt(crypto(pass_insta, key), 'password pour instagram:')
        else:
            pass_insta = insta_pass
        [emailinsta,passwordinsta] = email_insta,pass_insta

    #We had a problem with \n at the end of the database since the way the string is inserted in the dt the first chars are \n then the service used:encrypted(password)
    #this line simply checks the end of the file to see it there is a \n there and if there is not it simply adds it to prevent our script that chops the \n from chopping a bit of the ecrypted message
    checkendofdt()
    #this fishes the credentials and stores them in the credential_list for direct use on this session
    credential_list = fishfromdt(key, service)
    #then the list is derived from credential_list
    [gab_pass,gab_email,twitter_email,twitter_pass,facebook_email,facebook_pass,insta_email,insta_pass] = credential_list
    #which is then sent to be saved back in credential_list we do it this way because the other way caused some problem earlier
    #this should be investigated as it will render the code less overly complicated
    return [gab_pass,gab_email,twitter_email,twitter_pass,facebook_email,facebook_pass, instagram_email, instagram_pass]


#cypto engine
#Those are all pieces which enables us to run an encrypted database with the salt saved as salt.txt and the ecrypted credentials as well as the ecrypted password saved in credential.txt
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

def crypto(input, key):
    f = Fernet(key)
    input = input.encode('UTF-8')
    encrypted_output = f.encrypt(input)
    return encrypted_output.decode('UTF-8')


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
    gab_email = gab_pass = twitter_email = twitter_pass = facebook_email = facebook_pass = instagram_pass = instagram_email = str(None)

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
    return [gab_pass,gab_email,twitter_email,twitter_pass,facebook_email,facebook_pass,instagram_email,instagram_pass]

def decrypt(crypted, key):
    f = Fernet(key)
    decrypted = f.decrypt(crypted.encode('UTF-8'))
    decrypted = decrypted.decode('UTF-8')
    return decrypted
    
    

key = comparepass()
service = input("quels services utiliser? gab(g), twitter(t), facebook(f)")
#service = input("quels services utiliser? gab(g), twitter(t), facebook(f), instagram(i)\n")

credential_list = []
credential_list = fishfromdt(key, service)
[gab_pass ,gab_email ,twitter_email ,twitter_pass ,facebook_email ,facebook_pass, instagram_email, instagram_pass] = credential_list

#This check if there are missing credential and ask the user for them if any services are missing them, this probably don't work so good it needs more testing (investigated as it is now the keyword for this search)
if service.find('g') != -1:
    if gab_pass == "None" or gab_email == "None":
        credential_list = logcredentialsindt(service, credential_list, key)
        [gab_pass ,gab_email ,twitter_email ,twitter_pass ,facebook_email ,facebook_pass ,instagram_email , instagram_pass] = credential_list
if service.find('t') != -1:
    if twitter_email == "None" or twitter_pass == "None":
        credential_list = logcredentialsindt(service, credential_list, key)
        [gab_pass ,gab_email ,twitter_email ,twitter_pass ,facebook_email ,facebook_pass ,instagram_email , instagram_pass] = credential_list
if service.find('f') != -1:
    if facebook_email == "None" or facebook_pass == "None":
        credential_list = logcredentialsindt(service, credential_list, key)
        [gab_pass ,gab_email ,twitter_email ,twitter_pass ,facebook_email ,facebook_pass ,instagram_email , instagram_pass] = credential_list
if service.find('i') != -1:
    if instagram_email == "None" or instagram_pass == "None":
        credential_list = logcredentialsindt(service, credential_list, key)
        [gab_pass ,gab_email ,twitter_email ,twitter_pass ,facebook_email ,facebook_pass ,instagram_email , instagram_pass] = credential_list
#decrypts the credential for the services we are gonna use
if service.find('g') != -1:
    [emailgab,passwordgab] =  decrypt(gab_email, key),decrypt(gab_pass, key)
if service.find('f') != -1:
    [email,password] = decrypt(facebook_email, key),decrypt(facebook_pass, key)
if service.find('t') != -1:
    [emailtwitter,passwordtwitter] = decrypt(twitter_email, key),decrypt(twitter_pass, key)
if service.find('i') != -1:
    [emailinsta,passwordinsta] = decrypt(instagram_email, key),decrypt(instagram_pass, key)


msg = input('quel message post tu aujourd\'hui?\n')
if service.find('g') != -1:
    #Gab
    try:
        ex_gab()
    except:
        pass
if service.find('f') != -1:    
     #facebook    
    try:
        ex_fb()
    except:
        pass
if service.find('t') != -1:
    #twiter
    try:
        ex_tw()
    except:
        pass
if service.find('i') != -1:
    #instagram
    try:
        ex_insta()
    except:
        pass

#video about one of the first versions running this is our goal the less amount of input possible
#ideally the thing already knows the social you want to post on as well as your credentials
# and like in the video only ask you what you want to post, one question that's it!
#https://youtu.be/QjVAZzlAvLo



