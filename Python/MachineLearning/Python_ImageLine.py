from PIL import Image, ImageFilter
from PIL import ImageEnhance
import matplotlib.pyplot as plt

image = Image.open("EMT - 02.jpg");

##
plt.subplot(1,3,1) # ORG
plt.title("image-ORG")
plt.imshow(image)

# Converting the image to greyscale
imageX = image.convert("L")

### Method 01
image01 = imageX.filter(ImageFilter.FIND_EDGES)

##
plt.subplot(2,3,1) 
plt.title("M-01")
plt.imshow(image01)

### Method 02 - laplican Kernel
image02 = imageX.filter(ImageFilter.Kernel(
            (3, 3), 
            (-1, -1, -1, -1, 8, -1, -1, -1, -1), 
            1, 0))

##
plt.subplot(1,3,3) 
plt.title("M-02")
plt.imshow(image02)

###
plt.show()