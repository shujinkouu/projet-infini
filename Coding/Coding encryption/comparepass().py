def comparepass():
    cwd = os.getcwd()
    d = open(cwd + "\Database\\" + "credentials.txt", 'r+')
    d = list(d)
    #print(d)
    try:
        #print(passcrypted)
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
        return key
        #print(key)
        f = Fernet(key)
        secret = password
        #    print(secret)
        token = f.encrypt(secret)
        #token = token.decode('UTF-8')
        #    print(token)
        passcrypted = d[0]
        passcrypted = passcrypted[passcrypted.find(':')+1:]

        try:
            if f.decrypt(token) == f.decrypt(passcrypted.encode('UTF-8')):
                #print("same pass")
                pass
        except UnboundLocalError:
            print("first pass")
        except:
            print("wrong password")
            exit()
    except IndexError:
        logpass()
        pass
