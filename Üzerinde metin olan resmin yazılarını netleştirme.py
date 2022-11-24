import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 

img = cv.imread("/Users/mandeez/Downloads/my info/06.jpg")


cv.imshow('Original Image', img)
cv.waitKey(0)


Sh_img = cv.filter2D(img, -1,np.array([[1,1,1],[1,-9,1],[1,1,1]]))

cv.imshow('Sharpened Image', Sh_img)
cv.waitKey(0)
cv.destroyAllWindows()
