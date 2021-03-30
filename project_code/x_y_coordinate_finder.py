import cv2
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ',', y)
def coordinate_finder():
    frame = cv2.imread('ROI3.jpg')
    cv2.putText(frame, '3',(63,40),cv2.FONT_HERSHEY_SIMPLEX,1.7,(0,255,0),4,cv2.LINE_AA)
    cv2.imshow("image",frame)
    height,width,channels=frame.shape
    print(height,width)
    #ROI=frame[300:720,390:900
    #ROI = frame[350:720, 100:650]
    #ROI = frame[154:354, 215:630]
    #cv2.imwrite("ROI.jpg",ROI)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
coordinate_finder()