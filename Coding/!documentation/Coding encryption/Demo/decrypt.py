import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import time

def getencryptedmsg():
    cwd = os.getcwd()
    d = open(cwd + "\Database\\" + "decrypt msg.txt", 'r+') 
    d = list(d)
    d = str(d[0])
    d = d[:-1]
    print(d)
    print(d.encode('UTF-8'))
    return d.encode('UTF-8')

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
        print("decryption salt used is: "+str(salt))
    except:
        salt = os.urandom(16)
        d = open(cwd + "\Database\\" + "salt.txt", 'a')
        saltp = salt.decode('UTF-8')
        #print(saltp)
        d.write(saltp)
        d.close()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    print(salt)
    key = base64.urlsafe_b64encode(kdf.derive(password))
    print(key)
    return key

def decrypt(input, key):
    print(input)
    print("decryption key used is: "+ str(key))
    f = Fernet(key)
    hi = f.encrypt(b'hi')
    print("!!!"+hi.decode('UTF-8'))
    hi = f.decrypt(hi)
    print("!!!"+hi.decode('UTF-8'))
    print("!!!"+input.decode('UTF-8'))
    print("!!!!!!!!!!!!!")
    #print(f.decrypt(b'gAAAAABgQGsy2b0I1f8S6A4Zxfbj4SQEicUQ4vw1VUTdzeC_8SvngF_FKCnwfWiBz2Sut8de3M0WjDMdakyO4DeDRFKwyndpcw=='))
    decrypted_output = f.decrypt(input)
    print('holla')
    return decrypted_output.decode('UTF-8')

password = input('enter the password you used to encrypt your secret message\n')

key = keygen(password.encode('UTF-8'))
encrypted_msg = getencryptedmsg()
#print(encrypted_msg)
print('hi there')
decrypted = decrypt(encrypted_msg, key)

print(decrypted)

time.sleep(0)