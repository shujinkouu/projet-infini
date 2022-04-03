import cv2
from tkinter.filedialog import askopenfilename
import os
from time import sleep

def choosetime():
    st = int(input('start time'))
    stinframe = st*24
    se = int(input('end time'))
    seinframe = se*24
    return stinframe,seinframe

def init():
    n=0
    while True:
        n=n+1
        print(n)
        success, img = cap.read()
        if n >= int(stinframe) and n <= int(seinframe):
            #cv2.imshow("Video", img)
            out.write(img)
            if n == int(seinframe):
                break
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            print(str(n))
            break
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()





path = askopenfilename()
cap = cv2.VideoCapture(path)
stinframe,seinframe = choosetime()
sleep(1)

cwd =os.getcwd()
out = cv2.VideoWriter(cwd+"/output.mp4", cv2.VideoWriter_fourcc(*"XVID"), 24.0, (1280, 720))

sleep(3)

init()
