import cv2
from pixel_coordinates import *
def initial_process(cap):
    count=0
    dict1,count1=pixel_coordinates()
    cap.set(cv2.CAP_PROP_POS_FRAMES,84)
    status,initial_frame=cap.read()
    initial_frame=initial_frame[0:,0:]
    gray_initial_frame = cv2.cvtColor(initial_frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_initial_frame, 30, 200)
    cv2.imwrite("background2.jpg", edges)
    for y in dict1.keys():
        for x in dict1[y]:
            if edges[y][x]>0:
                edges[y][x]=0
                count=count+1
    cv2.imwrite("background3.jpg",edges)
    print(count)
    return (count/count1)*100
