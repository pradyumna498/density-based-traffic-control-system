import cv2
import numpy as np
def background():
    cap=cv2.VideoCapture("video.mp4")
    fgbg = cv2.createBackgroundSubtractorMOG2(history=1800,varThreshold=40)
    #no_of_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    i=0
    while(i<400):
        i=i+1
        ret, frame = cap.read()
        fgmask = fgbg.apply(frame)
    cap.release()
    cv2.destroyAllWindows()
    initial_background = fgbg.getBackgroundImage()
    cv2.imwrite("background.jpg",initial_background)
background()
