# Face-Recog-Tool
This is a command line tool for facial recognition.It uses image processing library OpenCV.

###Installation
```
git clone https://github.com/JeeveshN/Face-Recog-Tool.git
sudo apt-get install python-opencv
pip install numpy
```
##Getting Started
**Training Set** has to be made before the actual training begins.Multiple pictures of the subjects shot from different angles with preferably different facial expressions would yield the best results.   
Their are 2 ways to achieve this:  
###Fast Mode
Multiple pictures of a single subject are kept in the folder named **Training** (Only single face must be present in each) and 
```
python Train_Faces.py "Name of the Subject"
```
This automatically detects and crops out the face of subject and stores the image in **Dataset** folder (Training Set)
###Learn From Failure
After each prediction the program will ask the user about the wrong predictions and what their correct predictions are supposed to be and will learn and keep getting better accordingly.
Their is a number below each of the detected faces so the user can tell the program which face was wrongly predicted. 
```
Number below face:Correct Name
```
###Learning from wrong Prediction
![](/extras/Selection_017.png?raw=True)   ![](/extras/Selection_019.png?raw=True)  
![](/extras/Selection_018.png?raw=True) 
###Underlying Algorithm
The program uses **Linear Binary Pattern Histogram** approach.The basic idea is not to look at the image as a whole but describe local features of object.
To calculate Local Binary Pattern texture descriptor of a pixel we see all of it's neighbouring 8 pixels and mark a 0 if neighbor is less than center or else a 1 and the binary value calculated by moving around is LBP of center pixel.  
For more details refer to [This](http://docs.opencv.org/2.4/modules/contrib/doc/facerec/facerec_tutorial.html#local-binary-patterns-histograms)   
![](/extras/lbp.png?raw=True)  
##Demo
After their are sufficient number of pictures in the training set preferably 25-30 of each subject then we can start to use the program to make predictions.
```
python Face-Recog.py "Image Path or name(if in same folder)"
```
![](/extras/Selection_016.png?raw=True)
![](/extras/2.png?raw=True )
*Note*: Accuracy is low right now because the number of pictures in the training set are less, as the **Dataset** will grow with time predictions would become more and more accurate 
###Naming Convention For Dataset
Each and every picture to be used in the training set must start with the name of the **Subject** followed by any **Number** 
