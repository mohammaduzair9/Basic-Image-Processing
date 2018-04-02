from PIL import Image
import cv2
import numpy as np

#Read Image in GrayScale
img_gray = cv2.imread('lena.jpg',0)               
h,w = img_gray.shape[:2]

grad_img = np.asarray(img_gray)

for i in range(0,h):
    for j in range(0,w-1):

        #applying gradient
	a = min(img_gray[i][j+1],img_gray[i][j])
	if a == img_gray[i][j+1] :
 		temp_arr = img_gray[i][j] - img_gray[i][j+1]
	else :
		temp_arr = img_gray[i][j+1] - img_gray[i][j]
        
        
        grad_img[i,j] = temp_arr

img = Image.fromarray(grad_img)                              
img.save("gradient.jpg")

