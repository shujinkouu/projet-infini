def logpass():
    cwd = os.getcwd()
    d = open(cwd + "\Database\\" + "credentials.txt", 'a')
    password = input('what\'s your password?\n')
    password = password.encode('UTF-8')
    salt = b'\xcc\xd4\xacT\x91\xcb\xf5\x0f\xbct.\xc5\rX\x93\xb5'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode
    key = base64.urlsafe_b64encode(kdf.derive(password))
    #print(key)
    f = Fernet(key)
    secret = password
    token = f.encrypt(secret)
    token = token.decode('UTF-8')
    d.write("your password:"+token)
#    print('written ' + token)
    d.close()
