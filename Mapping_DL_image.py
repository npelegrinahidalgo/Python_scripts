#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:45:53 2023

@author: pele
"""

import matplotlib.image as mpimg
import numpy as np
import os
from skimage import io
import imreg_dft as ird
from PIL import Image
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu
import cv2


pathlist=[]

# This is the file that contains the beads for doing the image map:
beads_file=r'/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/beads/pos_1/NPH_PSMa3_StressMarq_beads_posXY1_channels_t0_posZ0.tif'


# Filename of images to map:
Filename='ThT_DL.tif'

# Paths to mapy

# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/PLL_ThT+2/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/PLL_ThT+2.5nM_PSM_+140nM_PFF2/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/PLL_ThT+2.5nM_PSM_+140nM_PFF2/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/PLL_ThT+2.5nM_PSM_+140nM_PFF2/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/PLL_ThT+2.5nM_PSM_+140nM_PFF2/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/ThT+2/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/ThT+2.5nM_PSM_+140nM_PFF2/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/ThT+500pM_PSM_+100nM_in-house/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/ThT+500pM_PSM_+100nM_in-house/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/ThT+500pM_PSM_+100nM_in-house/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/ThT+500pM_PSM_+100nM_in-house/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/ThT+500pM_PSM_+140nM_PFF1/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/ThT+500pM_PSM_+140nM_PFF1/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/ThT+500pM_PSM_+140nM_PFF1/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/ThT+500pM_PSM_+140nM_PFF1/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/ThT+500pM_PSM_+140nM_PFF1-1/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/ThT+500pM_PSM_+500nM_in-house/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/ThT+500pM_PSM_+500nM_in-house/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/ThT+500pM_PSM_+500nM_in-house/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/ThT+500pM_PSM_+500nM_in-house/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/ThT+5nM_PSM_+500nM_in-house/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/ThT+5nM_PSM_+500nM_in-house/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/ThT+5nM_PSM_+500nM_in-house/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/ThT+5nM_PSM_+500nM_in-house/pos_3/")




######## This is the bead mapping part ###########

# Load the image file:
img = io.imread(beads_file)

# Extract the red and green parts of the image (only looks at the first frame, which is fine for beads)         
greenSlice = (img[11,0:684,0:428]/255).astype(np.uint8)
redSlice = (img[0,0:684,428:856]/255).astype(np.uint8)

# Perform the image registration
result = ird.similarity(greenSlice, redSlice, numiter=3)
# result = ird.translation(greenSlice, redSlice)

# To look at the overlay- make binary
thr_ch1 = threshold_otsu(redSlice)
thr_ch2 = threshold_otsu(greenSlice)

binary_ch1 = redSlice > thr_ch1
binary_ch2 = greenSlice > thr_ch2

# Make an RGB image for overlay

imRGB = np.zeros((greenSlice.shape[0],greenSlice.shape[1],3))
imRGB[:,:,0] = binary_ch1
imRGB[:,:,1] = binary_ch2

fig, ax = plt.subplots(1,3, figsize=(14, 4))

ax[0].imshow(greenSlice,cmap='Greens_r')
ax[0].set_title('Green')
ax[1].imshow(redSlice,cmap='Reds_r');
ax[1].set_title('Red')
ax[2].imshow(imRGB)
ax[2].set_title('Overlay')


# Now show the transformed image

binary_ch2_transformed = result['timg'] > thr_ch2
imRGB_t = np.zeros((greenSlice.shape[0],greenSlice.shape[1],3))
imRGB_t[:,:,0] = binary_ch1
imRGB_t[:,:,1] = binary_ch2_transformed


fig, ax = plt.subplots(1,3, figsize=(14, 4))

ax[0].imshow(result['timg'],cmap='Greens_r')
ax[0].set_title('Green Transformed')
ax[1].imshow(redSlice,cmap='Reds_r');
ax[1].set_title('Red')
ax[2].imshow(imRGB_t)
ax[2].set_title('Transformed Overlay')



for path in pathlist:

    image_file=path+Filename

    # Load the image file:
    img_to_convert = io.imread(image_file)
    
    
    # Extract the red and green parts of the image         
    # greenSlice2 = (img_to_convert[0:256,0:512]).astype('uint16')
    # redSlice2 = (img_to_convert[256:512,0:512]).astype('uint16')
    
    newresult=ird.transform_img_dict(img_to_convert, result, bgval=None, order=1, invert=False).astype('uint16')
    
    im = Image.fromarray(newresult)
    im.save(path+'green_trans_beads_XY2_new.tif')
    
    im2 = Image.fromarray(img_to_convert)
    im2.save(path+'green.tif')
    
    # im3 = Image.fromarray(redSlice2)
    # im3.save(path+'red.tif')