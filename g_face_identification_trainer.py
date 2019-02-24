import os
import cv2
from PIL import Image
import numpy as np
import pickle

#calling and storing the file for face recognition
face_cascade=cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognizer=cv2.face.LBPHFaceRecognizer_create()


BASE_DIR=os.path.dirname(os.path.abspath(__file__))         #gives the current working directory
image_dir=os.path.join(BASE_DIR,"images")


#giving id to each similar label(face) from 0 to ... and storing the labels in label_ids
current_id=-1;
label_ids={};

y_labels=[]
x_train=[]

#looking for the images
#root=folders inside images folder
for root,dirs,files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
            path=os.path.join(root,file)

            #label is the person name directory
            label=os.path.basename(root).replace(" ","-").lower()       #lowercase and removespace
            print(path,label)
            

            if not label in label_ids:
                current_id+=1
                label_ids[label]=current_id
               
            id_=label_ids[label]
            print(label_ids)
            

            
            
            #y_labels.append(label)   #all the persons name....we want to use some number for labels
            #x_train.append(path)      #all the images path.....we want to verify this image,turn it into NUMPY array,covert to gray
            
            pil_image=Image.open(path).convert("L")#making  grayscale.

            #resizing image
            #size=(500,500)
            #final_image=pil_image.resize(size,Image.ANTIALIAS)
            
            image_array=np.array(pil_image,"uint8")#coverting image into array of numbers that is every pixel value
            print(image_array)

            #faces stores coodinates values of all the face in this particular frame
            faces=face_cascade.detectMultiScale(image_array,scaleFactor=1.5,minNeighbors=5)

            for(x,y,w,h) in faces:
                roi=image_array[y:y+h , x:x+w]#storing the face part of grey frame
                x_train.append(roi)
                print(id_)
                y_labels.append(id_)
print(x_train)
print(y_labels)



#having got the data about the faces
#x_train[i] contain the face in terms of array and y_label[i] contains the corresponding id of the face
#this data is passed to our previous face test program
#this data is campared with the face in capture and then accrdinly actions are taken

with open("labels.pickle",'wb') as fil:
    pickle.dump(label_ids,fil)


recognizer.train(x_train,np.array(y_labels))
recognizer.save("trainner.yml")
