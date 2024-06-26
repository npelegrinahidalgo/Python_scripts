#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:21:11 2024

@author: pele

Purpose:
    extract data from csv files exported from CODI containing cluster information
    
"""

import warnings
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from sklearn.cluster import DBSCAN
from skimage import filters,measure

tag = "NPH33"


filename_contains = "clusters_batch.csv"
pathlist = []

pathlist.append(r"/Users/pele/Library/CloudStorage/OneDrive-UniversityofEdinburgh/ONI placement/Results/NPH33/NPH32_2024-06-25_09-51-21/")



for path in pathlist:
    
    for roots,dirs,files in os.walk(path):
        
        for name in files:

            if filename_contains in name:
                
                data_table = name
                
    clusters_table = pd.read_table(path + data_table, sep = ",")


    grouped = clusters_table.groupby('dataset')
    
    clusters = len(grouped["Cluster ID"])
    
    average = grouped.mean()
    
    row_counts = grouped.size()
    
    FOV_table = average.assign(Clusters=row_counts.values)
    
    Clusters_col = FOV_table.pop("Clusters")

    FOV_table.insert(0,"Clusters", Clusters_col)
    
    FOV_table = FOV_table.drop(columns=["export id", "Cluster ID", "x (nm)","y (nm)",])
    
    FOV_table.to_csv(path + str(tag) + "_Clusters_data.csv", sep = ",")
    
    


