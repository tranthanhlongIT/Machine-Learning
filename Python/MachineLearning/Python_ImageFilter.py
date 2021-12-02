import numpy as np
import scipy.ndimage as nd
from skimage import data, morphology, filters as imfilter
import cv2
import matplotlib.pyplot as plt
from PIL import Image

img = data.coins()


### 
flevel = 5
# scipy
dst = np.zeros(img.shape, img.dtype)
for i in range(img.shape[2]):
    dst[:, :, i] = nd.median_filter(img[:, :, i], flevel)

# opencv
dst = cv2.medianBlur(img, 5)

# show IMGs
plt.subplot(2,2,1) #
plt.imshow(img)
plt.subplot(2,2,2) #
plt.imshow(dst)
plt.show()