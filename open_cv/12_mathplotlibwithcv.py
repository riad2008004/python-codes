import cv2
from matplotlib import pyplot

image_list=[]

for i in range(10):
    image="cv_tutarial/image_"+str(i+1)+".png"
    image_list.append(cv2.imread(image))
    temp="image"+str(i+1)
    # cv2.imshow(temp,image_list[i])
    pyplot.subplot(2,5,i+1)   #to define row colum and figure position
    pyplot.imshow(image_list[i],'gray')   # to show image
    pyplot.title(i+1)   # image title
    pyplot.axis(False)  # to off axis
    
print(len(image_list))    
pyplot.show()    # to show plotted data 
    
cv2.waitKey(0)
cv2.destroyAllWindows()    
