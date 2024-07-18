# Importing the Modules or Libraries
import numpy as np 
import cv2 

# Reading the image
image = cv2.imread('Images/Car.jpg')

# Resizing the image
# Interpolation
image_resized = cv2.resize(image, None, fx=0.5, fy=0.5)


# Removing the impurities from image
image_cleared = cv2.medianBlur(image_resized, 3)
image_cleared = cv2.medianBlur(image_cleared, 3)
image_cleared = cv2.medianBlur(image_cleared, 3)

image_cleared = cv2.edgePreservingFilter(image_cleared, sigma_s=5)

# Bilateral Image filtering 
image_filtered = cv2.bilateralFilter(image_cleared, 3, 10, 5)

for i in range(2):
	image_filtered = cv2.bilateralFilter(image_filtered, 3, 20, 10)

for i in range(3):
	image_filtered = cv2.bilateralFilter(image_filtered, 5, 30, 10)

for i in range(3):
	image_filtered = cv2.bilateralFilter(image_filtered, 5, 20, 10)

for i in range(2):
	image_filtered = cv2.bilateralFilter(image_filtered, 3, 40, 5)

# Sharpening the image using addWeighted()
gaussian_mask= cv2.GaussianBlur(image_filtered, (7,7), 2)
image_sharp = cv2.addWeighted(image_filtered, 1.5, gaussian_mask, -0.5, 0)
image_sharp = cv2.addWeighted(image_sharp, 1.4, gaussian_mask, -0.2, 10)

# Displayng the Images
cv2.imshow('Water Color art', image_sharp)
cv2.imshow('Clear impurities', image_cleared)
cv2.imshow('Original Image', image_resized)
cv2.waitKey(0)