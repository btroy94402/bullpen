'''created by Brian Troy (bitroy@yahoo.com)
Simple use of the python cv2 modele to stream your webcam.  Video is 
imported as RGB numpy array and displayed realtime in a while loop.  Image feed can
be converted to grayscale (see comments).  Press q to close the loop
and the video stream.'''

import cv2
import os

video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()  #Check is boolean data type, frame is numpy array.  This reads the image.

    print(check)
    print(frame)#Three dimensional numpy array since its a color image.
	
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = frame #default webcam feed is RGB.  
				 #If grayscale is desired comment out this line
				 #and uncomment #'gray=..." line immediately following.
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	
	cv2.imshow("Capturing",gray) #capturing is window title.  gray is the image variable.
   
    key=cv2.waitKey(30)
    
    if key==ord('q'): #While loop will stop when user presses q.
        break
video.release()  #releases the webcam
cv2.destroyAllWindows #closes the display window(s) in memory.
