import cv2
import numpy as np

img = cv2.imread('inp.jpg',0)

ret,bin = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

kernel = np.ones((3,3),np.uint8)
opened = cv2.morphologyEx(bin, cv2.MORPH_OPEN, kernel)
cv2.imshow("opened", opened)

kernel = np.ones((5,5),np.uint8)
closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)
ret, output = cv2.threshold(closed,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow("segment", output)
cv2.imwrite("segment.png", output)
cv2.waitKey(0)
