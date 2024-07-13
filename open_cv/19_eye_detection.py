import cv2

eye_cascade=cv2.CascadeClassifier("xml_files/haarcascade_eye_tree_eyeglasses.xml")
face_cascade=cv2.CascadeClassifier("xml_files/haarcascade_frontalface_default.xml")

image=cv2.imread("images/riad.jpg")
image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(image_gray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)
    copy_face=image_gray[y:y+h,x:x+w]
    eyes=eye_cascade.detectMultiScale(copy_face)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(image,(x+ex,y+ey),(x+ex+ew,y+ey+eh),(255,255,0),2)

cv2.imshow("Image",image)
cv2.waitKey(0)