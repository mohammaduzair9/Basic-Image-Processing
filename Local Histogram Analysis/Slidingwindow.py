import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(12,12))

#reading image as grayscale
img = cv2.imread("mountains.jpg",0)

def slidingWindowEqualization(im, winSize):
    newImg = np.zeros((im.shape[0], im.shape[1]))
    for row in xrange(im.shape[0]-winSize+1):
        for col in xrange(im.shape[1]-winSize+1):
            newImg[row:row+winSize,col:col+winSize] = cv2.equalizeHist(im[row:row+winSize,col:col+winSize])
    return newImg

windowSize = 256
output_img = slidingWindowEqualization(img, windowSize)
plt.subplot(211)
plt.axis('off')
plt.title("Image after transformation")
plt.imshow(output_img, cmap="gray")

#writing output image
cv2.imwrite("SlidingWindow.jpg", output_img)

plt.subplot(212)
plt.hist(output_img.ravel(),256,[0,256])
plt.title("Histogram")

plt.show()

