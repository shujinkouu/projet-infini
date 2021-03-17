def select_document():
#    global path
#    path = "../../Videos/Piracy it-s a crime.mp4"
    tkinter.Tk().withdraw()
    global path
    path = askopenfilename()
    print(path)
#    path = path[13:]
    print(path)
#    path = '"' + "../.." + path + '"'
    path = str(path)
    print(path)
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



#DEBUG FUNCTIONS

def get_timecode_debug(timecodeinms):
    timecodeinsec = round(timecodeinms/1000)
    print(timecodeinsec)
    timecode1 = timecodeinsec%3600
    print(timecode1)

    if (timecodeinsec != timecode1):
        hours = round((timecodeinsec - timecode1)/3600)
        print("you have " + str(hours) + "hours in this content")
    else:
        print("those two are equal, hours = 0")
        hours = 0

    if (hours != 0):
        timecodeinsec = timecodeinsec - hours*3600
        timecode1 = timecodeinsec%60
        minutes = round((timecodeinsec - timecode1)/60)
        print(str(minutes) + " minutes")
    else:
        timecode1 = timecodeinsec%60
        minutes = round((timecodeinsec - timecode1)/60)
        print(str(minutes) + " minutes")

    if (minutes != 0):
        timecodeinsec = timecodeinsec - minutes*60
        seconds = round(timecodeinsec)
        print(str(seconds) + " seconds")
    else:
        seconds = round(timecodeinsec)
        print(str(seconds) + " seconds")

    if (hours == 0):
        hours = ""
    else:
        pass

    print("hours = " + str(hours))
    print("minutes = " + str(minutes))
    print("seconds = " + str(seconds))


    hours = str(hours)
    minutes = str(minutes)
    seconds = str(seconds)


    print("hours = " + hours)
    print("minutes = " + minutes)
    print("seconds = " + seconds)

    global timecode
    timecode = str(hours) + "." + str(minutes) + "." + str(seconds)
    print(timecode)
