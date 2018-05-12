import cv2
from matplotlib import pyplot as plt

def xycut(image, image_path):
    # reading image
    img = plt.imread(image_path)
    fig, ax = plt.subplots()
    ax.imshow(img)

    black_pix = []
    white_lines = []
    # detecting the white lines
    for i in range(0, bin_img.shape[0]):
        # if number of white phixels in row is greater than 750
        if (bin_img[i].sum() / 255 > 750):

            # draw horizontal lines
            ax.axhline(y=i, color='green')
        else:
            # black pixels on x-axis
            for j in range(0, bin_img.shape[1]):
                if (bin_img[i][j] == 0):
                    black_pix.append(j)

    if len(black_pix) != 0:
        # draw first & last vertical line only
        ax.axvline(x=min(black_pix), linewidth=3, color='green')
        ax.axvline(x=max(black_pix), linewidth=3, color='green')

    # remove the axis
    ax.set_axis_off()
    # saving new figure
    plt.savefig('xycut.png', bbox_inches='tight')
    # show the figure
    plt.show()


# load image as greyscale
image = cv2.imread("XY-cuts.png", 0)
# binarize image
(_, bin_img) = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
# call xycut function
xycut(bin_img, "XY-cuts.png")
