#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 11:24:18 2022

@author: pele
"""
import os
import pandas as pd
# from picasso import render
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from sklearn.cluster import DBSCAN
from skimage import filters,measure




pathlist = []

pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/ONI/20220614_ibd13_IFN-treated/A1_buffer/pos_0/30_20GDSC_reconstruction/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/ONI/20220614_ibd13_IFN-treated/A1_buffer-1/pos_0/30_20GDSC_reconstruction/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/ONI/20220614_ibd13_IFN-treated/A1_buffer-2/pos_0/30_20GDSC_reconstruction/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/ONI/20220614_ibd13_IFN-treated/A2_buffer_dif_pos/pos_0/30_20GDSC_reconstruction/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/ONI/20220614_ibd13_IFN-treated/A2_buffer_dif_pos/pos_1/30_20GDSC_reconstruction/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/ONI/20220614_ibd13_IFN-treated/A2_no_buffer/pos_0/30_20GDSC_reconstruction/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/ONI/20220614_ibd13_IFN-treated/A3_buffer/pos_0/30_20GDSC_reconstruction/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/ONI/20220614_ibd13_IFN-treated/A3_buffer-0/pos_0/30_20GDSC_reconstruction/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/ONI/20220614_ibd13_IFN-treated/A4_buffer-2/pos_0/30_20GDSC_reconstruction/")


for path in pathlist:
    
    print(path)
    loc_path = path + "total_aSyn_FitResults_withheader.txt"
    
    loc_table = pd.read_table(loc_path, sep ="\t", header =7)
    
    locs = len(loc_table["#frames"])
    
    print(locs)
    
    