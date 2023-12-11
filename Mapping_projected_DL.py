#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:47:36 2023

@author: pele
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Purpose: uses tetraspeck beads to align multi-channel images.
"""


# USER INPUTS ####################

# Provide file paths to Tetraspeck green and red channels:
beads_green=r'/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_3/561_cropped.tif'
beads_red=r'/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_3/638_cropped.tif'

# Provide path to dataset to be aligned (whch contains a subfolder per condition within which are all FOVs, channels are in separate files)

pathlist=[]


pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_10/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_11/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_12/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_13/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_14/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_15/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_16/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_17/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_18/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_19/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_20/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_21/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_22/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_23/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_24/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_9/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_10/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_11/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_12/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_13/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_14/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_15/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_16/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_17/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_18/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_19/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_20/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_21/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_22/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_23/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_24/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_9/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_10/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_11/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_12/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_13/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_14/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_15/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_16/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_17/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_18/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_19/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_20/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_21/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_22/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_23/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_24/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_9/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_10/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_11/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_12/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_13/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_14/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_15/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_16/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_17/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_18/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_19/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_20/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_21/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_22/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_23/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_24/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_9/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_10/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_11/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_12/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_13/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_14/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_15/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_16/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_17/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_18/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_19/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_20/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_21/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_22/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_23/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_24/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_9/")

# Filename identifiers of channels to be mapped:
green_ID='561_cropped.tif'
red_ID='638_cropped.tif'



# MAIN CODE ######################

# Import required libraries
import numpy as np
np.bool = np.bool_
import os
from skimage import io
import imreg_dft as ird
import imageio
from PIL import Image


# Load the bead image files:
imgR = io.imread(beads_red)
imgG = io.imread(beads_green)

# Extract the final frame of the bead data (final frame used to reduce risk of saturation skewing result)
redSlice = imgR.astype('float32')
greenSlice = imgG.astype('float32')

# Compute the transformation required for image registration using the imreg_dft package (Christoph Gohlke, https://pypi.org/project/imreg_dft/)
result = ird.similarity(redSlice, greenSlice, numiter=5)


# For each folder, create a list of all files to be aligned

for path in pathlist:
    
    data_green = io.imread(path + green_ID).astype('float32')
    newresult = ird.transform_img_dict(data_green, result, bgval=None, order=1, invert=False).astype('float32')
    im = Image.fromarray(newresult)
    im.save(path + '561_mapped.tif')
    
    
print("Image registration complete.")
