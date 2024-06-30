import cv2

vid=cv2.VideoCapture(0)

print(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(vid.get(cv2.CAP_PROP_FRAME_WIDTH))

vid.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
vid.set(cv2.CAP_PROP_FRAME_WIDTH,1080)
print(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(vid.get(cv2.CAP_PROP_FRAME_WIDTH))

while True:
    log_f, frame=vid.read()
    frame=cv2.flip(frame,1)
    cv2.imshow("Vid",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows()