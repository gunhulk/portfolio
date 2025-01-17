# -*- coding: utf-8 -*-
"""Lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L6-ENvCQzt9nhCuEmeUo30kgaOVlmpcv
"""

from google.colab import drive
drive.mount("/content/drive", force_remount=True)
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy as np
numPixels = 0
numRed = 0
numGreen = 0
numBlue = 0
grandSequence = []

im = Image.open("/content/drive/My Drive/Pictures/download.jpg").convert("RGB")

# split the image into individual channels
channel = im.split()

channelR = channel[0]
channelG = channel[1]
channelB = channel[2]

red = channelR.histogram()
green = channelG.histogram()
blue = channelB.histogram()

print("TOTAL:")
for i in range(len(red)):
  numPixels = numPixels + red[i]
print(numPixels)

sequenceRed = []
print("RED RED RED---------------------------------------------------:")
for r in range(len(red)):
 PR = numRed/numPixels
 print("RED frequencies:")
 print(PR)
 NR = PR * 255
 sequenceRed.append(NR)
 print("RED new value:")
 print(NR)
 numRed = numRed + red[r]

sequenceGreen = []
print("GREEN GREEN GREEN----------------------------------------------:")
for g in range(len(green)):
 PG = numGreen/numPixels
 print("GREEN frequency:")
 print(PG)
 NG = PG * 255
 sequenceGreen.append(NG)
 print("GREEN new value:")
 print(NG)
 numGreen = numGreen + green[g]
 



sequenceBlue = []
print("BLUE BLUE BLUE-------------------------------------------------:")
for b in range(len(blue)):
      rowcol = (row,col)
      PB = numBlue/numPixels
      print("BLUE frequency:")
      print(PB)
      NB = PB * 255
      sequenceBlue.append(NB)
      print("BLUE new value:")
      print(NB)
      numBlue = numBlue + blue[b]


grandSequence.extend(sequenceRed)
grandSequence.extend(sequenceGreen)
grandSequence.extend(sequenceBlue)
print(grandSequence)
print(len(grandSequence))
newim = im.point(grandSequence)
newim

from google.colab import drive
drive.mount('/content/drive')