import numpy as np
import cv2

def trackbar_call_1(x):
    pass
def trackbar_call_2(x):
    pass
def trackbar_call_3(x):
    pass

# img_2=cv2.imread("images/cup.png")
img_1=np.zeros((512,512,3),np.uint8)

cv2.namedWindow("Image")
cv2.imshow("Image",img_1)

cv2.createTrackbar("R","Image",0,255,trackbar_call_1)
cv2.createTrackbar("G","Image",0,255,trackbar_call_2)
cv2.createTrackbar("B","Image",0,255,trackbar_call_3)

while True:
    r=cv2.getTrackbarPos("R","Image")
    g=cv2.getTrackbarPos("G","Image")
    b=cv2.getTrackbarPos("B","Image")
    
    img_1[:]=(b,g,r)
    cv2.imshow("Image",img_1)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
