#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 13:28:34 2023

@author: pele

Script to analyse EV data (NR & DNA-PAINT) coincidence in clustered data (using NR as mask)

"""

import os
from skimage.io import imread
from PIL import Image
import matplotlib.pyplot as plt
from skimage import color, io
from skimage.filters import try_all_threshold, threshold_otsu
import numpy as np
from tabulate import tabulate
import pandas as pd


root_path = r"/Volumes/Noe PhD 2/Microscopes/TIRFM/20230301_EVs_SiMPull/"
# inpaths to analyse
pathlist=[]



pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/TIRFM/20230301_EVs_SiMPull/A2_500pM_NR+1nM_E2285_2023-03-01_15-53-04/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/TIRFM/20230301_EVs_SiMPull/A3_1X_perm_only_2023-03-01_17-36-27/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/TIRFM/20230301_EVs_SiMPull/A3_1X_perm__500pM_NR+1nM_E2285_2023-03-01_17-41-37/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/TIRFM/20230301_EVs_SiMPull/B2_500pM_NR+1nM_E2285_2023-03-01_16-26-50/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/TIRFM/20230301_EVs_SiMPull/B2_only_2023-03-01_16-07-40/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/TIRFM/20230301_EVs_SiMPull/B3_10X_perm_500pM_NR+1nM_E2285_2023-03-01_17-04-28/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/TIRFM/20230301_EVs_SiMPull/B3_10X_perm_500pM_NR+2nM_E2285_2023-03-01_17-16-23/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/TIRFM/20230301_EVs_SiMPull/B3_10X_perm_only_2023-03-01_17-01-18/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/TIRFM/20230301_EVs_SiMPull/A3_1X_perm__500pM_NR+2nM_E2285_2023-03-01_17-52-54/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/TIRFM/20230301_EVs_SiMPull/A3_1X_perm__500pM_NR+2nM_E2285_2023-03-01_18-08-14/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/TIRFM/20230301_EVs_SiMPull/C2_500pM_NR+1nM_E2285_2023-03-01_16-56-39/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/TIRFM/20230301_EVs_SiMPull/C2_only_2023-03-01_16-47-46/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/TIRFM/20230301_EVs_SiMPull/B3_10X_perm__500pM_NR+5nM_E2285_2023-03-01_18-20-56/")



folder_NR = "1_5EVs_NR_DBSCAN/"
folder_DNAPAINT = "1_5EVs_DNA-PAINT_DBSCAN/"


image_name = "1_5SR_fwhm_python_clustered.tif"



Coincidence_table = pd.DataFrame(columns=["File", "Coincidence value"])




def load_image(toload):
    image=imread(toload)
    return image
    


for path in pathlist:
    
    print(path)
    
    # Define paths for both images:

    NR_path = path + folder_NR + image_name
    
    PAINT_path = path + folder_DNAPAINT + image_name
    
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
    
    
    # Calculate coincidence:
        
    Coincidence = PAINT * NR_mask
    plt.imshow(Coincidence, vmin = 0, vmax = 0.2)
    plt.title("Coincidence")
    plt.axis('off')
    plt.show()
    
    total_coincidence = sum(sum(Coincidence))
    
    # Save coincidence image (so it can be opened in Fiji)
        
    coincidence_saved = Image.fromarray(Coincidence)
    # coincidence_saved.save(path_tosave + str("Coincidence.tif"))
    
    # Add coincidence value to table
    
    Coincidence_table = Coincidence_table.append({"File":path, "Coincidence": str(total_coincidence)},ignore_index=True)
    
Coincidence_table.to_csv(root_path + "clusters_coincidence.csv", sep = "\t")


   
    
    # First I load the TuJ1 mask path by using the os.walk() function (this way I find the right file within the specified folder)
    # Make sure the mask has been scaled up to the right dimensions (i.e. x8)
    
#     TuJ1 = path + "TuJ1 mask/"
    
#     for root, dirs, files in os.walk(path):
#         for name in files:
#             if "Scaled_TuJ1_mask.tif" in name:
#                 if not "._" in name:
#                         # ~~~ 'if not' added because there are hidden files in my directory that are being imported instead of the actual file containing the localisations (i.e. Fit_Results file)
#                     TuJ1_resultsname = name
#                     print(TuJ1_resultsname)
    
#     TuJ1_path= TuJ1 + TuJ1_resultsname 
    
    
#     aSyn = path + "1_30pS129_DBSCAN/"
    
#     for root, dirs, files in os.walk(aSyn):
#         for name in files:
#             if "SR_points_python.tif" in name:
#                     if not "._" in name:
#                         # ~~~ 'if not' added because there are hidden files in my directory that are being imported instead of the actual file containing the localisations (i.e. Fit_Results file)
                        
#                         aSyn_resultsname = name
#                         print(aSyn_resultsname)
                        
#     aSyn_path= aSyn + aSyn_resultsname
    
    
#     im_TuJ1 = io.imread(TuJ1_path)
#     im_asyn = io.imread(aSyn_path)
    
    
#     plt.imshow(im_TuJ1)
#     plt.suptitle(path)
#     plt.axis('off')
#     plt.show()
    
#     plt.imshow(im_asyn)
#     plt.suptitle(path)
#     plt.axis('off')
#     plt.show()
    
#     # Coincidence between DAPI and asyn binary images
    
#     coincidence = im_TuJ1 * im_asyn
#     plt.imshow(coincidence)
#     plt.suptitle("Coincidence")
#     plt.axis('off')
#     plt.show()
    
#     total_coincidence = sum(sum(coincidence))
    
#     print(total_coincidence)
    
#     # Save coincidence image (so it can be opened in Fiji)
    
#     coincidence_saved = Image.fromarray(coincidence)
#     coincidence_saved.save(path + 'Coincident.tif')
    
    

#     # I wanna find the way to make my results into a table containing columns 
#     # as wells and rows as position within that well. Then this can be used in 
#     # Prism for further stats tests - i.e. quantification of aSyn in nucleus
#     # or in the cytosol, or total amount of aSyn (to prove the dox system is 
#     # working)
    
#     Coincidence = Coincidence.append({"File":path, "Coincidence value": str(total_coincidence)},ignore_index=True)
#     # Coincidence["Coincidence value"] = total_coincidence
#     # Coincidence["File"] = path
    
    
#     # Coincidence.to_csv(path)

# Coincidence.to_csv(path_root + "coincidence.csv", sep = "\t")
# # df = pd.DataFrame(Coincidence)
# # df.columns=Positions
# # df.insert(0,"Well", Wells)
# # df.to_csv(outpath + str(DAPI_thr) + str(asyn_thr) + 'total_coincidence.csv')
        
        
        
        





# By comparing the binary images between themselves and by opening the DAPI image on Fiji
# I see that the otsu threshold seems to be a better option for now. I will use this
# option for all the channels and then see if it is doing a good job!
























