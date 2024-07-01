import cv2
import numpy as np

image=cv2.imread("images/hsv_test.png")
cv2.imshow("OR_Image",image)

while True:
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    # cv2.imshow("HSV_IMAGE",hsv)
    l_b=np.array([100,150,0])
    h_b=np.array([140,255,255])
    mask=cv2.inRange(hsv,l_b,h_b)
    cv2.imshow("Mask",mask)
    result=cv2.bitwise_and(image,image,mask=mask)
    cv2.imshow("Mask to or img",result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()