import cv2 as cv
import numpy as np
from PIL import Image

img = cv.imread("/Users/mandeez/Downloads/my info/06.jpg")


def ChangingTheBit(input_file_path, pixel_size):
    image = Image.open(input_file_path)
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )
    image.show(title=str(pixel_size) + "Bit Image")


def GrayScaleToBit():
    bits = [8, 16, 24]
    imgPath = "/Users/mandeez/Downloads/my info/06.jpg"
    saveImgPath = "/Users/mandeez/Downloads/my info/07.jpg"

    Image.open(imgPath).convert('RGB').convert('L').save(saveImgPath)

    for index in range(3):
        ChangingTheBit(saveImgPath, bits[index])
    image = Image.open(saveImgPath)
    image.show()


GrayScaleToBit()
