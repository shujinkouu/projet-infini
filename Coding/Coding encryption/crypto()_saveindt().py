def crypto(input, key):
    f = Fernet(key)
    input = input.encode('UTF-8')
    encrypted_output = f.encrypt(input)
    return encrypted_output.decode('UTF-8')


def saveindt(a, service_name):
    print('we in saveindt()')
    cwd = os.getcwd()
    d = open(cwd + "\Database\\" + "credentials.txt", 'a') 
    d.write('\n'+service_name+a)
