import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)
if image is None:
    raise FileNotFoundError("Image not found!")

cv2.imshow("Original Image", image)
cv2.waitKey(0)

plt.hist(image.ravel(), 256, [0, 256])
plt.title("Histogram")
plt.show()

_, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
_, thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
thresh3 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
thresh4 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
_, thresh5 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

titles = ['Original', 'Binary', 'Binary Inv', 'Adaptive Mean', 'Adaptive Gaussian', 'Otsu']
images = [image, thresh1, thresh2, thresh3, thresh4, thresh5]

plt.figure(figsize=(10, 8))
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()

cv2.destroyAllWindows()
