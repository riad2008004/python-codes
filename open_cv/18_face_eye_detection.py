import cv2
face_cascade=cv2.CascadeClassifier("xml_files/haarcascade_frontalface_default.xml")
image=cv2.imread("images/riad.jpg")
image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(image_gray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),3)

cv2.imshow("Image",image)
cv2.waitKey()
