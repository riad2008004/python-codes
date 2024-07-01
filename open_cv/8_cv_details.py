import cv2  #split image

img=cv2.imread("images/example.jpg")

croped_copy=img[100:400 , 100:400]

img[300:600, 600:900]=croped_copy

cv2.imshow("Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()


