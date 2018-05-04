import cv2
import numpy as np
from matplotlib import pyplot as plt
from Filter import applyFilter

plt.figure(figsize=(12,12))

im = cv2.imread("inp1.tif", 0).astype(np.float)

#creating gaussian filter 
gaussianFilter = np.array([[1,1,2,2,2,1,1],
                           [1,2,2,4,2,2,1],
                           [2,2,4,8,4,2,2],
                           [2,4,8,16,8,4,2],
                           [2,2,4,8,4,2,2],
                           [1,2,2,4,2,2,1],
                           [1,1,2,2,2,1,1]], np.float)
gaussianFilter /= np.sum(gaussianFilter*1.0)

#applying gaussian filter
output = applyFilter(im, imFilter=gaussianFilter)
#writing image to image file
cv2.imwrite("gaussian.jpg",output)
#plotting original image
plt.subplot(211)
plt.axis('off')
plt.title("Original Image")
plt.imshow(im, cmap="gray")

#plotting smoothed image 
plt.subplot(212)
plt.axis('off')
plt.title("Smoothed Image (gaussian filter7x7 (sigma 1.4))")
plt.imshow(output, cmap="gray")
plt.show()