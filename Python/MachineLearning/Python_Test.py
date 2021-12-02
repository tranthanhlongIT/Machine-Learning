#ID: Trần Thành Long - 2199121
#Picture: b-002
#Algorithm: Laplacian + Prewitt Filter

from PIL import Image, ImageFilter
from PIL import ImageEnhance
from scipy import ndimage, misc
import matplotlib.pyplot as plt
from skimage import data,color,filters
import numpy as np
import cv2 as cv

### Open image for filter
image = Image.open("b-001.jpg");

### Open image for histogram
img01 = cv.imread('b-001.jpg',0)

### Open image for binary + threshold
img02 = cv.imread('b-001.jpg',cv.IMREAD_COLOR) 

### HISTOGRAM
# Find frequency of pixels in range 0-255
histr = cv.calcHist([img01],[0],None,[256],[0,256])

### GREYSCALE
# Converting the image to greyscale
imageX = image.convert("L")

### LAPLACIAN + PREWITT FILTER
# Laplican Kernel
image01 = imageX.filter(ImageFilter.Kernel(
            (3, 3), 
            (-1, -1, -1, -1, 8, -1, -1, -1, -1), 
            1, 0))

# Prewitt Kernel
image02 = filters.prewitt(imageX)    

# Laplican + Prewitt Kernel
image03 = filters.prewitt(image01)

### BINARY + THRESHOLD
# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale 
img03 = cv.cvtColor(img02, cv.COLOR_BGR2GRAY)

# Applying different thresholding 
# all pixels value above 120 will be set to 255
ret, thresh1 = cv.threshold(img03, 120, 255, cv.THRESH_BINARY_INV)

### SHOW ORGINAL IMAGE
plt.subplot(4,4,1) 
plt.title("Original Image")
plt.imshow(image)

# SHOW HISTOGRAM OF THE IMAGE
plt.subplot(4,4,2)
plt.title("OI - Histogram")
plt.plot(histr)

### SHOW GREYSCALE IMAGE
plt.subplot(4,4,3) 
plt.title("Greyscale Image")
plt.imshow(imageX, cmap='gray')

### SHOW IMAGE WITH LAPLACIAN FILTER
plt.subplot(4,4,9)
plt.title("Image With Laplican Filter")
plt.imshow(image01)

### SHOW IMAGE WITH PREWITT FILTER
plt.subplot(4,4,10)
plt.title("Image With Prewitt Filter")
plt.imshow(image02)

### SHOW IMAGE WITH LAPLACIAN AND PREWITT FILTER
plt.subplot(4,4,11)
plt.title("Image With Laplican and Prewitt Filter")
plt.imshow(image03)

### SHOW BINARY AND TRHESHOLD IMAGE
plt.subplot(4,4,12)
plt.title('Binary + Threshhold Image')
plt.imshow(thresh1, cmap="gray")

###
plt.show()