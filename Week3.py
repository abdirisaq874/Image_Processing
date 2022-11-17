import cv2
import numpy as np
import sys
import cv2 as cv

# image_with_2D_convolution_part 

image = cv2.imread('image.jpg')

kernel1 = np.ones((5,5),np.float32)

img = cv2.filter2D(src=image,ddepth=-1,kernel=kernel1)
cv2.imshow('Original',image)
cv2.imshow('Kernel Blur',img)


cv2.waitKey()




# Averaging_Filter_mask (smoothing) 

path='image.jpg'
img = cv2.imread(path)

im1 = cv2.blur(img,(5,5))
im2 =cv2.boxFilter(img,-1,(2,2),normalize=True)

cv2.imshow('image',np.hstack((im1,im2)))
cv2.waitKey(0)
cv2.destroyAllWindows
cv2.waitKey(1)


# Non_linear_filter 

img = cv2.imread('image.jpg')

median = cv2.medianBlur(img,5)
compare = np.concatenate((img,median),axis=1)

cv2.imshow('img',compare)
cv2.waitKey(0)


#Laplace_operator

def main(argv):
    ddepth = cv.Cv_165
    kernel_size = 3
    window_name = "Laplace Demo"

    imageName = argv[0] if len(argv)>0 else 'image.jpg'

    src =cv.imread(cv.samples.findFile(imageName),cv.IMREAD_COLOR)

    if src is None:
        print('Error opening image')
        print('Program Arguments:[image_name -- default image.jpg]')
        return -1


    src = cv.GaussianBlur(src,(3,3),0)

    src_gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY)

    cv.namedWindow(window_name,cv.WINDOW_AUTOSIZE)

    dst = cv.Laplacian(src_gray,ddepth,ksize=kernel_size)


    abs_dst= cv.convertScaledAbs(dst)

    cv.imshow(window_name,abs_dst)
    cv.waitKey(0)

    return 0

if __name__=="_main_":
    main(sys.argv[1:])
