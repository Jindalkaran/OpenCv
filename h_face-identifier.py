import numpy as np
import cv2
import pickle

#calling and storing the file for face recognition
face_cascade=cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognizer=cv2.face.LBPHFaceRecognizer_create()

recognizer.read("trainner.yml")

#for getting names of the lable since the trainer file contains only the id_ number
#this contains name:1 but we want something like 1:name therefore reversing
labels={"person_name":1}
with open("labels.pickle",'rb') as f:                    
    og_labels=pickle.load(f)                            
    labels={v:k for k,v in og_labels.items()}
    
print(labels)

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #faces stores coodinates values of all the face in this particular frame
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)

    #x and y denotes the bottom and left axis face
    #w andh denotess width and height
    
    for(x,y,w,h) in faces:
        #print(x,y,w,h)
        roi_gray=gray[y:y+h , x:x+w]#storing the face part of grey frame

        #recodnize
        id_,conf=recognizer.predict(roi_gray)  #this inbuilt function compares the face with recognizer and returns the id with conference(amount of similarity)
        print(conf)
        if conf>=45 and conf<=70 :
            print(id_)
            print(labels[id_])
            #printing name on image
            font=cv2.FONT_HERSHEY_SIMPLEX
            name=labels[id_]
            color=(150,20,150)
            stroke=2;
            cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)

        #making rectangle
        color=(200,20,20)
        stroke=2;
        end_cord_x=x+w;
        end_cord_y=y+h;
        cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y),color,stroke)
        
    cv2.imshow('frame',frame)    
    
    if(cv2.waitKey(20) & 0xFF==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
