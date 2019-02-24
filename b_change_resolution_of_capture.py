import numpy as np
import cv2

cap = cv2.VideoCapture(0)#this acts like a capture device
                        #to capture photo(video) fromour webcam

#this def are for resolution
def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

#changing the resolution of capture video
change_res(600,400)

while(True):#for continuous shot unless q pressed on screen
    # Capture frame-by-frame
    ret, frame = cap.read()#intializing frame

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
