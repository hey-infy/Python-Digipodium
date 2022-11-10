import cv2
from datetime import datetime as dt                #importing datetime library for getting clock

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
color_black = (0,0,0)    #color written in tuple format (Blue,Green,Red)  (Range: 0-225)    
color_white = (255,255,255)

while cam.isOpened():    
    status,image = cam.read() 
    h,w, _= image.shape()     #shape() is used to find dimnesiona nd color of the image 
    if status:
        #Add text                     
        cv2.putText(image,'Live Camera Feed', (10,30), font, 1, color_black, 2)    #putText() to add text on img on position 10,10 (as previous), 1 is size of font and 2 is thickness of text of title             
        #Draw Box
        cv2.rectangle(image, (5,5), (300,40), (0,255,0),2)       #(x,y) is cordinate of top corner and (300,100) of bottom corner of rectangle (if thickness is -ve put -1)
        #Adding clock on screen 
        timestr = dt.now().strftime("%H:%M:%S")
        cv2.putText(image, timestr, (w-100,70), font, 1, color_black, 2)    #to get clock at right position 
        cv2.imshow('Live Camera', image)
        if cv2.waitKey(1) == 27:    
            break
cam.release() 
cv2.destroyAllWindows() 