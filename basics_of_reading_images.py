# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 17:40:38 2021

@author: Aditya Galande

About images READING (manipulation)
"""

import numpy as np
from skimage import io
from matplotlib import pyplot as plt
from PIL import Image

#To read the image
myImage = io.imread("aditya.jpg")

#To show image
plt.imshow(myImage);

#To save image
plt.imsave("my_image_2.jpg", myImage)

#To make image RGB tinted
tintedImg = myImage * [0., 0., 1.]
plt.imshow(tintedImg)


#To create random image with numpy
randomImg = np.random.random([500,500])

plt.imsave("randomImg.png", randomImg)


img = Image.open("aditya.jpg")
print(type(img))
#img.show()

#It tells img format for this (JPEG)
print(img.format)


#Convert image into numpy array
img1 = np.asarray(img)
print(type(img1))
#O/P
#<class 'numpy.ndarray'>

#######################################################
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

image = mpimg.imread("aditya.jpg")
#It show img in plot
plt.imshow(image)
#It show img with color bar
plt.colorbar()


#######################################################
from skimage import io

imageIO = io.imread("aditya.jpg")
plt.imshow(imageIO)

#######################################################
import cv2
from matplotlib import pyplot as plt

greyImg = cv2.imread("aditya.jpg", 0)
cv2.imshow("Grey_IMG", greyImg)

cv2.waitKey(0)
cv2.destroyAllWindows()








