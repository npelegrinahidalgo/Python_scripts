#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 16:08:53 2022

@author: pele
"""

import os
from PIL import Image
import matplotlib.pyplot as plt
from skimage import color, io
import skimage.filters as thr
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

thr_block_size = 9

def subtract_bg(image):
    
    background = thr.threshold_local(image, thr_block_size, offset=np.percentile(image, 1), method='median')
    bg_corrected =image - background
    plt.imshow(bg_corrected)
    plt.suptitle('after')
    plt.show()
    mask_tub_saved = Image.fromarray(bg_corrected)
    mask_tub_saved.save (save_path + str(thr_block_size) + '_without_bg_TuJ1.tif')
    return bg_corrected



for path in pathlist:
    
    print(path)
    
    new_folder = "TuJ1 mask/"
    save_path = os.path.join(path, new_folder)
    if not os.path.exists(save_path):
        os.makedirs(save_path)
 
    tubulin = path + 'TuJ1.tif'
    
    im_tub = io.imread(tubulin)
    
    plt.imshow(im_tub)
    plt.suptitle('beta-tublin')
    plt.colorbar()
    plt.show()
        
    
    plt.imshow(im_tub)
    plt.suptitle('before')
    plt.show()
    
    subtracted_tub = subtract_bg(im_tub)
    
    
    threshold = thr.threshold_otsu(subtracted_tub)
    
    thr_tub = subtracted_tub > threshold
    
    plt.imshow(thr_tub)
    plt.suptitle('thresholded beta-tublin')
    plt.show()

    

    # Save boolean image to use as a mask
    # Name corresponds to count --> image being processed following pathlist order and the threshold used for background subtraction
    
    
    thr_tub_saved = Image.fromarray(thr_tub)
    thr_tub_saved.save(save_path + str(thr_block_size) + '_without_bg_otsu_mask_TuJ1.tif')
    


