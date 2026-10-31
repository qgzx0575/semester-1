# Program to invert image pixels
# (Illustrates how to use the Image class from Session 2)

import sys
from image import Image

# Check command line to see if filenames have been specified

if len(sys.argv) != 3:
    sys.exit("Usage: python invert.py <input-image> <output-image>")

# Create an image from data in the file named on the command line

img = Image.read(sys.argv[1])

num_pixels = img.width * img.height

# Invert pixel values
# (Can address pixels linearly here - don't need to use row & column)

for i in range(num_pixels):
    img[i] = img.max_value - img[i]

# Write inverted image to the specified file

img.write_pgm(sys.argv[2])


# If you didn't want to modify the image in place, you could
# generate the output in new Image object, like this:
#
# inverted_img = Image.create(img.width, img.height)
#
# for i in range(num_pixels):
#     inverted_img[i] = img.max_value - img[i]
