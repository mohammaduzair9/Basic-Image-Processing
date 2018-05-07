import cv2
import numpy as np

# Loading the image in RGB
img = cv2.imread("image.png", 0)

# Applying Gaussian blur with kernel size 7 to remove unwanted noise
blurred_image = cv2.GaussianBlur(img,(7,7),0)

# Applying Otsu's thresholding to binarize the image
retval ,binarized_image = cv2.threshold(blurred_image,40,255,cv2.THRESH_BINARY)

# Applying Closing to fill in the holes
filter = np.ones((3,3),np.uint8)
closed_image = cv2.morphologyEx(binarized_image, cv2.MORPH_CLOSE, filter)

# Using connected components to label the image
retval, markers = cv2.connectedComponents(closed_image)

# Mapping the component labels to hue val
label_hue = np.uint8(120*markers/np.max(markers))
blank_ch = 255*np.ones_like(label_hue)
labeled_image = cv2.merge([label_hue, blank_ch, blank_ch])

# changing from HSV to RGB again to show
labeled_image = cv2.cvtColor(labeled_image, cv2.COLOR_HSV2BGR)

# background label set to black
labeled_image[label_hue==0] = 0

# getting the unique colors in the image
unique_colors = np.unique(labeled_image.reshape(-1, labeled_image.shape[2]), axis=0)

print "Colors available in labeled image:"
for x in xrange(unique_colors.shape[0]):
    print str(x+1)+"=> B:"+str(unique_colors[x,0])+"    G:"+str(unique_colors[x,1])+"   R:"+str(unique_colors[x,2])+" "

print "\nSelect one of the colors and give its RGB values "

r = raw_input("B : ")
g = raw_input("G : ")
b = raw_input("R : ")

# making an output image
output_image = np.zeros_like(labeled_image)

# getting the object of user input color
for x in xrange(labeled_image.shape[0]):
    for y in xrange(labeled_image.shape[1]):
        if (labeled_image[x,y,0] == int(r) and labeled_image[x,y,1] == int(g) and labeled_image[x,y,2] == int(b)):
            output_image[x,y,0:3] = labeled_image[x,y,0:3]

# show the output image
cv2.imshow("Selected", labeled_image)
cv2.waitKey(0)
