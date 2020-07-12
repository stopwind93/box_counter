# Box_Counter

Use computer vision techniques to count the number of boxes in the image.
![alt text](https://github.com/stopwind93/box_counter/blob/master/Table.JPG?raw=true)

## Steps
### 1) Import Libraries
- cv2
- numpy
- matplotlib

### 2) Import raw file & convert to grayscale
Reduce information for each pixel.

### 3) Convert Grayscale to Binary
Convert grayscale to binary based on thresholding algorithm.

### 4) Find Contour Using Binary Image
2 Contour Feature Extraction are used:  
Contour Approximation whereby vertices = 4  
Contour Perimeter whereby perimeter more than 80 but less than 1000  

### 5) Plot Detected Boxes

## Conclusion
Number of detected boxes: 53
