#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 13:28:34 2023

@author: pele

Script to analyse EV data (NR & DNA-PAINT) coincidence in clustered data (using NR as mask)

"""
import warnings
import os
from skimage.io import imread
from PIL import Image
import matplotlib.pyplot as plt
from skimage import color, io
from skimage.filters import try_all_threshold, threshold_otsu
import numpy as np
from tabulate import tabulate
import pandas as pd
import cv2


warningDisabled = True


if warningDisabled:
    warnings.simplefilter(action='ignore', category=FutureWarning)


root_path = r"/Volumes/Noe PhD 4/Microscopes/ONI/20240112_NPH_PLL_EVs_D6G4_50%lasers/"

# inpaths to analyse
pathlist=[]

pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/ONI/20240112_NPH_PLL_EVs_D6G4_50%lasers/A4+500pM_NR+1nM_E2285/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/ONI/20240112_NPH_PLL_EVs_D6G4_50%lasers/B3+500pM_NR+1nM_E2285/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/ONI/20240112_NPH_PLL_EVs_D6G4_50%lasers/C3+500pM_NR+1nM_E2285/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/ONI/20240112_NPH_PLL_EVs_D6G4_50%lasers/A3+500pM_NR+1nM_E2285/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/ONI/20240112_NPH_PLL_EVs_D6G4_50%lasers/B4+500pM_NR+1nM_E2285/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/ONI/20240112_NPH_PLL_EVs_D6G4_50%lasers/C4+500pM_NR+1nM_E2285/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20240112_NPH_PLL_EVs_D6G4_50%lasers/C3_only/")


folder_NR = "1_5_NR_DBSCAN/"
folder_DNAPAINT = "1_1_exWAGO_DBSCAN/"


image_name_NR = "1_5NRSR_fwhm_python_clustered.tif"

image_name_DNAPAINT = "1_1exWAGOSR_fwhm_python_clustered.tif"

Coincidence_table = pd.DataFrame(columns=["File", "Coincidence value"])




def load_image(toload):
    image=imread(toload)
    return image
    


for path in pathlist:
    
    print(path)
    
    for i in range(0,9):
  
        path_within = path + 'pos_' + str(i) + '/'
        
        print(path_within)
            
        # Define paths for both images:
    
        NR_path = path_within + folder_NR + image_name_NR
        
        PAINT_path = path_within + folder_DNAPAINT + image_name_DNAPAINT
        
        # Load NR image and mask it (average + 2* std formula):
            
        NR = load_image(NR_path)
        plt.imshow(NR, vmin = 0, vmax = 0.2)
        plt.title("NR")
        plt.axis('off')
        plt.show()
        
        
        NR_ave = NR.mean()
        NR_std = NR.std()
        
        NR_mask = NR > NR_ave +  2 * NR_std
        
        # Load DNA-PAINT image:
            
        PAINT = load_image(PAINT_path)
        plt.imshow(PAINT, vmin = 0, vmax = 0.2)
        plt.title("DNA-PAINT raw")
        plt.axis('off')
        plt.show()    
        
        coincidence_result = cv2.bitwise_and(NR, PAINT)
        

        
        # Calculate coincidence:
            
        Coincidence = PAINT * NR_mask
        plt.imshow(Coincidence, vmin = 0, vmax = 0.2)
        plt.title("Coincidence")
        plt.axis('off')
        plt.show()
        
        binary_coinc = Coincidence/PAINT
        
        if coincidence_result.all() ==  Coincidence.all():
            
            print("True")
        
        total_coincidence = sum(sum(Coincidence))
        
        # Save coincidence image (so it can be opened in Fiji)
            
        coincidence_saved = Image.fromarray(Coincidence)
        coincidence_saved.save(path_within + str("Coincidence_.tif"))
        
        # Add coincidence value to table
        
        Coincidence_table = Coincidence_table.append({"File":path_within, "Coincidence": str(total_coincidence)},ignore_index=True)
        
Coincidence_table.to_csv(root_path + "clusters_coincidence.csv", sep = "\t")




















