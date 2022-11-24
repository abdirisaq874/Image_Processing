import random
import cv2
import matplotlib.pyplot as plt

def addingNoise(image):
    row, col = image.shape
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        image[y_coord][x_coord] = 255
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        image[y_coord][x_coord] = 0

    return image


image = cv2.imread('/Users/mandeez/Downloads/my info/06.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imwrite('/Users/mandeez/Downloads/my info/04.jpg',addingNoise(image))

#  Histogram Displayment
print(image)
print(image.ravel())
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.hist(image.ravel(), 256, [0, 256])
plt.title('Histogram of the  paper and salt picture')
plt.show()
