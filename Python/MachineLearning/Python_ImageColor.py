import matplotlib.pyplot as plt
from PIL import Image
org_im = Image.open('Image - 01.png')
im = org_im.copy()
pix = im.load()
cols,rows = im.size

#look at every single pixel and if red turn it to gray
for r in range(rows):
    for c in range(cols):
        if (pix[c,r] == (0,255,0) or pix[c,r] == (0,0,255)): #if pixel is red
            pix[c,r] = (255,255,255) #set it gray

# show IMGs
plt.subplot(1,2,1) # ORG
plt.imshow(org_im)
plt.subplot(1,2,2) # replace RED "img"
plt.imshow(im)
plt.show()