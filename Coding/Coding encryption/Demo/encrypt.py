import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import tempfile
import time

def keygen(password):
    try:
        cwd = os.getcwd()
        d = open(cwd + "\Database\\" + "salt.txt", 'r+')
        l = list(d)
        d.close()
        l = str(l[0])[4:]
        l = l[:-1]
        print(l)
        salt = l.encode('UTF-8')
        print(salt)
    except:
        salt = os.urandom(16)
        d = open(cwd + "\Database\\" + "salt.txt", 'a')
        saltp = str(salt)
        #saltp = salt.decode('UTF-8')
        print(saltp)
        d.write(saltp)
        d.close()
        saltp = saltp[4:]
        saltp = saltp[:-1]
        salt = saltp.encode('UTF-8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    #print("encryption salt used is: "+str(salt))
    key = base64.urlsafe_b64encode(kdf.derive(password))
    #print("encryption key used is: "+ str(key))
    return key

def crypto(input, key):
    f = Fernet(key)
    input = input.encode('UTF-8')
    encrypted_output = f.encrypt(input)
    return encrypted_output.decode('UTF-8')


def saveindt(a):
    cwd = os.getcwd()
    tf = tempfile.NamedTemporaryFile()
    random_name = tf.name
    random_name = random_name[random_name.rindex("\\")+1:]
    d = open(cwd + "\Database\\" + "encrypted msg "+random_name+ ".txt", 'a')    
    d.write(a+"\n")
    d.close()
    print("the encrypted message "+random_name+" was created in the database")

password = input('enter the password you\'ll use to encrypt your secret message\n')
secret = input('enter the message to be encrypted\n')

key = keygen(password.encode('UTF-8'))
encrypted_msg = crypto(secret, key)
saveindt(encrypted_msg)

time.sleep(0)