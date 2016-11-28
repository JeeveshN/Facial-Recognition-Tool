import cv2
import sys
import os
import re
import numpy as np
import shelve

if len(sys.argv) < 2:
    print "Usage: python Detect_face.py 'image path'"
    sys.exit()

image_path=sys.argv[1]
font = cv2.FONT_HERSHEY_SIMPLEX
cascade="Face_cascade.xml"
face_cascade=cv2.CascadeClassifier(cascade)
d = {0:"Sherlock",1:"Watson"}

def get_images(path):
    images = list()
    labels = list()
    for img in os.listdir(path):
        labl = re.findall("(.*)[0-9]",img)
        print labl
        if "Watson" in labl[0]:
            c=1
        else:
            c=0
        image_path =os.path.join(path,img)
        image=cv2.imread(image_path)
        image_grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        images.append(image_grey)
        labels.append([c])
    return images,labels

#def add_to_dataset(image):
def initialize_recognizer():
    face_recognizer = cv2.createLBPHFaceRecognizer()
    Dataset = get_images("./Dataset")
    face_recognizer.train(Dataset[0],np.array(Dataset[1]))

def recognize(image_path):
    image=cv2.imread(image_path)
    image_grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image_grey,scaleFactor=1.16,minNeighbors=5,minSize=(25,25),flags=0)
    temp_set = list()
    num=0
    for x,y,w,h in faces:
        sub_img=image_grey[y-10:y+h+10,x-10:x+w+10]
        temp_set.append(sub_img)
        nbr,conf = face_recognizer.predict(sub_img)
        print conf
        cv2.rectangle(image,(x,y),(x+w,y+h),(255, 255,0),2)
        cv2.putText(image,d[nbr],(x,y-5), font, 0.4,(255,255,0),1)
        cv2.putText(image,str(num),(x,y+h+13), font, 0.5,(255,255,0),1)
        num = int(num)+1

    cv2.imshow("Faces Found",image)
    cv2.waitKey(0)
