import cv2
import sys
import os
import random

cascade = "../face_cascade.xml"
face_cascade=cv2.CascadeClassifier(cascade)
dir_path = False

def detect(image_path,name):
    image = cv2.imread(os.path.abspath(image_path))
    # cv2.imshow("Faces Found",image)
    image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image_grey,scaleFactor=1.16,minNeighbors=5,minSize=(25,25),flags=0)
    for x,y,w,h in faces:
        sub_img=image[y:y+h,x:x+w]
        os.chdir("../../Dataset/")
        cv2.imwrite(name+ str(random.uniform(0,100000))+ ".jpg",sub_img)
        os.chdir("../Trainer")
        os.chdir(directory_path)


def main():
    if len(sys.argv) != 2:
        print "Usage: python train_faces.py <Name of person>"
        sys.exit()

    name = sys.argv[1]

    global directory_path
    directory_path = "./" 

    directory_path = directory_path+sys.argv[1]+"/"

    if not os.path.exists(directory_path):
        print "No images exist for the given person"
        sys.exit()

    os.chdir(directory_path)
    
    print "Creating Proper Dataset......."
    images_exist = False
    for img in os.listdir("."):
        if img.endswith('.jpg') or img.endswith('.png') or img.endswith('.jpeg'):
            detect(img, name)
            images_exist = True
    if not images_exist:
        print "No images found to create a dataset"

if __name__ == "__main__":
    main()

