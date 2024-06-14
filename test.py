import cv2
import numpy as np

# Load the image
image_path = 'assets/qr_code_alpha.png'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image to get a binary image
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# Find contours of white regions
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Extract coordinates of all white pixels
white_pixel_coords = []
for contour in contours:
    for point in contour:
        x, y = point[0]
        white_pixel_coords.append((x, y))

# Print or use the white pixel coordinates as needed
print("Coordinates of all white pixels:")
for coord in white_pixel_coords:
    print(coord)
