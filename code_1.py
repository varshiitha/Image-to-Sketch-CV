import cv2
import numpy as np

# Read input image
img = cv2.imread('d.jpg')

# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert grayscale image
inverted_gray_img = 255 - gray_img

# Apply Gaussian blur
blurred_img = cv2.GaussianBlur(inverted_gray_img, (21, 21), 0)

# Invert blurred image
inverted_blurred_img = 255 - blurred_img

# Create a pencil sketch image by blending the inverted blurred image with the grayscale image
pencil_sketch_img = cv2.divide(gray_img, inverted_blurred_img, scale=256.0)

# Show input and sketch images side by side
cv2.imshow('Input Image', img)
cv2.imshow('Pencil Sketch', pencil_sketch_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
