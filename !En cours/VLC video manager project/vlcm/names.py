import os
import tkinter
from tkinter.filedialog import askopenfilename

def select_document():
    tkinter.Tk().withdraw()
    global path
    path = askopenfilename()
    path = str(path)
    global old_file_name
    old_file_name = path


select_document()

name = os.path.basename(old_file_name)
print(name)

#New code
result = name.find("{")
print(result)

if result == -1:
    print("there is no timecode")
if result >= 0:
    print("there is a timecode")
    
locationofsplit = name.find("-")
print(locationofsplit)

name = name[locationofsplit:]
print(name)