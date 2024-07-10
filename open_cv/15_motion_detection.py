import cv2
import cv2.version

cap=cv2.VideoCapture("video/car_move.mp4")

_,p_frame=cap.read()
_,l_frame=cap.read()

while cap.isOpened():
    diff=cv2.absdiff(p_frame,l_frame)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    gray_blur=cv2.GaussianBlur(gray,(9,9),0)
    _,binary=cv2.threshold(gray_blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(binary,None,iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        # cv2.drawContours(p_frame,contours,-1,(0,255,0),3)
        if cv2.contourArea(contour)>900:
            x,y,w,h=cv2.boundingRect(contour)
            cv2.rectangle(p_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("VID",p_frame)
    
    p_frame=l_frame
    _,l_frame=cap.read()
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
cap.release()