# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 10:08:31 2023

@author: danie
"""

# Load packages
import cv2
import matplotlib.pyplot as plt
from skimage.exposure import equalize_adapthist
import numpy as np
from skimage.filters import (threshold_otsu)
import scipy.ndimage as snd
from keras.preprocessing import image




import numpy as np
data = np.load('"D:/Research/Project_GlialTopology/3.DataAnalysis\GlialScarTDA-20230405T201941Z-001/GlialScarTDA/results_npy/M02_30D_TDA.npy"')




# Reading image and converting it into an ndarray
Image1 = cv2.imread('F:/Daniel/Project_PericyteReactivity/2.Images/Exp1-Gfap,Iba1/10x/Images_Tiff/Td21_14D_MCAO_Peri_Pdgfr.tif', 0)

plt.figure(figsize = (10,10)) # To determine Image size
plt.imshow(Image1, cmap='gray')
plt.axis ('off') # To hide ticklabes
plt.show ()



## Applying filter

img2 = equalize_adapthist(Image1, clip_limit = 0.02)
# Rescaling img2 from 0 to 255.
Image2_Adaptative = img2*255.0
# Saving img3.
cv2.imwrite('..Adaptative_Enhance.png', Image2_Adaptative)
# Displaying c1
plt.figure(figsize = (10,10)) # To determine Image size
plt.imshow(Image2_Adaptative, cmap='gray')
plt.axis('off')
plt.show


img = image.img_to_array( = img2*255.0
, dtype='uint8')
Adaptative_Segmentation = cv2.adaptiveThreshold(Image2_Adaptative,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

##5 Otsu
PDGFR_Array = numpy.asarray(Image2_Adaptative)
thresh = threshold_otsu(PDGFR_Array)
# Pixels with intensity greater than the "threshold" are kept.
PDGFR_Otsu = 255*(PDGFR_Array > thresh)

# Displaying Gfap_Otsu image
plt.figure(figsize = (10,10)) # To determine Image size
plt.title("binary_sauvola", fontsize=30, pad=20) # To determine Tile and padding
plt.imshow(PDGFR_Otsu, cmap='gray')
plt.axis('off')
plt.show


PDGFR_Array = np.array(PDGFR_Otsu)
# Performing binary dilation for 5 iterations.
PDGFR_Dilation = snd.morphology.binary_dilation(PDGFR_Array, iterations=5)

plt.figure(figsize = (10,10)) # To determine Image size
plt.imshow(PDGFR_Dilation, cmap='gray')
plt.axis('off')
plt.show