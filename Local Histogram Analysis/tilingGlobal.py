from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread('mountains.jpg',0)
intensity_count = [0] * 256         #Initialize intensity values with 256 zeroes
L = 255.0

in1 = [0] * 256
in2 = [0] * 256
in3 = [0] * 256
in4 = [0] * 256

height, width = img.shape[:2]        #Get width and height
N = height * width * 1.0                 #Get total Pixels
half_height, half_width = height/2, width/2
half_N = (N / 2) * 1.0

im1 = np.zeros((256,256,0))
im2 = np.zeros((256,256,0))
im3 = np.zeros((256,256,0))
im4 = np.zeros((256,256,0))
high_contrast = np.zeros(img.shape)         #Array for global_equalized_new_image
high_contrast_local = np.zeros(img.shape)   #Array for local_equalized_new_image

for y in range(0, height):
    for x in range(0, width): 
        intensity_count[img[y,x]] += 1          #Increment each gray_level pixel value according to tile (tile 1, 2, 3 or 4)
        if y <= height/2 and x < width/2:
            in1[img[y,x]] += 1
        elif y <= height/2 and x >= width/2:
            in2[img[y,x]] += 1
        elif y > height/2 and x < width/2:
            in3[img[y,x]] += 1
        elif y > height/2 and x >= width/2:
            in4[img[y,x]] += 1

newList1 = [x / half_N for x in in1]
newList2 = [x / half_N for x in in2]
newList3 = [x / half_N for x in in3]
newList4 = [x / half_N for x in in4]

pdf1_array = np.asarray(newList1); cdf1_array = np.cumsum(pdf1_array)
pdf2_array = np.asarray(newList1); cdf2_array = np.cumsum(pdf2_array)
pdf3_array = np.asarray(newList1); cdf3_array = np.cumsum(pdf3_array)
pdf4_array = np.asarray(newList1); cdf4_array = np.cumsum(pdf4_array)

approx1_List = [round(x * L) for x in cdf1_array]
approx2_List = [round(x * L) for x in cdf2_array]
approx3_List = [round(x * L) for x in cdf3_array]
approx4_List = [round(x * L) for x in cdf4_array]

for y in range(0, height):
    for x in range(0, width): 
        if y <= height/2 and x < width/2:
            high_contrast_local[y,x] = approx1_List[img[y,x]]
        elif y <= height/2 and x >= width/2:
            high_contrast_local[y,x] = approx2_List[img[y,x]]
        elif y > height/2 and x < width/2:
            high_contrast_local[y,x] = approx3_List[img[y,x]]
        elif y > height/2 and x >= width/2:
            high_contrast_local[y,x] = approx4_List[img[y,x]]

cv2.imwrite('high_contrast_local.png', high_contrast_local)

newList = [x / N for x in intensity_count]

pdf_array = np.asarray(newList)
cdf_array = np.cumsum(pdf_array)

approx_List = [round(x * L) for x in cdf_array]

for y in range(0,height):
    for x in range(0,width):
        high_contrast[y,x] = approx_List[img[y,x]] 

plt.hist(high_contrast_local.ravel(),256,[0,256])
plt.xlabel('Intensity Values')
plt.ylabel('Pixel Count')
plt.savefig('high_contrast_local.png')
plt.clf()
#plt.show()


cv2.imwrite('high_contrast_global.png', high_contrast)                         #PLOT THE HISTOGRAMS
plt.hist(img.ravel(),256,[0,256])
plt.xlabel('Intensity Values')
plt.ylabel('Pixel Count')
plt.savefig('Original.png')
plt.clf()
#plt.show()
plt.hist(high_contrast.ravel(),256,[0,256])
plt.xlabel('Intensity Values')
plt.ylabel('Pixel Count')
plt.savefig('high_contrast_global.png')
plt.clf()
#plt.show()


