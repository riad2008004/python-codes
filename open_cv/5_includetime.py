import cv2
import datetime

vid=cv2.VideoCapture(0)

print(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(vid.get(cv2.CAP_PROP_FRAME_WIDTH))


while True:
    log_f, frame=vid.read()
    frame=cv2.flip(frame,1)
    cv2.putText(frame,"Height: "+str(cv2.CAP_PROP_XI_HEIGHT),(10,10),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.5,(255,0,0),1,cv2.LINE_AA)
    cv2.putText(frame,"Date & Time: " + str(datetime.datetime.now()),(10,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.5,(255,0,0),1,cv2.LINE_AA)
    cv2.imshow("Vid",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows()