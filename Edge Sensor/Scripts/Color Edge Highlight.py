'''
this program takes an image and creates an outline of its edges. While it works with all pictures, it functions best
with black and white images with high contrast. The output will be in color.
'''

import numpy
from PIL import Image


def tracing (input_file, output_file, original_file, power):
    nim = Image.open(input_file)  # put in location of input file
    data = numpy.zeros((nim.size[0], nim.size[1], 3), dtype=numpy.uint8)
    pix = nim.load()

    x = 2
    y = 2

    while x < nim.size[0] - 2:
        while y < nim.size[1] - 2: #loops through each pixel in the image
            pixtl = pix[(x - 1), (y - 1)] #rgb value of the top left pixel adjacent to the pixel being looked at

            pixl = pix[(x - 1), y] #rgb value of the left pixel adjacent to the pixel being looked at

            pixbl = pix[(x - 1), (y + 1)] #rgb value of the bottom left pixel adjacent to the pixel being looked at

            pixtr = pix[(x + 1), (y - 1)] #rgb value of the top right pixel adjacent to the pixel being looked at

            pixr = pix[(x + 1), y] #rgb value of the right pixel adjacent to the pixel being looked at

            pixbr = pix[(x + 1), (y + 1)] #rgb value of the bottom right pixel adjacent to the pixel being looked at

            totr = abs(pixtl[0] + pixl[0] + pixbl[0] - pixtr[0] - pixr[0] - pixbr[0]) #finds contrast between left and right sides
            totg = abs(pixtl[1] + pixl[1] + pixbl[1] - pixtr[1] - pixr[1] - pixbr[1])
            totb = abs(pixtl[2] + pixl[2] + pixbl[2] - pixtr[2] - pixr[2] - pixbr[2])
            if (totr + totg + totb) == 0:
                pixt = pix[x, (y-1)]
                pixb = pix[x, (y+1)]
                totr = abs(pixtl[0] + pixt[0] + pixtr[0] - pixbr[0] - pixb[0] - pixbl[0])
                totg = abs(pixtl[1] + pixt[1] + pixtr[1] - pixbr[1] - pixb[1] - pixbl[1])
                totb = abs(pixtl[2] + pixt[2] + pixtr[2] - pixbr[2] - pixb[2] - pixbl[2])

            if (totr + totg + totb) > (675-power):
                data[x, y] = (255 - totr, 255 - totg, 255 - totb)  # new rgb value for the pixel
            else:
                data[x, y] = (255, 255, 255)

            y += 1
        y = 2
        x += 2
    image = Image.fromarray(data)
    image.mode = 'RGB'
    image.save(output_file)  # outline output
    nim.save(original_file)


test_image = 'C:/Users/andys/Documents/Programming/IDE Workspace/Python/Edge Sensor/test images/anime1.jpg'
deposit_image = 'C:/Users/andys/Documents/Programming/IDE Workspace/Python/Edge Sensor/edges color highlight.jpg'
comparison_image = 'C:/Users/andys/Documents/Programming/IDE Workspace/Python/Edge Sensor/Original Image.jpg'
intensity = 675
tracing(test_image, deposit_image, comparison_image, intensity)
