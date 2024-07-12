import numpy as np
import cv2
from matplotlib import pyplot

image = cv2.imread("images/car_lane.png")
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
height=image.shape[0]
width=image.shape[1]
n_width=width-170
n_height=height-100

region_of_interest_vertics=[(0,height),(0,n_height),(width/2,height/2),(n_width,height)]

def drow_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1,y1), (x2,y2), (0, 255, 0), thickness=10)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img

def region_of_interest(img,vertics):
    mask=np.zeros_like(img)
    if len(img.shape) > 2:
        channel_count = img.shape[2]
        match_mask_color = (255,) * channel_count
    else:
        match_mask_color = 255
    
    cv2.fillPoly(mask,vertics,match_mask_color)
    masked_image=cv2.bitwise_and(img,mask)
    return masked_image

gray_image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)   
canny_image=cv2.Canny(gray_image,100,200) 
cropped_image=region_of_interest(canny_image,np.array([region_of_interest_vertics],np.int32)) 
lines=cv2.HoughLinesP(cropped_image,6,np.pi/60,160,np.array([]),40,25)
image_with_lines = drow_the_lines(image, lines)

pyplot.subplot(1,1,1)
pyplot.imshow(image_with_lines)
# pyplot.axis(False)
pyplot.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
