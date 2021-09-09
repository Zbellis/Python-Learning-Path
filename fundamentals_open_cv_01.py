import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as numpy
import cv2

image_color = mpimg.imread("background3.jpg")
plt.imshow(image_color)
image_color.shape
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
plt.imshow(image_gray, cmap='gray')

image_gray.shape
image_gray
cv2.imwrite("background3_grayscale.jpg", image_gray)

color_image = cv2.imread("background3.jpg")
cartoon_image = cv2.stylization(color_image, sigma_s = 200, sigma_r=0.3)
cv2.imshow('cartoon', cartoon_image)
cv2.waitKey()
cv2.destroyAllWindows()

