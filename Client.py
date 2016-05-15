# import the necessary packages
import socket
import sys
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2 as cv
import numpy
from PIL import Image
import pickle

TCP_IP = '192.168.8.100'
TCP_PORT = 27016
BUFFER_SIZE = 1024
name=''

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket created"
sock.connect((TCP_IP, TCP_PORT))
print "Socket connected"


# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
camera.brightness = 70
rawCapture = PiRGBArray(camera, size=(640, 480))
a=0


# allow the camera to warmup
time.sleep(0.1)


 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array

	#Load a cascade file for detecting faces
	face_cascade = cv.CascadeClassifier('/home/pi/faces.xml')

	#Convert to grayscale
	gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

	#Look for faces in the image using the loaded cascade file
	faces = face_cascade.detectMultiScale(gray, 1.1, 5)

	# clear the stream in preparation for the next frame
	rawCapture.truncate()
	rawCapture.seek(0)

	#Draw a rectangle around every found face
	for (x,y,w,h) in faces:

                if (len(faces) == a):   
                        cv.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
			font = cv.FONT_HERSHEY_SIMPLEX
    			cv.putText(image,name,(((x+w)/2),((y+h)/2)), font, 2,(0,100,0),2,cv.LINE_AA)
		else:
                        cv.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
                        ccrop = image[y:y+h,x:x+w]
                        cv.imwrite('send.jpg',ccrop);
                        imgg = Image.open("send.jpg")

                        imag = {'pixels': imgg.tobytes(),'size': imgg.size,'mode': imgg.mode,}
                        serialize_img = pickle.dumps(imag)
                        print "sending image"
                        print "serializing now"
                        sock.send(str(len(serialize_img)))
                        print "sending length of image"
                        signal = sock.recv(4096)
                        if signal != "OK":
                                print 'No OK recieved'
                        print 'Sending pickle'
                        sent = sock.send(serialize_img)
                        print 'Pickle Sent'
                        print len(serialize_img)
                        print "Waiting to receive"
                        data= sock.recv(BUFFER_SIZE)
                        print >>sys.stderr, 'received "%s"' % data
                        name=data
                        
        a = len(faces)       
        cv.imshow("Frame", image)
	key = cv.waitKey(1) & 0xFF
	
	print "Found "+str(len(faces))+" face(s)"

	print "Found "+name+" face(s)"
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
