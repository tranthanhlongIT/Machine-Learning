import cv2 
import numpy as np 
from matplotlib import pyplot as plt
# path to input image is specified and  
# image is loaded with imread command 
image1 = cv2.imread('Chipu.jpg') 
  
# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale 
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img,100,200)

# applying different thresholding 
# techniques on the input image
# all pixels value above 120 will 
# be set to 255
ret, thresh1 = cv2.threshold(edges, 120, 255, cv2.THRESH_BINARY_INV)
  
# the window showing output images
# with the corresponding thresholding 
# techniques applied to the input images


plt.subplot(1,3,1)
plt.imshow(img)
plt.title('Original Image')

plt.subplot(1,3,2)
plt.imshow(edges)
plt.title('Edge Image')
plt.subplot(1,3,3)
plt.imshow(thresh1,cmap="gray")
plt.title('Thresh + Edge Image')
plt.show()

# De-allocate any associated memory usage  
if cv2.waitKey(0) & 0xff == 27: 
    cv2.destroyAllWindows()