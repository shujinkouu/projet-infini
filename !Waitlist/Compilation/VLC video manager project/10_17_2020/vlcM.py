"""
ok so here is my first attempt at a video manager hope you enjoy :3

2 INDENTS:
        *
1 INDENTS:
    *

"""

import vlc
import tkinter
from tkinter.filedialog import askopenfilename
import time
import os
import atexit
import keyboard

def Rename(timecode):
    media.stop()
    name = os.path.basename(old_file_name)
    path = os.path.dirname(old_file_name)
    name = "{" + timecode + "}" + name
    path = path + "/" + name
    #print(path)
    new_file_name = path
    os.rename(old_file_name, new_file_name)
    print("File renamed!")


def exit_handler():
    timecodeinms = media.get_time()
    timecode = TimeCode(timecodeinms)
    Rename(timecode)
    print("we exiting boii!")

def TimeCode(timecodeinms):
    #timecode maker
    #1233212 timecode in ms
    #20.33 timecode in normal human language
    timecodeinsec = round(timecodeinms/1000)
    #print(timecodeinsec)
    timecode1 = timecodeinsec%3600
    #print(timecode1)
    if (timecodeinsec != timecode1):
        hours = round((timecodeinsec - timecode1)/3600)
        #print("you have " + str(hours) + "hours in this content")
    else:
        #print("those two are equal, hours = 0")
        hours = 0

    if (hours != 0):
        timecodeinsec = timecodeinsec - hours*3600
        timecode1 = timecodeinsec%60
        minutes = round((timecodeinsec - timecode1)/60)
        #print(str(minutes) + " minutes")
    else:
        timecode1 = timecodeinsec%60
        minutes = round((timecodeinsec - timecode1)/60)
        #print(str(minutes) + " minutes")

    if (minutes != 0):
        timecodeinsec = timecodeinsec - minutes*60
        seconds = round(timecodeinsec)
        #print(str(seconds) + " seconds")
    else:
        seconds = round(timecodeinsec)
        #print(str(seconds) + " seconds")

    if (hours == 0):
        hours = ""
    else:
        pass

    hours = str(hours)
    minutes = str(minutes)
    seconds = str(seconds)
    #print("hours = " + hours)
    #print("minutes = " + minutes)
    #print("seconds = " + seconds)
    timecode = str(hours) + "." + str(minutes) + "." + str(seconds)
    if timecode[0] == ".":
        timecode = timecode[1:]
    #print(timecode)
    return timecode
    
def select_document():
#    global path
#    path = "../../Videos/Piracy it-s a crime.mp4"
    tkinter.Tk().withdraw()
    global path
    path = askopenfilename()
#    print(path)
#    path = path[13:]
#    print(path)
#    path = '"' + "../.." + path + '"'
    path = str(path)
#    print(path)
    global old_file_name
    old_file_name = path
    
def GetSeconds():
    time = media.get_time()
    time = str(time)
    timemodified = time[:-3]
    print("saved value is " + timemodified + " secondes")

def open_document():
    print(path)
    media = vlc.MediaPlayer(path)
    media.play()
    #media.pause()
    #media.stop()
    #media.set|get_time()


if 0xFF == ord('q'):
#        timecodeinms = media.get_time()
#        timecode = TimeCode(timecodeinms)
#        Rename(timecode)
        print('gu')
        pause()
        exit()


#media = vlc.MediaPlayer("../../Videos/Piracy it-s a crime.mp4")

atexit.register(exit_handler)
select_document()
#open_document()
#print(path)
media = vlc.MediaPlayer(path)
media.play()
#time.sleep(10)
#print(media.get_length())
wait = media.get_length()/1000 - 16
#print("the timecode in ms is " + str(timecodeinms))
#print(old_file_name)

while True:
    try:
        if keyboard.is_pressed('q'):
            print('q ete presse')
            break
    except:
        break

time.sleep(wait)

media.stop()






"""
media = vlc.MediaPlayer("../../Videos/Piracy it-s a crime.mp4")
print(media)
media.play()
print("hello world")
media.play()
"""