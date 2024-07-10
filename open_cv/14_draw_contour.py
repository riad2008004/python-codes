import cv2

sample_image=cv2.imread("images/opencv_logo.png")
sample_image_g=cv2.cvtColor(sample_image,cv2.COLOR_BGR2GRAY)
_,binary_image=cv2.threshold(sample_image_g,200,255,cv2.THRESH_BINARY)
contours,hc=cv2.findContours(binary_image,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

cv2.drawContours(sample_image,contours,5,(0,255,0),3)

cv2.imshow("Original",sample_image)
cv2.imshow("Gray",sample_image_g)
cv2.imshow("Binary",binary_image)

cv2.waitKey(0)
cv2.destroyAllWindows()