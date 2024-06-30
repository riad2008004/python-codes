import cv2
# import numpy as np

def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print("XY CORDINATE: ", end='')
        print(x,",",y)
        cor_text=str(x)+","+str(y)
        cv2.putText(img,cor_text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),1,cv2.LINE_AA)
        cv2.imshow("Image",img)
        
    elif event==cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        print("RGB: "+str(red)+","+str(green)+","+str(blue))
        brg_text=str(red)+","+str(green)+","+str(blue)
        cv2.putText(img,brg_text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,0),1,cv2.LINE_AA)
        cv2.imshow("Image",img)        
                
img= cv2.imread("images/example.jpg",1)
cv2.imshow("Image",img)

cv2.setMouseCallback("Image",click)
cv2.waitKey(0)
cv2.destroyAllWindows()
