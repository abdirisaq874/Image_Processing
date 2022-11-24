import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 


def NPhoto(photo):
    L=np.max(photo)
    NPhoto=L-photo
    return NPhoto

img = cv.imread("/Users/mandeez/Downloads/my info/06.jpg")

NPhoto= NPhoto(img)
Aside = np.hstack((img, NPhoto))
print("original photo:",img.shape)
print("negative photo:",NPhoto.shape)
print("Aside:", Aside.shape)

plt.imshow(Aside,cmap="gray")
plt.show()
