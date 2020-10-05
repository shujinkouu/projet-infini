import os
import cv2
import numpy as np

filename = "output2.mp4" # .avi .mp4
frames_per_seconds = 24.0
my_res = "720p" # 1080p

#Standard Video Dimensions Sizes

def get_dims(cap, res="1080p"):
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[res]
    change_res(cap, width, height)
    return width, height

# Video Encoding, might require additional installs
# Types of Codes: http://www.fourcc.org/codecs.php
VIDEO_TYPE = {
    "avi": cv2.VideoWriter_fourcc(*"XVID"),
    #"mp4": cv2.VideoWriter_fourcc(*"H264"),
    "mp4": cv2.VideoWriter_fourcc(*"XVID"),
}

def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return VIDEO_TYPE["avi"]

#Set resolution for the video capture
#Function adapted from https://kirr.co/016qmh
def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

STD_DIMENSIONS = {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4K": (3840, 2160),
}

cap = cv2.VideoCapture(0)
dims = get_dims(cap, res=my_res)
print(dims)
video_type_cv2 = get_video_type(filename)

#out = cv2.VideoWriter("output.mp4", int(cv2.VideoWriter_fourcc(*"XVID")), 24.0, 1920, 1080, cap)

out = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*"XVID"), 24.0, (1280, 720))
#out = cv2.VideoWriter(filename, video_type_cv2, frames_per_seconds, dims)


while(True):
    # Capture fra-by-frame
    ret, frame = cap.read()
    
    out.write(frame)
    
    # Display the resulting frame
    cv2.imshow("frame", frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
        
# When everything is done, Close everything

cap.release()
out.release()
cv2.destroyAllWindows()