import cv2
import numpy as np
from matplotlib import pyplot as plt
from Filter import applyFilter

plt.figure(figsize=(12,12))

#reading image from file
im = cv2.imread("inp1.tif", 0).astype(np.float)

#creating weighted filter:
#[1 2 1],
#[2 4 2],
#[1 2 1]
weightedFilter = (1.0/16)*np.array([[1,2,1],[2,4,2],[1,2,1]], np.int32)

#applying filter on image
output = applyFilter(im, imFilter=weightedFilter)

#writing image to image file
cv2.imwrite("weightedavg.jpg",output)

#plotting original image
plt.subplot(211)
plt.axis('off')
plt.title("Original Image")
plt.imshow(im, cmap="gray")

#plotting smoothed image
plt.subplot(212)
plt.axis('off')
plt.title("Smoothed Image (weighted avg. filter3x3)")
plt.imshow(output, cmap="gray")
plt.show()