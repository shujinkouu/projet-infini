import pytube
url = "https://youtu.be/6iERC2SSNvc"

youtube = pytube.YouTube(url)
#streams = youtube.streams.all()
#for i in streams:
#	print(i)
video = youtube.streams.get_by_itag(18)	
#itag=18
video.download()
print("done")