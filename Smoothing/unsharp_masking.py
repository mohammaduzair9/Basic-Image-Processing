import cv2
import numpy as np
from matplotlib import pyplot as plt
import copy
from Filter import applyFilter

plt.figure(figsize=(12,12))
#reading image from file
im = cv2.imread("inp2.tif", 0).astype(np.float)

#function for unsharp masking
def unsharpMasking(img):
    inputImg = copy.deepcopy(img)
    blurredImg = applyFilter(inputImg, filterSize=5)
    mask = inputImg - blurredImg
    result = inputImg + mask
    return result
#unsharp masking the image
output = unsharpMasking(im)
#writing image to image file
cv2.imwrite("unsharp_masking.jpg",output)
#plotting original image
plt.subplot(211)
plt.axis('off')
plt.title("Original Image")
plt.imshow(im, cmap="gray")
#plotting transformed image
plt.subplot(212)
plt.axis('off')
plt.title("Transformed Image")
plt.imshow(output, cmap="gray")

plt.show()