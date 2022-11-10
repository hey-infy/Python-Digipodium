#Base code for OpenCV
import cv2

cam = cv2.VideoCapture(0)    #To turn camera on and assign it to a variable for further ref

while cam.isOpened():    #while camera is open
    status,image = cam.read()      #cam ob reads camera value, if there is something status will be true and img can be generated
    if status:                   #if status is true  then perform further operation  
        #betweeen these two lines more code will be written 
        cv2.imshow('Live Camera', image)           #Show the generated final image with all operations performed
        if cv2.waitKey(1) == 27:    #27 is ASCII for Escape key   (to stop the camera)
            break
cam.release() 
cv2.destroyAllWindows()      