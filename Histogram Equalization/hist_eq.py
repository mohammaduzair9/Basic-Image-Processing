from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread('hist2.tif',0)

#Initialize intensity values with 256 zeroes
intensity_count = [0] * 256         

height,width = img.shape[:2]        
N = height * width                  

	#Array for new_image
high_contrast = np.zeros(img.shape) 

for i in range(0,height):
    		for j in range(0,width):
        			intensity_count[img[i][j]] += 1     #Find pixels count for each intensity

L = 256

intensity_count,total_values_used = np.histogram(img.flatten(),L,[0,L])      
pdf_list = np.ceil(intensity_count*(L-1)/img.size)                    #Calculate PDF
cdf_list = pdf_list.cumsum()                                            	#Calculate CDF


for y in range(0, height):
    		for x in range(0, width): 
			#Apply the new intensities in our new image
        			high_contrast[y,x] = cdf_list[img[y,x]]                         

	
#PLOT THE HISTOGRAMS
cv2.imwrite('high_contrast.png', high_contrast)                         

plt.hist(img.ravel(),256,[0,256])
plt.xlabel('Intensity Values')
plt.ylabel('Pixel Count')
plt.show()

plt.hist(high_contrast.ravel(),256,[0,256])	
plt.xlabel('Intensity Values')
plt.ylabel('Pixel Count')
plt.show()
