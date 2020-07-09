import cv2
import numpy as np
from matplotlib import pyplot as plt

src = "Table.JPG"
img = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
#bw = cv2.adaptiveThreshold(item, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 15)
_, bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findCoutours(bw, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

boxes = list()
for contour in contours:
	epsilon = 0.001 * cv2.arcLength(contour, True)
	approx = cv2.approxPolyDP(contour, epsilon, True)
	if len (approx) == 4 and 80< cv2.arcLength(contour, True) < 1000:
		boxes.append(approx)
		
print("Number of detected boxes: {}".format(len(boxes))) #Number of detected rectangles according to criteria
img = cv2.imread(src,cv2.IMREAD_ANYCOLOR)
for box in boxes:
	cv2.drawContours(img, [box], 0, (0,255,0), 1)
	
height, width, channels = img.shape
dpi_rand = 300
plt.figure(figsize=(width*3/dpi_rand, height*3/dpi_rand), dpi=dpi_rand)
plt.imshow(img, cmap='Greys_r')
plt.show