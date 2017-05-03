import cv2
import random
import os
import sys

count = 0

cap = cv2.VideoCapture(0)


def start(directory_name):
	while True:
		if cap.grab():
			RET, IMAGE = cap.retrieve()
			if not RET:
				continue
			global count
			count += 1
			if count%25 == 0:
				cv2.imwrite(str(random.uniform(0, 100000)) + ".jpg", IMAGE)
			cv2.imshow("Video", IMAGE)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		count =- 1
	cap.release()
	cv2.destroyAllWindows()


def main():
    if len(sys.argv) != 2:
        print "Usage: create_dataset.py <Name of the person>"
        sys.exit()

    name = sys.argv[1]
    name = "./"+name

    if os.path.exists(name):
        print "name already exists"
        name = name+str(random.randint(0, 10000))
        print "So, the dataset has been saved as" + name
    
    os.makedirs(name)
    os.chdir(name)

    start(name)


if __name__ == "__main__":
	main()
