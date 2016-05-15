import socket                                      
import sys
import pickle       
from PIL import Image 
import numpy
import math
import matlab.engine
import os


eng = matlab.engine.start_matlab()                              # Starting the matlab engine through which we will later call the matlab script
TCP_IP = '192.168.8.103'                                        #Server IP
TCP_PORT = 27016    
BUFFER_SIZE = 1024                                              #Server


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
sock.bind((TCP_IP, TCP_PORT))



print "In listening mode"
sock.listen(1)
conn, addr = sock.accept()

BUFFER_SIZE = 4096
serialize_img = ''

while True:
    
    print >>sys.stderr, '\nwaiting to receive message'

    length = int(conn.recv(4096))                           # recieving the length of the image from the client 
    
    conn.send("OK")                                         # An Ack to tell the client that length of the image is recieved
   
    count = 0                                               # Loop for recieving untill the expected length is reached
    while len(serialize_img) != length:
        im= conn.recv(4096)
        serialize_img+=im

    print >>sys.stderr, 'received %s bytes from ' % (len(im))


    img = pickle.loads(serialize_img)                                   # Deserializing the image recieved
    my_im = Image.frombytes(img['mode'], img['size'], img['pixels'])    # converting image into desire format pil image in this case

    
    #print >>sys.stderr, data
    
    my_im.save("F:/r2015b/bin/communication/recieved.jpg","JPEG")             # writing recieved filedata into the destination file
    a=eng.predictlabel()                                                      # Calling matlab function to predict label of this input image 
    pkl_file = open('myfile.pkl', 'rb')                                       # saving image in location from where matlab code will read the image 
    myDict = pickle.load(pkl_file)                                            # A dictionary where we have names accross the label codes
    label=myDict.get(a)                                                       # getting name corresponding the recieved label
    
    sent = conn.send(label)                                                   # Sending name to the client 
    pkl_file.close()                                                          # closing the file

    print >>sys.stderr, 'sent %s bytes back to ' % (sent)               
    serialize_img = ''	