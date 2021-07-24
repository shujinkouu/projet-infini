import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password = input('what\'s your password?\n')
password = password.encode('UTF-8')
print(password)
salt = b'\xcc\xd4\xacT\x91\xcb\xf5\x0f\xbct.\xc5\rX\x93\xb5'
#os.urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
)
key = base64.urlsafe_b64encode
key = base64.urlsafe_b64encode(kdf.derive(password))
#if password = "b'hi there'" then key = "b'xDb-u3bhogRmYyKvcXuiOYNYjz7q0QVC9_tX0-ES7uA='"
#if password = "b'hi there'" then key = "b'xDb-u3bhogRmYyKvcXuiOYNYjz7q0QVC9_tX0-ES7uA='"
f = Fernet(key)

secret = input("secret message?\n")
secret = secret.encode('UTF-8')
token = f.encrypt(secret)
#token
#b'gAAAAABgPZPjziOZ54MHNaF7kYpW88yKvoY2b8_UDhCQX3aAMthaErVmwA-Ne4w2PI9rYkMlKp-NyOr4jltVTjyXEtstIdKerWOvK_Qwk4J89biqdXg40bs='
crypted = token
print(crypted)
decrypted = f.decrypt(token)
print(decrypted.decode('UTF-8'))
#b'secret message hi!'

#print(salt)
#b'\xcc\xd4\xacT\x91\xcb\xf5\x0f\xbct.\xc5\rX\x93\xb5'

#b'gAAAAABgPahWTParmP00bh8ZU4snkSFxB6fyFFU_Eg3vuCkUpjcLOEutxVFBHhJQUKnJeDSET4pgIcNTgl5VwBed5KCcY-TZTQ=='