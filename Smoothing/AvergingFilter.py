import cv2
import numpy as np
from matplotlib import pyplot as plt
from Filter import applyFilter

plt.figure(figsize=(12,12))

#reading image from file
im = cv2.imread("inp1.tif", 0).astype(np.float)

size = int(raw_input("> Enter the size of averaging filter: "))
#applying filter on image
output = applyFilter(im, filterSize=size)

#writing image to image file
cv2.imwrite("averaging.jpg",output)

#plotting original image
plt.subplot(211)
plt.axis('off')
plt.title("Original Image")
plt.imshow(im, cmap="gray")

#plotting smoothed image
plt.subplot(212)
plt.axis('off')
plt.title("Smoothed Image (avg. filter"+str(size)+"x"+str(size)+")")
plt.imshow(output, cmap="gray")

plt.show()