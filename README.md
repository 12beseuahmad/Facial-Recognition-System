# Facial-Recognition-System
A system built using computer vision toolbox matlab and opencv python capable of identifying a person in the video for security purposes deployed on a raspberry pi


Real time facial recognition system is a turn-key solution deployed on a raspberry pi capable of identifying or verifying a person from a video frame. This would be achieved by comparing the facial features of the face detected from the video frame with the facial features of the face gallery present in the database. The main purpose of the system will be for security only but can be increasingly used for other purposes as-well.
Initially, face recognition systems focused on still images. However, during the last years research on face recognition in image sequences has gained much attention, although nearly all systems apply still-image face recognition techniques to individual frames. In addition to its broader number of applications, video-based face recognition provides several advantages over still image based face recognition.
The main steps involved in our system are as follow:


#Input:
The input for the system will be obtained through a Raspberry Pi Cam in the form of a live video feed


#Image Extraction:
The image will be extracted frame by frame from the video for further processing.


#Face Detection:
This step is responsible for detecting the face from the video frame. The technique that we will be using for face detection is the Voila and Jones face detection algorithm.



#Face Recognition:


•	Feature extraction: The technique that we will be using for feature extraction is Histogram Of Oriented Gradient features and Local Binary Pattern (LBP) features.


•	Feature Classification: We will use Multi Class Support Vector Machine (SVM) for feature classification.  


#Final Output: 
The result that will be obtained from the classifier will be the label corresponding to that face in the model.

#How To Run:
The repo contains the following files    

Client.py	          : This is file that is responsible for face detection in the video, it detect the face in the video, crops it and then send this cropped face to the server (server.py).You have to run this file from the Raspberry pi.Later this file recieves the label from the server and place it on the face present in the video.   

FaceTraining.m	    : This is the file that is responsible for training the SVM model that will be later used for prediction of the test image.The directory structure and the training process is explained in the file itself. you have to place this file in the working environment of matlab.   

Server.py	          : This is the python Server that is on the Pc where matlab is installed. The server purpose is to recieve the cropped face from the client(running on raspberry pi) recognize this face and returen the label to the client   

dictionary.py       : A dictionary is created for the code and name mapping.we have assigned a code to each face class. later on time of recognition the server by using this dictionary sends client the label corresponding to the code in the dictionary   

predictlabel.m      : This is the matlab script that will be called by the python server. this file returns the label of the face fed into it	   

preprocessing.m     : This file does some preprocessing on the face so that on time of feature extraction we can have clear and detailed features   


place .m file in matlab working environment, client.py on raspberry pi, server.py on matlab pc

#System Flow

Raspberry pi camera detect the face from the video (client.py file) sends this face to serer.py the server on recieving this image sends this image to a matlab script(predictlabel.m)
and wait for the label to get returned the predictlabel script uses the trained SVM model for prediction (trained model is obtained through FaceTraining.m).The predict model on prediction find the class code then it resolve the name correspondin to this code using the dictionary of code:name that was stored previously on the disk using (dictionary.pi)
predict label sends the name to server.py the server.py sends this name to the client.py running on raspberry pi the client.py then displays this recieved name on the face that was detected in the frame

#Demo Video

https://www.dropbox.com/s/26c7aitvworas88/FRS_Final_Defence_Demo.mp4?dl=0
