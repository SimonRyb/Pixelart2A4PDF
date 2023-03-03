#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image, ImageEnhance

# Variable to base downscaling on, width of image
BasePixel = 30

# Open the input image
im = Image.open("bild7.jpg")
width, height = im.size
print('Old dimentions')
print('width: ',width)
print('height: ',height)
print('factor: ',(width/height))
print('new width: ',int(BasePixel*(width/height)))
print('new height: ',BasePixel)

# Resize the image to the desired pixel size
im = im.resize((BasePixel,(int(BasePixel*(height/width)))), Image.BILINEAR)


# Create an ImageEnhance object for the contrast
contrast = ImageEnhance.Contrast(im)

# Apply the contrast enhancement
im = contrast.enhance(1.5)

# Save the pixelated image
im.save("output_image.jpg")