#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 10:50:24 2022

@author: pele
"""
import os
from PIL import Image
import matplotlib.pyplot as plt
from skimage import color, io
from skimage.filters import try_all_threshold, threshold_otsu
import numpy as np
from tabulate import tabulate
import pandas as pd



# inpaths to analyse
pathlist=[]


pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20220809_NPH_CA_aSyn_pS129/G51D_A3_pos_2/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20220809_NPH_CA_aSyn_pS129/Ctl_A2_pos_2/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20220809_NPH_CA_aSyn_pS129/G51D_A3_pos_1/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20220809_NPH_CA_aSyn_pS129/Ctl_A2_pos_1/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20220809_NPH_CA_aSyn_pS129/Ctl_A2_pos_0/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20220809_NPH_CA_aSyn_pS129/Ctl_A2_pos_0/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20220809_NPH_CA_aSyn_pS129/G51D_A3_pos_3/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20220809_NPH_CA_aSyn_pS129/G51D_A3_pos_0_5000frames/")

path_root = "/Volumes/Noe PhD 2/Microscopes/ONI/20220809_NPH_CA_aSyn_pS129/"


Coincidence = pd.DataFrame(index=range(16),columns=["File", "Coincidence value"])

for path in pathlist:
    
    print(path)
    # # The lines below is simply to track each coincidence value back to its file
    # i = 1
    # i += 1
    
    # First I load the TuJ1 mask path by using the os.walk() function (this way I find the right file within the specified folder)
    # Make sure the mask has been scaled up to the right dimensions (i.e. x8)
    
    TuJ1 = path + "TuJ1 mask/"
    
    for root, dirs, files in os.walk(path):
        for name in files:
            if "Scaled_TuJ1_mask.tif" in name:
                if not "._" in name:
                        # ~~~ 'if not' added because there are hidden files in my directory that are being imported instead of the actual file containing the localisations (i.e. Fit_Results file)
                    TuJ1_resultsname = name
                    print(TuJ1_resultsname)
    
    TuJ1_path= TuJ1 + TuJ1_resultsname 
    
    
    aSyn = path + "1_30pS129_DBSCAN/"
    
    for root, dirs, files in os.walk(aSyn):
        for name in files:
            if "SR_points_python.tif" in name:
                    if not "._" in name:
                        # ~~~ 'if not' added because there are hidden files in my directory that are being imported instead of the actual file containing the localisations (i.e. Fit_Results file)
                        
                        aSyn_resultsname = name
                        print(aSyn_resultsname)
                        
    aSyn_path= aSyn + aSyn_resultsname
    
    
    im_TuJ1 = io.imread(TuJ1_path)
    im_asyn = io.imread(aSyn_path)
    
    
    plt.imshow(im_TuJ1)
    plt.suptitle(path)
    plt.axis('off')
    plt.show()
    
    plt.imshow(im_asyn)
    plt.suptitle(path)
    plt.axis('off')
    plt.show()
    
    # Coincidence between DAPI and asyn binary images
    
    coincidence = im_TuJ1 * im_asyn
    plt.imshow(coincidence)
    plt.suptitle("Coincidence")
    plt.axis('off')
    plt.show()
    
    total_coincidence = sum(sum(coincidence))
    
    print(total_coincidence)
    
    # Save coincidence image (so it can be opened in Fiji)
    
    coincidence_saved = Image.fromarray(coincidence)
    coincidence_saved.save(path + 'Coincident.tif')
    
    

    # I wanna find the way to make my results into a table containing columns 
    # as wells and rows as position within that well. Then this can be used in 
    # Prism for further stats tests - i.e. quantification of aSyn in nucleus
    # or in the cytosol, or total amount of aSyn (to prove the dox system is 
    # working)
    
    Coincidence = Coincidence.append({"File":path, "Coincidence value": str(total_coincidence)},ignore_index=True)
    # Coincidence["Coincidence value"] = total_coincidence
    # Coincidence["File"] = path
    
    
    # Coincidence.to_csv(path)

Coincidence.to_csv(path_root + "coincidence.csv", sep = "\t")
# df = pd.DataFrame(Coincidence)
# df.columns=Positions
# df.insert(0,"Well", Wells)
# df.to_csv(outpath + str(DAPI_thr) + str(asyn_thr) + 'total_coincidence.csv')
        
        
        
        





# By comparing the binary images between themselves and by opening the DAPI image on Fiji
# I see that the otsu threshold seems to be a better option for now. I will use this
# option for all the channels and then see if it is doing a good job!

























