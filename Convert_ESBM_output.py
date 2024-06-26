#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:58:07 2024

@author: pele

Purpose: extract DBSCAB "metrics" values and convert them to right units for prism graphs plotting

"""

import warnings
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from sklearn.cluster import DBSCAN
from skimage import filters,measure

px_size = 117
scale = 8

table_name = "1_50_aSyn_Metrics.csv"

total_clus = pd.DataFrame(columns = ["file", "Number of clusters"])


pathlist = []

pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/Placement/DFM/20240605_NPH26/20240606_NPH26_30000-frames/L1+10nM-E2285/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/Placement/DFM/20240605_NPH26/20240606_NPH26_30000-frames/L1+10nM-E2285/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/Placement/DFM/20240605_NPH26/20240606_NPH26_30000-frames/L1+10nM-E2285/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/Placement/DFM/20240605_NPH26/20240606_NPH26_30000-frames/L2+10nM-E2285/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/Placement/DFM/20240605_NPH26/20240606_NPH26_30000-frames/L2+10nM-E2285/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/Placement/DFM/20240605_NPH26/20240606_NPH26_30000-frames/L2+10nM-E2285/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/Placement/DFM/20240605_NPH26/20240606_NPH26_30000-frames/L3+10nM-E2285/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/Placement/DFM/20240605_NPH26/20240606_NPH26_30000-frames/L3+10nM-E2285/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/Placement/DFM/20240605_NPH26/20240606_NPH26_30000-frames/L3+10nM-E2285/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/Placement/DFM/20240605_NPH26/20240605_NPH26_30000-frames/L4+10nM-E2285/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/Placement/DFM/20240605_NPH26/20240605_NPH26_30000-frames/L4+10nM-E2285/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/Placement/DFM/20240605_NPH26/20240605_NPH26_30000-frames/L4+10nM-E2285/pos_2/")

root_path = r"/Volumes/Noe PhD 4/Microscopes/Placement/DFM/20240605_NPH26/"

def load_table(to_open):
    
    table = pd.read_table(to_open)

    return table

def convert_data(table):
    
    converted_data = pd.DataFrame(index=table.index)
    
    converted_data["area (nm2)"] = table["area"] * (px_size / scale)
    converted_data["length (nm)"] = table["major_axis_length"] * (px_size / scale)
    converted_data["eccentricity"] = table["Eccentricity"]
    converted_data["density"] = table["Number_of_locs"] / table["area"]
    converted_data["file"] = path
    
    clusters = len(data)
    
    return converted_data, clusters
    

for path in pathlist:
    
    to_open = path + "1_50_aSyn_DBSCAN/" + table_name
    
    data = load_table(to_open)
    
    output_table, clusters = convert_data(data)
    
    total_clus = total_clus.append({"file": path, "Number of clusters": clusters}, ignore_index = True)
    
    output_table.to_csv(path +'Converted_properties.csv', sep = '\t')

total_clus.to_csv(root_path + "Number_of_clusters.csv")
    

    
    
    
    
    
    
    
    