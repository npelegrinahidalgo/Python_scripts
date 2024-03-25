#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 22:04:41 2022

@author: pele

What does this script do?

(1) Calculate tvec values from beads files and adds them to table
(2) Table tvec used for translation of SR data 
(3) Return mapped SR image as .tif and FitResults as .txt


"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from sklearn.cluster import DBSCAN
from skimage import filters,measure
import cv2
from numpy import unravel_index
import imreg_dft as ird
from skimage import io
from statistics import mean


# Settings
image_height=512
image_width=512
Pixel_size=103
scale=8
precision_threshold=250
eps_threshold=0.5
minimum_locs_threshold=15
prec_thresh=40



# Directs to GDSCSMLM files of beads
pathlist_beads = r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/Beads/Test_2024-02-16_14-01-07/Processed images/"
beads_green=r'/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/Beads/Test_2024-02-16_14-01-07/X0Y0R1W1_515_0.tif'
beads_red=r'/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/Beads/Test_2024-02-16_14-01-07/X0Y0R1W1_638_0.tif'


# Images to correct afterwards
# Select either SR or DL correction
SR_correction=1



# Red file to be corrected- must be either tiff (for DL) or fitresults (for SR)
filename_contains_ch2="515_0_FitResults.txt"

pathlist=[]

# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/A2_NoEVs+D6G4AB(2nM)+nB(6nM)+E2285(1nM)+NR(5nM)_2024-02-16_15-04-42/Processed images/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/A2_NoEVs+D6G4AB(2nM)+nB(6nM)+E2285(1nM)_2024-02-16_14-38-34/Processed images/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/B2+D6G4AB(2nM)+nB(6nM)+E2285(1nM)+NR(5nM)_2024-02-16_15-22-12/Processed images/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/B2+D6G4AB(5nM)+nB(15nM)+D7674(1nM)+NR(5nM)_2024-02-16_19-00-33/Processed images/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/B3+UE3R2AB(2nM)+nB(6nM)+D7674(1nM)+NR(5nM)_2024-02-16_18-02-44/Processed images/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/B4+D6G4AB(2nM)+AF647+NR(5nM)_2024-02-16_16-47-47/Processed images/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/C2+D6G4AB(2nM)+nB(6nM)+E2285(1nM)+NR(5nM)_2024-02-16_15-47-51/Processed images/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/A3+UE3R2AB(2nM)+nB(6nM)+D7674(1nM)+NR(5nM)_2024-02-16_20-40-14/Processed images/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/C2+D6G4AB(5nM)+nB(15nM)+D7674(1nM)+NR(5nM)_2024-02-16_19-44-36/Processed images/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/C3+UE3R2AB(2nM)+nB(6nM)+D7674(1nM)+NR(5nM)_2024-02-16_18-18-46/Processed images/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/C4+D6G4AB(2nM)+AF647+NR(5nM)_2024-02-16_17-40-43/Processed images/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/Beads/Test_2024-02-16_14-01-07/Processed images/")

tag_515 = "515"

tag_638 = "638"

def generate_SR(coords):
    SR_plot_def=np.zeros((image_height*scale,image_width*scale),dtype=float)
    j=0
    for i in coords:
        
        xcoord=coords[j,0]
        ycoord=coords[j,1]
        scale_xcoord=round(xcoord*scale)
        scale_ycoord=round(ycoord*scale)
        # if(scale_xcoord<image_height and scale_ycoord<image_width):
        SR_plot_def[scale_ycoord,scale_xcoord]+=1
        
        j+=1
        
    return SR_plot_def


imgG = io.imread(beads_green)
imgR = io.imread(beads_red)


# Extract the final frame of the bead data (final frame used to reduce risk of saturation skewing result)
redSlice = imgR[imgR.shape[0] - 1].astype('float32')
greenSlice = imgG[imgG.shape[0] - 1].astype('float32')

# Load beads DL data --> perform translation and then use tvec (translation shift values) to correct each exWAGO image
result = ird.similarity(redSlice, greenSlice, numiter=5)

tvec_dic = result["tvec"]

tvec_0 = float(tvec_dic[0])
tvec_1 = float(tvec_dic[1])

        

                        

for path in pathlist:
    print(path)
    
    check_file = os.path.join(path,"X0Y0R3W3_638_0_SR.tif")
    
    if os.path.isfile(check_file):
        
        rows = range(1,4)
        wells = range(1,4)
    else:
        
        rows = range(1,3)
        wells = range(1,3)
    
    for row in rows:
        
        for well in wells:
            
            FOV = "X0Y0R" + str(row) + "W" + str(well) + "_"
            
            filename_contains_ch2= FOV + "515_0_FitResults.txt"

            
            if SR_correction==1:
                for root, dirs, files in os.walk(path):
                        for name in files:
                                if filename_contains_ch2 in name:
                                    if "._" not in name:
                        
                                        resultsname = name
                                        print(resultsname)
                                            
                # This is the file to load for channel 2
                fits_path=path+resultsname
                loc_data=pd.read_table(fits_path)
                
                coords= np.array(list(zip(loc_data['X'],loc_data['Y'])))
            
                xcoords=np.array(loc_data['X'])
                ycoords=np.array(loc_data['Y'])
                
                modified_xcoords=xcoords+tvec_1
                modified_xcoords_rounded = np.around(modified_xcoords, decimals = 3)
                modified_ycoords=ycoords+tvec_0
                modified_ycoords_rounded = np.around(modified_ycoords, decimals = 3)
        
                
            
                
                modified_coords=np.array(list(zip(modified_xcoords,modified_ycoords)))
                SR_modified=generate_SR(modified_coords)
                imsr = Image.fromarray(SR_modified)
                imsr.save(path + str(FOV) +'515_mapped_SR.tif')
                
                loc_data_modified=loc_data
                loc_data_modified['X']=modified_xcoords_rounded
                loc_data_modified['Y']=modified_ycoords_rounded
                
                loc_data_modified.to_csv(path+ str(FOV) + '515_mapped_FitResults.txt', sep = '\t', index=False)


    