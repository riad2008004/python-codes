import cv2
image=cv2.imread("images/example.jpg")
gry_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur_image=cv2.GaussianBlur(image,(99,99),0)
cv2.imshow("Example",gry_image)
cv2.imshow("Example_1",image)
cv2.imshow("bluar",blur_image)
cv2.waitKey(0)