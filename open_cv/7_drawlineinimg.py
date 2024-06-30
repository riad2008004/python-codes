import cv2
import numpy as np
count,p,q=0,0,0

def click(event,x,y,flags,param):
    global count,p,q
    if event == cv2.EVENT_LBUTTONDOWN:
        if count==0:
            print(x,",",y)
            cv2.circle(img,(x,y),5,(255,0,0),2)
            p=x
            q=y 
            count=count+1  
            cv2.imshow("Image",img)           
        else:  
            print(x,",",y)             
            cv2.circle(img,(x,y),5,(255,0,0),2)
            cv2.line(img,(p,q),(x,y),(255,0,0),2) 
            p=x
            q=y 
            count=count+1 
            cv2.imshow("Image",img)
                
img=np.zeros([512,512,3],np.uint8)
cv2.imshow("Image",img)

cv2.setMouseCallback("Image",click)
cv2.waitKey(0)
cv2.destroyAllWindows()
