import cv2
import sys
import os,random
cascade="../Face_cascade.xml"
face_cascade=cv2.CascadeClassifier(cascade)
def detect(image_path,name):
    image=cv2.imread(os.path.abspath(image_path))
    cv2.imshow("Faces Found",image)
    image_grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image_grey,scaleFactor=1.16,minNeighbors=5,minSize=(25,25),flags=0)
    print faces
    for x,y,w,h in faces:
        sub_img=image[y-5:y+h+5,x-5:x+w+5]
        os.chdir("../Dataset")
        cv2.imwrite(name+ str(random.uniform(0,100000))+ ".jpg",sub_img)
        os.chdir("../Trainer")
        cv2.rectangle(image,(x,y),(x+w,y+h),(255, 255,0),2)
    cv2.imshow("Faces Found",image)
    cv2.waitKey(0)


if len(sys.argv) < 2:
    print "Usage: python Train_Faces.py 'Name of person'"
    sys.exit()
name = sys.argv[1]

for img in os.listdir("."):
    if img.endswith('.jpg') or img.endswith('.png') or img.endswith('.jpeg'):
        detect(img,name)
