import cv2
import numpy as np
from initial_processing import *
def object_detection(cap,object_detector):
    totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    i=0
    areas=[0]*90
    sum_total_area=0
    mycontours=[]
    while i<totalFrames:
        i=i+1
        total_area = 0
        ret,frame=cap.read()
        height,width,_=frame.shape
        #extract region of interest
        ROI=frame[350:720,100:650]
        myarea=370*550
        mask=object_detector.apply(ROI)
        #cv2.imshow("masked",mask)
        #cv2.waitKey(0)
        _,mask=cv2.threshold(mask,127,255,cv2.THRESH_BINARY)
        #finding contours in the image
        contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            #calculate area and remove small components
            area=cv2.contourArea(cnt)
            if area>800:
                x,y,w,h=cv2.boundingRect(cnt)
                total_area=total_area+(w*h)
                #drawung rectangle along the detected contours
                cv2.rectangle(ROI, (x, y), (x + w, y + h), (0, 255, 0), 3)
        sum_total_area = sum_total_area + total_area
        if(i<90):
            areas[i]=total_area
        else:
            sum_total_area=sum_total_area-areas[i%90]
            areas[i%90]=total_area
        print(i,total_area,"density:",(total_area*100)/myarea)
        cv2.imshow("ROI", ROI)
        """"
        if(sum_total_area<1000 and i>100):
            print("less vehicle density")
            break
        """
        key=cv2.waitKey(30)
        if key==27:
            break
    cap.release()
    print(mycontours)
def mainProgram(cap):
    """"
    count=initial_process(cap)
    print(count)
    if count<20:
        return
    """
    object_detector=cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=40)
    object_detection(cap,object_detector)
    #cv2.imshow("background",background)
    #cv2.waitKey(0)


