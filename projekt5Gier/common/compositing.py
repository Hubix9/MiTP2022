from common.ppmReader import Image
from copy import deepcopy

transparentColor = [255, 255, 255]


# Overlay imageB on top of imageA at coordinates x,y coordinates start from top left corner
def overlayImages(imageA: Image, imageB: Image, start_x: int, start_y: int) -> Image:
    if imageB.width + start_x > imageA.width or imageB.height + start_y > imageA.height:
        raise ValueError("Images cannot be overlaid, coordinates out of bounds")
    if start_x < 0 or start_y < 0:
        raise ValueError("Start coordinates cannot be below 0")

    outputImage = deepcopy(imageA)
    for y in range(0, imageB.height, 1):
        for x in range(0, imageB.width, 1):

            if not imageB.pixels[y][x] == transparentColor:
                outputImage.pixels[start_y + y][start_x + x] = imageB.pixels[y][x]

    return outputImage
