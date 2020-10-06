
#DEPENDENCY
import vlc
import tkinter
from tkinter.filedialog import askopenfilename
import time
import os

#FUNCTIONS

#opens up a window so the user gets to select a file this returns the file path under path and the file name under old_file_name
def select_document():
    tkinter.Tk().withdraw()
    global path
    path = askopenfilename()
    path = str(path)
    global old_file_name
    old_file_name = path

#Grabs the media time in ms and chop the last 3 digit to get to seconds return seconds as timeodified
def GetSeconds():
    time = media.get_time()
    time = str(time)
    timemodified = time[:-3]
    print("saved value is " + timemodified + " secondes")

#Selects the path stored in path and popens said document under a vlc window
def open_document():
    print(path)
    global media
    media = vlc.MediaPlayer(path)
    media.play()
    #media.pause()
    #media.stop()
    #media.set|get_time()

def get_timecode(timecodeinms):
    timecodeinsec = round(timecodeinms/1000)
    timecode1 = timecodeinsec%3600
    if (timecodeinsec != timecode1):
        hours = round((timecodeinsec - timecode1)/3600)
    else:
        hours = 0
    if (hours != 0):
        timecodeinsec = timecodeinsec - hours*3600
        timecode1 = timecodeinsec%60
        minutes = round((timecodeinsec - timecode1)/60)
    else:
        timecode1 = timecodeinsec%60
        minutes = round((timecodeinsec - timecode1)/60)

    if (minutes != 0):
        timecodeinsec = timecodeinsec - minutes*60
        seconds = round(timecodeinsec)
    else:
        seconds = round(timecodeinsec)
    if (hours == 0):
        hours = ""
    else:
        pass
    hours = str(hours)
    minutes = str(minutes)
    seconds = str(seconds)
    global timecode
    timecode = str(hours) + "." + str(minutes) + "." + str(seconds)


#CODE

select_document()
open_document()



timecodeinms = media.get_length()
#print("the timecode in ms is " + str(timecodeinms))
#print(old_file_name)

get_timecode(timecodeinms)

#Renaming utility
#has to be executed on close
name = os.path.basename(old_file_name)
path = os.path.dirname(old_file_name)
namewithtimecode = "{" + timecode + "} " + name
path = path + "/" + namewithtimecode
print(path)
new_file_name = path

media.stop()

os.rename(old_file_name, new_file_name)





#setp so that python waits for the video to finish before closing the window
time.sleep(10)
wait = media.get_length()/1000 - 16
time.sleep(wait)

"""
#string decompose
#look at the string from the right and feel the first / position
#then split it at this position to obtain 2 string one the path the other the name of the document


#1233212 timecode in ms
#20.33 timecode in normal human language


#l = old_file_name.index("/")
#, -0, 0


#old_file_name = ""



#
#20.553533333 minutes
#1233.212 seconds
#1233212


print("File renamed!")






#media = vlc.MediaPlayer("../../Videos/Piracy it-s a crime.mp4")
#print(media)
#media.play()
#print("hello world")
#media.play()
"""