import cv2

messi=cv2.imread("images/messi.jpg")
cup=cv2.imread("images/cup.png")

# cv2.imshow("Image",cv2.resize(messi,(512,512)))
# cv2.imshow("Image_1",cv2.resize(cup,(512,512)))

messi_resized = cv2.resize(messi, (512, 512))
cup_resized = cv2.resize(cup, (512, 512))

merged_image=cv2.addWeighted(messi_resized,0.9,cup_resized,0.2,1)
cv2.imshow("Image_3",merged_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


