# Program to compute the mean value of image pixels
# (Illustrates how to use the Image class from Session 2)

import sys
from image import Image

# Check command line to see if a filename has been specified

if len(sys.argv) != 2:
    sys.exit("Usage: python mean_value.py <image-file>")

# Create an image from data in the file named on the command line

img = Image.read(sys.argv[1])

num_pixels = img.width * img.height

# We can address pixels individually using nested for loops that
# iterate over row and column coordinates:

total = 0
for row in range(img.height):
    for col in range(img.width):
        total += img.get(row, col)

print(total / (img.width * img.height))

# This version of Image also allows linear indexing:

total = 0
for i in range(num_pixels):
    total += img[i]

print(total / num_pixels)

# We can fetch pixel values without having to index:

total = 0
for value in img:
    total += value

print(total / num_pixels)

# We can even avoid the loop, because built-in function sum()
# can compute a sum over anything we can iterate over!

print(sum(img) / num_pixels)
