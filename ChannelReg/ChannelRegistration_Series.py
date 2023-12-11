#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Purpose: uses tetraspeck beads to align multi-channel images.
"""


# USER INPUTS ####################

# Provide file paths to Tetraspeck green and red channels:
beads_green=r'/Volumes/RSaleeb_2TB/20231121_RS_NB_Preincubation_Test2/Beads_green.tif'
beads_red=r'/Volumes/RSaleeb_2TB/20231121_RS_NB_Preincubation_Test2/Beads_red.tif'

# Provide path to dataset to be aligned (whch contains a subfolder per condition within which are all FOVs, channels are in separate files)
dirPath = r'/Volumes/RSaleeb_2TB/20231121_RS_NB_Preincubation_Test2/Analysis/'

# Filename identifiers of channels to be mapped:
green_ID='SR_Render.tif'
red_ID='AF647_Scaled.tif'



# MAIN CODE ######################

# Import required libraries
import numpy as np
import os
from skimage import io
import imreg_dft as ird
import imageio


# Load the bead image files:
imgR = io.imread(beads_red)
imgG = io.imread(beads_green)

# Extract the final frame of the bead data (final frame used to reduce risk of saturation skewing result)
redSlice = imgR[imgR.shape[0] - 1].astype('uint16')
greenSlice = imgG[imgG.shape[0] - 1].astype('uint16')

# Compute the transformation required for image registration using the imreg_dft package (Christoph Gohlke, https://pypi.org/project/imreg_dft/)
result = ird.similarity(redSlice, greenSlice, numiter=5)

# Create a list of all data folders to be aligned
folderList = os.listdir(dirPath)

# For each folder, create a list of all files to be aligned
for folder in folderList:
    if not folder == '.DS_Store':
        fileList = os.listdir(dirPath + folder)

        # Parse filename (relevant to ONI Nanoimager filename formats, should be edited for other filename patterns)
        root = fileList[1]
        namePrefix = root[0 : root.index("posXY") + 5]
        nameSuffix = root[root.index("_channels") : root.index("posZ0_") + 6]
        
        # Count 
        fileList = os.listdir(dirPath + folder)
        FOV_Num = 0
        for file in fileList:
            if file.endswith(green_ID):
                FOV_Num = FOV_Num + 1
        
        # For each FOV
        for number in range(0, FOV_Num):
                
                print(namePrefix + str(number) + nameSuffix + green_ID)
                
                # Load image to be transformed
                data_green = io.imread(dirPath + folder + "/" + namePrefix + str(number) + nameSuffix + green_ID).astype('uint16')
                
                # Create an empty image array matching the dimensions of the loaded image
                newresult = np.empty((data_green.shape[0], data_green.shape[1], data_green.shape[2])).astype('uint16')
                
                # For each frame of the data, apply the computed image translation and load into the empty image array
                for i in range(data_green.shape[0]):
                    newresult[i]=ird.transform_img_dict(data_green[i], result, bgval=None, order=1, invert=False).astype('uint16')
                
                # Save the translated output
                imageio.mimwrite(dirPath + folder + "/" + namePrefix + str(number) + nameSuffix + green_ID[0:green_ID.index(".tif")] + '-trans.tif', newresult)
    
print("Image registration complete.")

