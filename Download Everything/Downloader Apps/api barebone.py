#ok so here is all you need

import pytube
from tkinter import *

def dl():
    url = userurl.get()
    yt = pytube.YouTube(url)
    print(yt.streams)

def dlbyitag():
    url = userurl.get()
    itag = useritag.get()
    yt = pytube.YouTube(url)
    video = yt.streams.get_by_itag(itag)
    video.download("D:\\")



#url = "url"
#yt = pytube.YouTube(url)


#itag = 'itag'
#video = yt.streams.get_by_itag(itag)
#path = "path"
#video.download(path)



window = Tk()
window.title("api barebone")

userurl = StringVar()
useritag = StringVar()

Label(window, text="url", fg="red", font=("Calibri", 15)).grid(sticky=N,padx=100,row =0)
Label(window, text="itag", fg="red", font=("Calibri", 15)).grid(sticky=N,padx=100,row =2)

Button(window,width=20,text="itag info",font=("Calibri",12), command=dl).grid(sticky=N,row=4,pady=15)
Button(window,width=20,text="Download",font=("Calibri",12), command=dlbyitag).grid(sticky=N,row=3,pady=30)

Entry(window,width=50,textvariable=userurl).grid(sticky=N,row=1)
Entry(window,width=50,textvariable=useritag).grid(sticky=N,row=3)

window.mainloop()