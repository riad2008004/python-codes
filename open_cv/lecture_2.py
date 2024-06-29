import cv2
vid=cv2.VideoCapture("video/example.mp4")
while True:
    nongarHub,img=vid.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break    
    