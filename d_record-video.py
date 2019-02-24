import numpy as np
import os
import cv2

def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

# Standard Video Dimensions Sizes  Dictionary
STD_DIMENSIONS =  {"480p": (640, 480),"720p": (1280, 720)}
# change cap scale based on input  and return the same dimensions
def get_dims(cap, res):
    width, height = STD_DIMENSIONS["480p"]#for default if wrong input res  given
    if res in STD_DIMENSIONS:
        width,height = STD_DIMENSIONS[res]
    ## change the current caputre device
    ## to the resulting resolution
    change_res(cap, width, height)
    return width, height




# Video Encoding, might require additional installs
# Types of Codes: http://www.fourcc.org/codecs.php
VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    #'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}

#getting the extension of filename created 
def get_video_type(filename):
    filename, exten = os.path.splitext(filename)
    if exten in VIDEO_TYPE:
      return  VIDEO_TYPE[exten]
    return VIDEO_TYPE['avi']





filename = 'recoded_video.mp4'#or avivideo format
frames_per_second = 24.0# Set resolution for the video capture
my_res=input("Enter Resolution:")
#for recrding audio we use ffmpg and not opencv

cap = cv2.VideoCapture(0)
#get_dims is replaced by height and width based on out input res
dimensions=get_dims(cap, my_res)
out = cv2.VideoWriter(filename, get_video_type(filename), 25, dimensions)

while True:
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()
