from PIL import Image
from PIL import ImageEnhance
import matplotlib.pyplot as plt

image = Image.open("Image - 02.png");
##
plt.subplot(2,3,1) # ORG
plt.title("image-ORG")
plt.imshow(image)

enh_bri = ImageEnhance.Brightness(image)
brightness = 1.5
image_brightened = enh_bri.enhance(brightness)
##
plt.subplot(2,3,2) # image_brightened
plt.title("image_brightened")
plt.imshow(image_brightened)

enh_col = ImageEnhance.Color(image)
color = 5
image_colored = enh_col.enhance(color)
##
plt.subplot(2,3,3) # image_colored
plt.title("image_colored")
plt.imshow(image_colored)


enh_con = ImageEnhance.Contrast(image)
contrast = 5
image_contrasted = enh_con.enhance(contrast)
##
plt.subplot(2,3,5) # image_contrasted
plt.title("image_contrasted")
plt.imshow(image_contrasted)


enh_sha = ImageEnhance.Sharpness(image)
sharpness = 5.0
image_sharped = enh_sha.enhance(sharpness)
##
plt.subplot(2,3,6) # image_sharped
plt.title("image_sharped")
plt.imshow(image_sharped)

###
plt.show()