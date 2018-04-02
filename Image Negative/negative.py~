from PIL import Image
import cv2
import sys
import numpy as np

S = 255

# if in rgb
if(sys.argv[2]=="rgb"):
    # open in rgb
    img = cv2.imread(sys.argv[1],cv2.IMREAD_COLOR)    
    B,G,R = cv2.split(img)
    B[:] = [S-x for x in B]     #inverting blue
    G[:] = [S-x for x in G]     #inverting green    
    R[:] = [S-x for x in R]     #inverting red

    #saving image
    my_img = cv2.merge((B, G, R)) 
    cv2.imwrite(sys.argv[1]+'_inverted.png', my_img)
    cv2.imshow(sys.argv[1]+'_inverted.png', my_img)     

#if in grayscale or binary
else:    
    # open in grayscale
    img = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE) 
    my_img = np.array([S-x for x in img])
    cv2.imwrite(sys.argv[1]+'_inverted.png', my_img)
    cv2.imshow(sys.argv[1]+'_inverted.png', my_img) 
     





