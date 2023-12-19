#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 11:47:56 2023

@author: pele

Script to analyse EV data (NR & DNA-PAINT) coincidence in clustered data (using NR as mask)


First, extract each NR cluster data into table, then use this table to analyse coincident events
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


root_path = r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/"

pathlist=[]

# inpaths to analyse

pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/A3_500pM_NR+1nM_E2285/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/A3_500pM_NR+1nM_E2285/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/A3_500pM_NR+1nM_E2285/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/A3_500pM_NR+1nM_E2285/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/A3_500pM_NR+1nM_E2285/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/A3_500pM_NR-3/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/A3_500pM_NR-3/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/A4_500pM_NR+1nM_E2285/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/A4_500pM_NR+1nM_E2285/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/A4_500pM_NR+1nM_E2285/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/A4_500pM_NR+1nM_E2285/pos_4/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/A4_500pM_NR+1nM_E2285/pos_5/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/B3_500pM_NR+1nM_E2285/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/B3_500pM_NR+1nM_E2285/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/B3_500pM_NR+1nM_E2285/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/B3_500pM_NR+1nM_E2285/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/B3_500pM_NR+1nM_E2285-1/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/B3_500pM_NR+1nM_E2285-1/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/B3_500pM_NR+1nM_E2285-1/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/B3_500pM_NR+1nM_E2285-1/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/B3_500pM_NR+1nM_E2285-1/pos_4/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/B3_500pM_NR+1nM_E2285-1/pos_5/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/B4_500pM_NR+1nM_E2285/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/B4_500pM_NR+1nM_E2285/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/B4_500pM_NR+1nM_E2285/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/B4_500pM_NR+1nM_E2285/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/B4_500pM_NR+1nM_E2285/pos_4/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/B4_500pM_NR+1nM_E2285/pos_5/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/C4_500pM_NR+1nM_E2285/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/C4_500pM_NR+1nM_E2285/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/C4_500pM_NR+1nM_E2285/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/C5_500pM_NR+1nM_E2285-1/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/C5_500pM_NR+1nM_E2285-1/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230414_NPH_SiMPull_mouse_EVs/C5_500pM_NR+1nM_E2285-1/pos_2/")

# Parameters to use:
    
pixel_size = 117
scale = 8
image_height = 684
image_width = 428



folder_NR = "1_5EVs_NR_DBSCAN/"
# folder_DNAPAINT = "1_5EVs_exWAGO_mapped_DBSCAN/"


NR_cluster_file = "1_5all.csv"
exWAGO_locs_file = "exWAGO_mapped_FitResults.txt"


Coincidence_table = pd.DataFrame(columns=["File", "Coincidence value"])




def load_image(toload):
    image=imread(toload)
    return image
    

i= -1

for path in pathlist:
    
   
    print(path)
    
    
    # Load NR cluster data (i.e. all.csv file):
        
    to_load_NR = path + folder_NR + NR_cluster_file
    
    NR_clusters_table = pd.read_table(to_load_NR, sep="\t")
    
    # Extract specific cluster data (i.e. one cluster per for loop):
        
    specific_cluster = NR_clusters_table[NR_clusters_table["cluster"] == i]
    
    locs_specific_cluster = np.array(list(zip(specific_cluster["xw"],specific_cluster["yw"])))
    
    scaled_locs_specific_cluster = locs_specific_cluster * scale
    
    tuple_NR = list(map(tuple, scaled_locs_specific_cluster))
    
    # Load exWAGO locs to be used for coincidence:
        
    to_load_exWAGO = path + exWAGO_locs_file
    
    exWAGO_locs_table = pd.read_table(to_load_exWAGO, sep="\t")
    
    exWAGO_locs_only = np.array(list(zip(exWAGO_locs_table["X"],exWAGO_locs_table["Y"])))
    
    
    scaled_exWAGO = exWAGO_locs_only * scale
    
    tuple_exWAGO = list(map(tuple, scaled_exWAGO))
    
    
    # Calculate coincidence between each cluster in NR and each loc in exWAGO:
        
    for loc in tuple_NR:
        
        for tup in tuple_exWAGO:
            
            coincidence = loc * tup
            
            if coincidence > 0:
                
                Coincidence_table = Coincidence_table.append({"File": path, "Coincidence value": int(coincidence)}, ignore_index = True)
            
            
                
    
    
    
    
    i += 1
    

#     # Load NR image and mask it (average + 2* std formula):
        
#     NR = load_image(NR_path)
#     plt.imshow(NR, vmin = 0, vmax = 0.2)
#     plt.title("NR")
#     plt.axis('off')
#     plt.show()
    
    
#     NR_ave = NR.mean()
#     NR_std = NR.std()
    
#     NR_mask = NR > NR_ave +  2 * NR_std
    
#     # Load DNA-PAINT image:
        
#     PAINT = load_image(PAINT_path)
#     plt.imshow(PAINT, vmin = 0, vmax = 0.2)
#     plt.title("DNA-PAINT raw")
#     plt.axis('off')
#     plt.show()    
    
    
#     # Calculate coincidence:
        
#     Coincidence = PAINT * NR_mask
#     plt.imshow(Coincidence, vmin = 0, vmax = 0.2)
#     plt.title("Coincidence")
#     plt.axis('off')
#     plt.show()
    
#     total_coincidence = sum(sum(Coincidence))
#     print(total_coincidence)
    
#     # Save coincidence image (so it can be opened in Fiji)
        
#     coincidence_saved = Image.fromarray(Coincidence)
#     # coincidence_saved.save(path_tosave + str("Coincidence.tif"))
    
#     # Add coincidence value to table
    
#     Coincidence_table = Coincidence_table.append({"File":path, "Coincidence value": str(total_coincidence)},ignore_index=True)
    
    
# Coincidence_table.to_csv(root_path + "clusters_coincidence.csv", sep = "\t")






