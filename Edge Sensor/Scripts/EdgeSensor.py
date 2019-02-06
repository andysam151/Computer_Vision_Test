'''
this program takes an image and creates an outline of its edges. While it works with all pictures, it functions best
with black and white images with high contrast. The output will be in black and white.
'''

import numpy
from PIL import Image

im = Image.open('C:/Users/andys/Documents/Programming/IDE Workspace/Python/Edge Sensor/test images/anime3.jpg') #put in location of input file
im = im.convert('1') #changes to black and white image
data = numpy.zeros((im.size[0], im.size[1], 3), dtype=numpy.uint8)
pix = im.load()
x = 2
y = 2
pixtl = 0
pixl = 0
pixbl = 0
pixtr = 0
pixr = 0
pixbr = 0
pixt = 0
pixb = 0
totr = 0

while x < im.size[0] - 1:
    while y < im.size[1] - 1: #loops through each pixel in the image
        pixtl = pix[(x - 1), (y - 1)] #bw value of the top left pixel adjacent to the pixel being looked at

        pixl = pix[(x - 1), y] #bw value of the left pixel adjacent to the pixel being looked at

        pixbl = pix[(x - 1), (y + 1)] #bw value of the bottom left pixel adjacent to the pixel being looked at

        pixtr = pix[(x + 1), (y - 1)] #bw value of the top right pixel adjacent to the pixel being looked at

        pixr = pix[(x + 1), y] #bw value of the right pixel adjacent to the pixel being looked at

        pixbr = pix[(x + 1), (y + 1)] #bw value of the bottom right pixel adjacent to the pixel being looked at

        totr = abs(pixtl + pixl + pixbl - pixtr - pixr - pixbr) #finds contrast between left and right sides

        data[x, y] = (255-totr, 255-totr, 255-totr) #new bw value for the pixel

        y += 1
    y = 2
    x += 2
image = Image.fromarray(data)
image.save('C:/Users/andys/Documents/Programming/IDE Workspace/Python/Edge Sensor/edges.jpg') #outline output
im.save('C:/Users/andys/Documents/Programming/IDE Workspace/Python/Edge Sensor/edges mono.jpg') #saves imput as black and white to another file
