import cv2

image=cv2.imread("images/example.jpg")
cv2.line(image,(0,0),(1000,1000),(0,0,255),5)
cv2.arrowedLine(image,(600,50),(200,300),(0,0,255),5)
cv2.rectangle(image,(50,50),(400,400),(255,0,0),10)
cv2.circle(image,(500,500),100,(0,255,0),10)
cv2.putText(image,"HI",(10,500),cv2.FONT_HERSHEY_SIMPLEX,5,(255,255,255),10,cv2.LINE_AA)
cv2.imshow("Image",image)
cv2.waitKey(0)