#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:47:36 2023

@author: pele


Purpose: uses tetraspeck beads to align multi-channel images.


"""


# USER INPUTS ####################

# Provide file paths to Tetraspeck green and red channels:
beads_green=r'/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/Beads/Test_2024-02-16_14-01-07/X0Y0R1W1_515_0.tif'
beads_red=r'/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/Beads/Test_2024-02-16_14-01-07/X0Y0R1W1_638_0.tif'

# Provide path to dataset to be aligned (whch contains a subfolder per condition within which are all FOVs, channels are in separate files)

pathlist=[]

# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/A2_NoEVs+D6G4AB(2nM)+nB(6nM)+E2285(1nM)+NR(5nM)_2024-02-16_15-04-42/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/A2_NoEVs+D6G4AB(2nM)+nB(6nM)+E2285(1nM)_2024-02-16_14-38-34/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/B2+D6G4AB(2nM)+nB(6nM)+E2285(1nM)+NR(5nM)_2024-02-16_15-22-12/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/B2+D6G4AB(5nM)+nB(15nM)+D7674(1nM)+NR(5nM)_2024-02-16_19-00-33/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/B3+UE3R2AB(2nM)+nB(6nM)+D7674(1nM)+NR(5nM)_2024-02-16_18-02-44/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/B4+D6G4AB(2nM)+AF647+NR(5nM)_2024-02-16_16-47-47/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/C2+D6G4AB(2nM)+nB(6nM)+E2285(1nM)+NR(5nM)_2024-02-16_15-47-51/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/A3+UE3R2AB(2nM)+nB(6nM)+D7674(1nM)+NR(5nM)_2024-02-16_20-40-14/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/C2+D6G4AB(5nM)+nB(15nM)+D7674(1nM)+NR(5nM)_2024-02-16_19-44-36/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/C3+UE3R2AB(2nM)+nB(6nM)+D7674(1nM)+NR(5nM)_2024-02-16_18-18-46/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/C4+D6G4AB(2nM)+AF647+NR(5nM)_2024-02-16_17-40-43/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/Beads/Test_2024-02-16_14-01-07/")



# Filename identifiers of channels to be mapped:
green_ID='515_0_DL.tif'
red_ID='638_0_DL.tif'


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
imgG = io.imread(beads_green)
imgR = io.imread(beads_red)


# Extract the final frame of the bead data (final frame used to reduce risk of saturation skewing result)
redSlice = imgR[imgR.shape[0] - 1].astype('float32')
greenSlice = imgG[imgG.shape[0] - 1].astype('float32')

# Compute the transformation required for image registration using the imreg_dft package (Christoph Gohlke, https://pypi.org/project/imreg_dft/)
result = ird.similarity(redSlice, greenSlice, numiter=5)


# For each folder, create a list of all files to be aligned

for path in pathlist:
    
    img_folder = path + "Processed images/"
    
    for root, dirs, files in os.walk(img_folder): 
        
        if len(files) > 53:
            
            rows = range(1,4)
            wells = range(1,4)
        
        else:
            
            rows = range(1,3)
            wells = range(1,3)
    
    for row in rows:
        
        for well in wells:
            
            FOV = "X0Y0R" + str(row) + "W" + str(well) + "_"
            
            in_path = img_folder + FOV
            
            if os.path.exists(in_path + green_ID):
                    
                data_green = io.imread(in_path + green_ID).astype('float32')
                newresult = ird.transform_img_dict(data_green, result, bgval=None, order=1, invert=False).astype('float32')
                im = Image.fromarray(newresult)
                im.save(in_path + '515_DL_mapped.tif')
                
            print("X0Y0R" + str(row) + "W" + str(well) + "done")
            
    print(path + " done")
    
print("Image registration complete.")
