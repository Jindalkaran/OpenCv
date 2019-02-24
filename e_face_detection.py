import numpy as np
import cv2

#calling and storing the file for face recognition
face_cascade=cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#cascade works on gray

    #faces stores coodinates values of all the face in this particular frame
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)#scalefactor=accuracy

    #x and y denotes the bottom and left axis face
    #w andh denotess width and height
    
    for(x,y,w,h) in faces:
        #print(x,y,w,h)
        roi_gray=gray[y:y+h , x:x+w]#storing the face part of grey frame

        #saving the face part
        img_item="my_image.png"
        cv2.imwrite( img_item,roi_gray)

        #drwaing rectangle
        color=(200,156,200) #in BGR
        stroke=2;
        end_cord_x=x+w;
        end_cord_y=y+h;
        cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y),color,stroke)
        
    cv2.imshow('frame',frame)    
    
    if(cv2.waitKey(20) & 0xFF==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
