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

def GoToTime():
    name = os.path.basename(old_file_name)
    if name[0] == "{":
        print("we have a maybe timecode")
        try:
            if int(name[1]) % 1 == 0:
                print('this is a timecode')
                indexofendtimecode = name.find("}")
                indexofstarttimecode = name.find("{") + 1
                timecode = name[indexofstarttimecode:indexofendtimecode]
                print(timecode)
                splitted = timecode.split('.')
                print(splitted)
                timecodelen = len(splitted)
                
                if timecodelen == 1:
                    print('seconds only')
                    print(splitted[0] + " = seconds")
                    ptimecodeinms = int(splitted[0]) * 1000
                    print(ptimecodeinms)
                if timecodelen == 2:
                    print('minutes and seconds only')
                    print(splitted[0] + " = minutes")
                    print(splitted[1] + " = seconds")
                    ptimecodeinms = int(splitted[1]) * 1000 + int(splitted[0]) * 60 * 1000
                    print(ptimecodeinms)
                if timecodelen == 3:
                    print('hours are here')
                    print(splitted[0] + " = hours")
                    print(splitted[1] + " = minutes")            
                    print(splitted[2] + " = seconds")
                    ptimecodeinms = int(splitted[2]) * 1000 + int(splitted[1]) * 60 * 1000 + int(splitted[0]) * 3600 * 1000
                    print(ptimecodeinms)
                media.set_time(ptimecodeinms)
        except ValueError:
            print('this is a string')

def KeyBind():
    n = 1
    while True:
        try:
    ##this serves the purpose of running code on keypress only once and then resetting this counter to it's natural state (1)
            if n == 2:
                n = 1
                time.sleep(1/10)
                                    
            if keyboard.is_pressed('q'):
                print('q ete presse')
                break

    ##input that doesn't shut the video down should look like this
            if keyboard.is_pressed('b') & n==1:
                while n==1:
                    print('b ete presse')
                    media.pause()
                    n=n+1
                    print("video paused")
                    break

            if keyboard.is_pressed('up') & n==1:
                while n==1:
                    print('up ete presse')
                    current_audio = media.audio_get_volume()
                    print(current_audio + 5)
                    audio_up5 = current_audio + 5
                    media.audio_set_volume(audio_up5)
                    n=n+1
                    break

            if keyboard.is_pressed('down') & n==1:
                while n==1:
                    print('down ete presse')
                    current_audio = media.audio_get_volume()
                    print(current_audio - 5)
                    audio_down5 = current_audio - 5
                    media.audio_set_volume(audio_down5)
                    n=n+1
                    break

            if keyboard.is_pressed('right') & n==1:
                while n==1:
                    #print('right ete presse')
                    current_pos = media.get_time()
                    #print(current_pos + 5000)
                    pos_up5 = current_pos + 5000
                    media.set_time(pos_up5)
                    n=n+1
                    break

            if keyboard.is_pressed('left') & n==1:
                while n==1:
                    #print('left ete presse')
                    current_pos = media.get_time()
                    #print(current_pos - 5000)
                    pos_down5 = current_pos - 5000
                    media.set_time(pos_down5)
                    n=n+1
                    break

        except:
            time.sleep(wait)


def Rename(timecode):
    length = int(media.get_length())
    time = int(media.get_time())
    media.stop()
    name = os.path.basename(old_file_name)
    if isinstance(int(name[1]), int) != False:
        if name[0] == "{":
            print("we have a maybe timecode")
            try:
                if int(name[1]) % 1 == 0:
                    print('this is a timecode')
                    indexofendtimecode = name.rfind("}") + 1
                    name = name[indexofendtimecode:]
                    #print(name)
            except ValueError:
                print('this is a string')
    else:
        pass
        #print(name[1])
        #print(isinstance(name[1], int))
        #print('u have a pb')
    if time>=length-5000:
        name = '_' + name
        print(media.get_time())
        print(media.get_length())
    else:
        name = "{" + timecode + "}" + name
    path = os.path.dirname(old_file_name)
    path = path + "/" + name
    #print(path)
    new_file_name = path
    if name[0] != '_':
        os.rename(old_file_name, new_file_name)
        print("File renamed!")
    else:
        print("already watched")


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

'''
if 0xFF == ord('q'):
#        timecodeinms = media.get_time()
#        timecode = TimeCode(timecodeinms)
#        Rename(timecode)
        print('gu')
        pause()
        exit()
'''

#media = vlc.MediaPlayer("../../Videos/Piracy it-s a crime.mp4")

atexit.register(exit_handler)
select_document()
#open_document()
#print(path)
media = vlc.MediaPlayer(path)
media.play()

GoToTime()

#time.sleep(10)
#print(media.get_length())
wait = media.get_length()/1000


#time.sleep(wait)

#print("the timecode in ms is " + str(timecodeinms))
#print(old_file_name)






KeyBind()    


#media.stop()






"""
media = vlc.MediaPlayer("../../Videos/Piracy it-s a crime.mp4")
print(media)
media.play()
print("hello world")
media.play()
"""