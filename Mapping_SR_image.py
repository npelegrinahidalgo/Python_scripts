#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 22:04:41 2022

@author: pele
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
image_height=684
image_width=428
Pixel_size=117
scale=8
precision_threshold=250
eps_threshold=0.5
minimum_locs_threshold=15
prec_thresh=40

to_save_beads = r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/"


# Directs to GDSCSMLM files of beads
pathlist_beads = []


pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/Beads_post-mapping/pos_0/")
pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/Beads_post-mapping/pos_1/")
pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/Beads_post-mapping/pos_2/")
pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/Beads_post-mapping/pos_3/")
pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/Beads_post-mapping/pos_4/")
pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/Beads_post-mapping/pos_5/")
pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/Beads_post-mapping/pos_6/")
pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/Beads_post-mapping/pos_7/")
pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/Beads_post-mapping/pos_8/")

# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_0/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_1/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_10/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_11/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_12/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_13/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_14/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_15/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_16/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_17/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_18/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_19/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_2/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_20/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_21/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_22/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_23/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_24/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_3/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_4/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_5/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_6/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_7/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_8/")
# pathlist_beads.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/Beads/pos_9/")




bead_file_green="green_FitResults.txt"
bead_file_red="red_FitResults.txt"

translation_values = pd.DataFrame(columns = ["0", "1"])

# Images to correct afterwards
# Select either SR or DL correction
SR_correction=1
DL_correction=0


# Red file to be corrected- must be either tiff (for DL) or fitresults (for SR)
filename_contains_ch2="red_projection.tif"

pathlist=[]


pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/C3_500pM_NR+1nM_E2285-1/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/C3_500pM_NR+1nM_E2285-1/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/C3_500pM_NR+1nM_E2285-1/pos_10/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/C3_500pM_NR+1nM_E2285-1/pos_11/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/C3_500pM_NR+1nM_E2285-1/pos_12/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/C3_500pM_NR+1nM_E2285-1/pos_13/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/C3_500pM_NR+1nM_E2285-1/pos_14/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/C3_500pM_NR+1nM_E2285-1/pos_15/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/C3_500pM_NR+1nM_E2285-1/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/C3_500pM_NR+1nM_E2285-1/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/C3_500pM_NR+1nM_E2285-1/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/C3_500pM_NR+1nM_E2285-1/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/C3_500pM_NR+1nM_E2285-1/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/C3_500pM_NR+1nM_E2285-1/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/C3_500pM_NR+1nM_E2285-1/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/C3_500pM_NR+1nM_E2285-1/pos_9/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A5_500pM_NR+1nM_E2285/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A5_500pM_NR+1nM_E2285/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A5_500pM_NR+1nM_E2285-1/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A5_500pM_NR+1nM_E2285-1/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A5_500pM_NR+1nM_E2285-1/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A5_500pM_NR+1nM_E2285-1/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A5_500pM_NR+1nM_E2285-1/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A5_500pM_NR+1nM_E2285-1/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A5_500pM_NR+1nM_E2285-1/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A5_500pM_NR+1nM_E2285-1/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A5_500pM_NR+1nM_E2285-1/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/B5_500pM_NR+1nM_E2285/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/B5_500pM_NR+1nM_E2285/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/B5_500pM_NR+1nM_E2285/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/B5_500pM_NR+1nM_E2285/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/B5_500pM_NR+1nM_E2285/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/B5_500pM_NR+1nM_E2285/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/B5_500pM_NR+1nM_E2285/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/B5_500pM_NR+1nM_E2285/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/B5_500pM_NR+1nM_E2285/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A4_500pM_NR+1nM_E2285/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A4_500pM_NR+1nM_E2285/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A4_500pM_NR+1nM_E2285/pos_10/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A4_500pM_NR+1nM_E2285/pos_11/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A4_500pM_NR+1nM_E2285/pos_12/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A4_500pM_NR+1nM_E2285/pos_13/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A4_500pM_NR+1nM_E2285/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A4_500pM_NR+1nM_E2285/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A4_500pM_NR+1nM_E2285/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A4_500pM_NR+1nM_E2285/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A4_500pM_NR+1nM_E2285/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A4_500pM_NR+1nM_E2285/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A4_500pM_NR+1nM_E2285/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230417_Test_SiMPull_EVs(20230414)/A4_500pM_NR+1nM_E2285/pos_9/")




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



