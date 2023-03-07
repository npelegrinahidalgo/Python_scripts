#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 10:55:09 2022

@author: pele
"""
from skimage.io import imread
import os
import pandas as pd
# from picasso import render
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from sklearn.cluster import DBSCAN
from skimage import filters,measure
from skimage.filters import threshold_local



pathlist = []

pathlist.append(r"/Volumes/Noelia PhD/Microscopes/TIRFM/20220609_ibd12_PFF_seeded/A1+ buffer_2022_06_09_17_22_06/")



def subtract_bg(image):
    background = threshold_local(image, 11, offset=np.percentile(image, 1), method='median')
    bg_corrected =image - background
    plt.imshow(bg_corrected)
    plt.suptitle('after')
    plt.show()
    return bg_corrected

for path in pathlist:
    
    tubulin = path + 'TuJ1.tif'
    
    to_mask = imread(tubulin)
    
    plt.imshow(to_mask)
    plt.suptitle('before')
    plt.show()
    
    subtract_bg(to_mask)
    


