#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 15:10:01 2022

@author: pele
"""

import numpy as np
import pandas as pd
import os
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import scatterplot

filename_contains = "pS129"

pathlist = []

pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20220810_organoid_G51D_pS129-Atto655_TuJ1-AF488_DAPI/5000_frames/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20220810_organoid_G51D_pS129-Atto655_TuJ1-AF488_DAPI/5000_frames-1/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20220810_organoid_G51D_pS129-Atto655_TuJ1-AF488_DAPI/5000_frames-2-1/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20220810_organoid_G51D_pS129-Atto655_TuJ1-AF488_DAPI/5000_frames-2-1/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20220810_organoid_G51D_pS129-Atto655_TuJ1-AF488_DAPI/5000_frames-2-1-2/pos_0/")


locs = pd.DataFrame(columns=["Source","localisations"])

for path in pathlist:
    for root, dirs, files in os.walk(path):
        for name in files:
            if filename_contains in name:
                if "_headers.txt" in name:
                    if not "._" in name:
                                # ~~~ 'if not' added because there are hidden files in my directory that are being imported instead of the actual file containing the localisations (i.e. Fit_Results file)
                                
                                
                        resultsname = name
                        print(path,resultsname)
                        
                        
                        
        fits_path= path + resultsname
        
        loc_data = pd.read_table(fits_path, sep = '\t', header = 7)
        
        # print(loc_data["Source"])
        # no_locs = len(loc_data["#frames"])
        print(str(len(loc_data["#frames"])))
        # new_locs = locs.append({"Source": path, "localisations":no_locs},ignore_index=True)
    
    
    