# Load beads SR data --> perform translation and then use tvec (translation shift values) to correct each exWAGO image

for bead_path in pathlist_beads:
        
    
    bead_data_green=pd.read_table(bead_path+bead_file_green)
    bead_data_red=pd.read_table(bead_path+bead_file_red)
    
    coords_green= np.array(list(zip(bead_data_green['X'],bead_data_green['Y'])))
    precsx_green= np.array(bead_data_green['Precision (nm)'])
    precsy_green= np.array(bead_data_green['Precision (nm)'])
    xcoords_green=np.array(bead_data_green['X'])
    ycoords_green=np.array(bead_data_green['Y'])
    
    # Generate points SR (ESMB method):
    SR_green=generate_SR(coords_green)
    
    coords_red= np.array(list(zip(bead_data_red['X'],bead_data_red['Y'])))
    precsx_red= np.array(bead_data_red['Precision (nm)'])
    precsy_red= np.array(bead_data_red['Precision (nm)'])
    xcoords_red=np.array(bead_data_red['X'])
    ycoords_red=np.array(bead_data_red['Y'])
    
    # Generate points SR (ESMB method):
    SR_red=generate_SR(coords_red)
    
    
    # Perform the translation
    result = ird.translation(SR_green, SR_red)
    tvec = result["tvec"].round(4)
    
    tvec_0 = float(tvec[0])
    tvec_1 = float(tvec[1])
    
    translation_values = translation_values.append({"0": tvec_0, "1": tvec_1}, ignore_index=True)
    
    # Apply to old image of red beads
    translated_Red=ird.transform_img(SR_red, tvec=tvec)
    
    
    # Now need to apply to localisations that were loaded:
        
    unscaled_tvec=tvec/scale
    modified_xcoords_red=xcoords_red+unscaled_tvec[1]
    modified_ycoords_red=ycoords_red+unscaled_tvec[0]
    modified_coords_red=np.array(list(zip(modified_xcoords_red,modified_ycoords_red)))
    SR_red_modified=generate_SR(modified_coords_red)
    
    bead_data_red_modified=bead_data_red
    bead_data_red_modified['X']=modified_xcoords_red
    bead_data_red_modified['Y']=modified_ycoords_red
    


translation_values.loc['mean'] = translation_values.mean()    

translation_values.to_csv(to_save_beads + "tvec_table.csv", sep="\t")


unscaled_tvec_ave = translation_values.loc['mean']/scale
                               

# for path in pathlist:
#     print(path)
    
#     if SR_correction==1:
#         for root, dirs, files in os.walk(path):
#                 for name in files:
#                         if filename_contains_ch2 in name:
#                             if "._" not in name:
                                
                
#                                     resultsname = name
#                                     print(resultsname)
                                    
#         # This is the file to load for channel 2
#         fits_path=path+resultsname
#         loc_data=pd.read_table(fits_path)
        
#         coords= np.array(list(zip(loc_data['X'],loc_data['Y'])))
    
#         xcoords=np.array(loc_data['X'])
#         ycoords=np.array(loc_data['Y'])
        
#         modified_xcoords=xcoords+unscaled_tvec_ave[1]
#         modified_xcoords_rounded = np.around(modified_xcoords, decimals = 3)
#         modified_ycoords=ycoords+unscaled_tvec_ave[0]
#         modified_ycoords_rounded = np.around(modified_ycoords, decimals = 3)

        
    
        
#         modified_coords=np.array(list(zip(modified_xcoords,modified_ycoords)))
#         SR_modified=generate_SR(modified_coords)
#         imsr = Image.fromarray(SR_modified)
#         imsr.save(path+'exWAGO_ave_mapped_SR.tif')
        
#         loc_data_modified=loc_data
#         loc_data_modified['X']=modified_xcoords_rounded
#         loc_data_modified['Y']=modified_ycoords_rounded
        
#         loc_data_modified.to_csv(path + 'exWAGO_ave_mapped_FitResults.txt', sep = '\t', index=False)
        
#     if DL_correction==1:
#         img_to_convert = io.imread(path+filename_contains_ch2).astype('int')
       
#         translated=ird.transform_img(img_to_convert, tvec=unscaled_tvec).astype('uint16')
        
#         imsr = Image.fromarray(translated)
#         imsr.save(path+'Translated_red_DL.tif')

    