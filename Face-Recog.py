import cv2
import sys
import os
import re
import numpy as np
import shelve,random
from PIL import Image
if len(sys.argv) < 2:
    print "Usage: python Detect_face.py 'image path'"
    sys.exit()

image_path=sys.argv[1]
font = cv2.FONT_HERSHEY_SIMPLEX
cascade="Face_cascade.xml"
face_cascade=cv2.CascadeClassifier(cascade)
Datafile = shelve.open("Data")
if 'Data' not in Datafile.keys():
    Datafile['Data']=list()
    Data_list = list()
else:
    Data_list = Datafile["Data"]

print Datafile["Data"]

def Make_Changes(label):
    if label not in Data_list:
        Data_list.append(label)

def get_images(path):
    images = list()
    labels = list()
    count=0
    for img in os.listdir(path):
        regex = re.compile(r'(\d+|\s+)')
        labl = regex.split(img)
        labl = labl[0]
        print labl
        print count
        count=count+1
        Make_Changes(labl)
        image_path =os.path.join(path,img)
        image=cv2.imread(image_path)
        image_grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        images.append(image_grey)
        labels.append(Data_list.index(labl))
    return images,labels

#def add_to_dataset(image):
def initialize_recognizer():
    face_recognizer = cv2.createLBPHFaceRecognizer()
    Dataset = get_images("./Dataset")
    face_recognizer.train(Dataset[0],np.array(Dataset[1]))
    return face_recognizer

def save_wrong_faces(num,temp_set):
    print "Enter number below face : Correct Name:\n"
    for i in xrange(num):
        inp = raw_input()
        inp = inp.split(":")
        print inp
        os.chdir("./Dataset")
        cv2.imwrite(inp[1]+ str(random.uniform(0,100000))+ ".jpg",temp_set[int(inp[0])])
        os.chdir("../")



def recognize(image_path,face_recognizer):
    image=cv2.imread(image_path)
    image_grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image_grey,scaleFactor=1.16,minNeighbors=5,minSize=(25,25),flags=0)
    temp_set = list()
    num=0
    for x,y,w,h in faces:
        sub_img=image_grey[y-10:y+h+10,x-10:x+w+10]
        temp_set.append(sub_img)
        nbr,conf = face_recognizer.predict(sub_img)
        print conf,nbr
        cv2.rectangle(image,(x,y),(x+w,y+h),(255, 255,0),2)
        cv2.putText(image,Data_list[nbr],(x,y-5), font, 0.5,(255,255,0),1)
        cv2.putText(image,str(num),(x,y+h+13), font, 0.5,(255,255,0),1)
        cv2.imwrite("Detected.jpg",image)
        num = int(num)+1
    Datafile["Data"]=Data_list
    Datafile.close()
    os.system("xdg-open Detected.jpg")
    print "No. of faces predicted wrong:"
    num_wrong = input()
    if num_wrong !=0:
        save_wrong_faces(num_wrong,temp_set)

def main():
    face_r = initialize_recognizer()
    recognize(image_path,face_r)




if __name__ == "__main__":
    main()
