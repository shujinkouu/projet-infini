import os

#simply move this file to env variable for immediate push capability by using push.py whilst in the directory in cmd
# this is all coming from https://www.geeksforgeeks.org/python-os-system-method/ thank to the guys over hhere for the idea :)

msg = input("push msg?\n")
msg = "\""+msg+"\""
msg2 = input("push description, leave empty for blank\n") 
msg2 = "\""+msg2+"\""

#os.system("git status")

def push():
    os.system("git add .")
    
    os.system("git commit -m "+msg+" -m "+msg2)
    os.system("git push")
    print("push was a success")
#print(msg)
#if msg != "":
push()
#else:
#    print("aborted")