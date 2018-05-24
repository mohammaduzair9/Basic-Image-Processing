import cv2
import numpy as np
from matplotlib import pyplot as plt
import copy

plt.figure(figsize=(12,12))
#reading image from file
im = cv2.imread("inp3.tif", 0).astype(np.float)
#function for median filtering
def medianFiltering(img, filterSize):
    #making deep copy of image
    filteredImg = copy.deepcopy(img)
    #calculating padding size
    paddingSize = filterSize/2
    #padding the image
    filteredImg = np.pad(filteredImg, (paddingSize, paddingSize), 'constant', constant_values=(0))
    #loop through image pixels
    for row in range(paddingSize, filteredImg.shape[0]-paddingSize):
        for col in range(paddingSize, filteredImg.shape[1]-paddingSize):
            kernal = []
            for x_filter in xrange(filterSize):
                for y_filter in xrange(filterSize):
                    kernal.append(filteredImg[row+x_filter-paddingSize][col+y_filter-paddingSize])
            #calculating median of list
            filteredImg[row,col] = np.median(kernal)
    #removing zero padding 
    filteredImg = filteredImg[paddingSize:filteredImg.shape[0]-paddingSize, paddingSize:filteredImg.shape[1]-paddingSize]
    return filteredImg

size = int(raw_input("> Enter the size of median filter: "))
#applying meadian filtering on image
output = medianFiltering(im, filterSize=size)
#writing file to image file
cv2.imwrite("median.jpg",output)
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