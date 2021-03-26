import cv2
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ',', y)
def coordinate_finder():
    frame = cv2.imread('background.jpg')
    cv2.imshow("image",frame)
    height,width,channels=frame.shape
    print(height,width)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
coordinate_finder()
