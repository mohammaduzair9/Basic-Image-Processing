# Basic Digital Image Processing Tasks
> This repository contains basic implementations of image processing algorithms in python.

## Required Libraries
*	PIL
```shell
$ pip install pillow
```
*	opencv-python
```shell
$ pip install opencv-python
```

## Algorithms

### Gradient

```shell
$ python gradient.py
```
|Original|Gradient|
|---|---|
|![Gradient-Original](https://github.com/mohammaduzair9/Basic-Digital-Image-Processing/blob/master/Gradient/lena.jpg)|![Gradient-Result](https://github.com/mohammaduzair9/Basic-Digital-Image-Processing/blob/master/Gradient/gradient.jpg)|

### Image Negative

```shell
$ python negative.py binary.jpeg binary
```
|Original|Binary Negative|
|---|---|
|![Binary-Negative-Original](https://github.com/mohammaduzair9/Basic-Digital-Image-Processing/blob/master/Image%20Negative/binary.jpg)|![Binary-Negative-Result](https://github.com/mohammaduzair9/Basic-Digital-Image-Processing/blob/master/Image%20Negative/binary_inverted.png)|

```shell
$ python negative.py lena.jpg gray
```
|Original|Grayscale Negative|
|---|---|
|![Gray-Negative-Original](https://github.com/mohammaduzair9/Basic-Digital-Image-Processing/blob/master/Image%20Negative/grayscale.png)|![Gray-Negative-Result](https://github.com/mohammaduzair9/Basic-Digital-Image-Processing/blob/master/Image%20Negative/grayscale_inverted.png)|


```shell
$ python negative.py lena.jpg rgb
```
|Original|RGB Negative|
|---|---|
|![Rgb-Negative-Original](https://github.com/mohammaduzair9/Basic-Digital-Image-Processing/blob/master/Image%20Negative/rgb.jpg)|![Rgb-Negative-Result](https://github.com/mohammaduzair9/Basic-Digital-Image-Processing/blob/master/Image%20Negative/rgb_inverted.png)|

### Image Segmentation

```shell
$ python Segmentation.py
```
|Original|Segmented|
|---|---|
|![Segmented-Original](https://github.com/mohammaduzair9/Basic-Digital-Image-Processing/blob/master/Image%20Segmentation/image.png)|![Segmented-Result](https://github.com/mohammaduzair9/Basic-Digital-Image-Processing/blob/master/Image%20Segmentation/Capture3.PNG)|

### Centroid

```shell
$ python Centroid.py
```
|Original|Centroid|
|---|---|
|![Centroid-Original](https://github.com/mohammaduzair9/Basic-Digital-Image-Processing/blob/master/Centroid/Signature.png)|<table><tr><td>Top Left</td><td>Top Right</td></tr><tr><td>![Centroid-TopLeft](https://github.com/mohammaduzair9/Basic-Digital-Image-Processing/blob/master/Centroid/TopLeft.png)</td><td>![Centroid-TopRight](https://github.com/mohammaduzair9/Basic-Digital-Image-Processing/blob/master/Centroid/TopRight.png)</td></tr><tr><td>Bottom Left</td><td>Bottom Right</td></tr><tr><td>![Centroid-BottomLeft](https://github.com/mohammaduzair9/Basic-Digital-Image-Processing/blob/master/Centroid/BottomLeft.png)</td><td>![Centroid-BottomRight](https://github.com/mohammaduzair9/Basic-Digital-Image-Processing/blob/master/Centroid/BottomRight.png)</td></tr></table>|

### Connected Component Labelling
### Histogram Equalization
### Local Histogram Analysis
### Morphology
### Sharpening
### Skeletonization
### Smoothing
### XY Cuts

