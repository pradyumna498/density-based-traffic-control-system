import cv2
def pixel_coordinates():
    frame = cv2.imread('background1.jpg')
    dict1=dict()
    for i in range(460,720):
            dict1[i]=[]
    for i in range(460,720):
        for j in range(0,620):
            b,g,r=frame[i][j]
            if((b<50 and g<50 and r>200 )):
                dict1[i].append(j)
    count=0
    for keys in dict1:
        count=count+len(dict1[keys])
    print(count)
    return dict1,count
