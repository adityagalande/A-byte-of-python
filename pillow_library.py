# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 23:12:53 2021

@author: Aditya Galande
"""

from PIL import Image
import glob

img = Image.open("aditya.jpg")
usa_img = Image.open("images/usa.png")
canada_img = Image.open("images/canada.png")
ind_img = Image.open("images/india.png")

######## This is re-sizing image ##########
print(type(img))
print(img.mode)
print(img.size)

#it compress(squeeze) not crop
small_img = img.resize((300, 600))
small_img.save("images/test_small_img2.jpg")

#it make exact image of 200, 300 px not squeeze
img.thumbnail((200, 300))
img.save("images/test_tmnail.jpg")

######## This is croping image ##########

#cropped_img = img.crop((0,0, 100, 100))
#cropped_img.save("images/cropped_img.jpg")

######## This is copying and pasting image ##########

#usa_img.thumbnail((50, 50))
#usa_img.save("images/usa_tmnail.png")
usa_tmnail = Image.open("images/usa_tmnail.png")
img_copy = img.copy()
img_copy.paste(usa_tmnail, (50, 50))
img_copy.save("images/copy_img.jpg")

#Rotate image
img130 = usa_img.rotate(130, expand=True)
img130.save("images/img130.png")

#flip image

flipB = img.transpose(Image.FLIP_TOP_BOTTOM)
flipB.save("images/flipped_bottom_img.jpg")

flipL = img.transpose(Image.FLIP_LEFT_RIGHT)
flipL.save("images/flipped_LR_img.jpg")

#grey image

grey_img = ind_img.convert("L")
grey_img.save("images/india_grey_img.jpg")

path = "images/flags/*"

for file in glob.glob(path):
    print(file)
    a = Image.open(file)
    rotatef45 = a.rotate(45, expand=True)
    rotatef45.save(file+"_rotated.png", "PNG")






