#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 11:05:21 2024

@author: pele

What does this script do?

- Calculate drift value (tvec) from DL beads image and apply to SR image


"""
import warnings
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
# from sklearn.cluster import DBSCAN
# from skimage import filters,measure
import cv2
from numpy import unravel_index
import imreg_dft as ird
from skimage import io
from statistics import mean

warningDisabled = True


# Settings
image_height=684
image_width=428
Pixel_size=117
scale=8
precision_threshold=250
eps_threshold=0.5
minimum_locs_threshold=15
prec_thresh=40


if warningDisabled:
    warnings.simplefilter(action='ignore', category=FutureWarning)

# Dataframes, lists, etc:
    
translation_values = pd.DataFrame()
pathlist_beads = []
pathlist=[]



pathlist_beads.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20240112_NPH_PLL_EVs_D6G4_30%lasers/Beads/")

"""
I am giving it specific positions instead of range() function because there are some positions
in this folder that are giving very extreme numbers in terms of mapping (i.e. tvec ratio)
"""
positions = ["1","3","4","5","6","7"]


bead_file_green="561_pre-cropped.tif"
bead_file_red="638_pre-cropped.tif"


# Images to correct afterwards
# Select either SR or DL correction
SR_correction=1
DL_correction=0


# Red file to be corrected- must be either tiff (for DL) or fitresults (for SR)
image_tag_to_correct = "exWAGO_FitResults.txt"


pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20240112_NPH_PLL_EVs_D6G4_50%lasers/A4+500pM_NR+1nM_E2285/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20240112_NPH_PLL_EVs_D6G4_50%lasers/B3+500pM_NR+1nM_E2285/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20240112_NPH_PLL_EVs_D6G4_50%lasers/C3+500pM_NR+1nM_E2285/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20240112_NPH_PLL_EVs_D6G4_50%lasers/A3+500pM_NR+1nM_E2285/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20240112_NPH_PLL_EVs_D6G4_50%lasers/B4+500pM_NR+1nM_E2285/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20240112_NPH_PLL_EVs_D6G4_50%lasers/C4+500pM_NR+1nM_E2285/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20240112_NPH_PLL_EVs_D6G4_50%lasers/C3_only/")




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


# Load beads DL data --> perform translation and then use tvec (translation shift values) to correct each exWAGO image

for bead_path in pathlist_beads:
    
    for i in range(1):
        
        bead_path_within = bead_path + 'pos_' + str(1) + '/'
        print(bead_path_within)
    
        green_path = bead_path_within + bead_file_green
        red_path = bead_path_within + bead_file_red
    
        
        # Load bead images file:
        green_img = io.imread(green_path)
        red_img = io.imread(red_path)
        
        result = ird.similarity(red_img, green_img, numiter=3)
        
        tvec_df = pd.DataFrame(result["tvec"]).transpose()
        
        translation_values = pd.concat([translation_values, tvec_df], axis = 0)
        
         
    translation_values.loc['mean'] = translation_values.mean()


# Identify translation values to be used for the mapping:

trans_val_dict = result
       

for path in pathlist:
    print(path)
    
    for i in range(0,9):
  
        path_within = path + 'pos_' + str(i) + '/'
        print(path_within)
        
        # Below the paths to the SR fitresults files:
            
        image_638 = path_within + image_tag_to_correct
    
        
        if SR_correction==1:
            
            # Dataframes to be used in the loop and need to be reset for each lap:
            modified_xcoords = pd.DataFrame()
            modified_ycoords = pd.DataFrame()
            
            # Load SR locs:
            fits_path=image_638
            loc_data=pd.read_table(fits_path)
            
            coords= np.array(list(zip(loc_data['X'],loc_data['Y'])))

                
            xcoords=np.array(loc_data['X'])
            ycoords=np.array(loc_data['Y'])
            modified_coords = pd.DataFrame(columns = ["X","Y"])
            
            # Scale up tvec (so it matches SR data-which is already scaled up)
            scaled_tvec = tvec_df * scale
            
            # Apply tvec values to each loc of the SR file (in x and y coordinates)
            for x in xcoords:
                
                modified_x = x + scaled_tvec[1]
                modified_xcoords_rounded = np.around(modified_x, decimals = 3)
                modified_xcoords = modified_xcoords.append(modified_xcoords_rounded)
                reindexed_mod_xcoords = modified_xcoords.reset_index(drop=True)
                
            for y in ycoords:
                
                modified_y = y + scaled_tvec[0]
                modified_ycoords_rounded = np.around(modified_y, decimals = 3)
                modified_ycoords = modified_ycoords.append( modified_ycoords_rounded)
                reindexed_mod_ycoords = modified_ycoords.reset_index(drop=True)
                
            # Add these corrected coords to the modified_coords table:
                
            modified_coords["X"] = reindexed_mod_xcoords.iloc[:,0]
            
            modified_coords["Y"] = reindexed_mod_ycoords.iloc[:,0]
            
            # Generate new SR image with corrected coords:
            
            # SR_modified=generate_SR(modified_coords)
            
            # # Save corrected image:
                
            # imsr = Image.fromarray(SR_modified)
            # imsr.save(path_within + image_tag_to_correct + '_mapped_SR.tif')

            # Convert image from corrected coords into locs file:
                
            loc_data_modified = loc_data
            loc_data_modified['X']=modified_coords["X"]
            loc_data_modified['Y']=modified_coords["Y"]
            
            # Save modified locs data:
                
            loc_data_modified.to_csv(path_within + 'mapped_' + image_tag_to_correct, sep = '\t', index=False)
        
        
            
            

        
        
        
            