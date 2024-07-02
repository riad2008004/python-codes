import cv2
import numpy as np
from matplotlib import pyplot

original_image= cv2.imread("images/messi.jpg")
original_image=cv2.cvtColor(original_image,cv2.COLOR_BGR2RGB)

conv_2d=cv2.filter2D(original_image,-1,(np.ones((5,5),np.float32)/25))
blur=cv2.blur(original_image,(10,10)) #10,10 are kernel size
gussion_blur=cv2.GaussianBlur(original_image,(5,5),0)   #soft blur remove high f noise
median_blur=cv2.medianBlur(original_image,7)    # remove salt peper noise
bileteral_filter=cv2.bilateralFilter(original_image,10,0,0)   # image are blur but edges are sharp

image=[original_image,conv_2d,blur,gussion_blur,median_blur,bileteral_filter]
title=["original","2D_convolution","blur","gussion_blur","median_blur","bileteral_filter"]

for i in range(len(image)):
    pyplot.subplot(2,4,(i+1))
    pyplot.imshow(image[i])
    pyplot.title(title[i])
    pyplot.axis(False)

pyplot.show()
cv2.waitKey(0)