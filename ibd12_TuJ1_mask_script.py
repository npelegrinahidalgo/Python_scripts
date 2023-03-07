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



pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/TIRFM/20220609_ibd12_PFF_seeded/A1+ buffer_2022_06_09_17_22_06/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/TIRFM/20220609_ibd12_PFF_seeded/A1+buffer_2022_06_09_12_06_42/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/TIRFM/20220609_ibd12_PFF_seeded/A1+buffer_2022_06_09_12_11_43/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/TIRFM/20220609_ibd12_PFF_seeded/A1+buffer_test_2022_06_09_12_20_39/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/TIRFM/20220609_ibd12_PFF_seeded/A1no_buffer_2022_06_09_11_53_00/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/TIRFM/20220609_ibd12_PFF_seeded/A2+ buffer_2022_06_09_13_08_33/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/TIRFM/20220609_ibd12_PFF_seeded/A2+ buffer_2022_06_09_13_38_03/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/TIRFM/20220609_ibd12_PFF_seeded/A2+ buffer_2022_06_09_14_00_53/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/TIRFM/20220609_ibd12_PFF_seeded/A2no_buffer_2022_06_09_12_54_59/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/TIRFM/20220609_ibd12_PFF_seeded/A3+ buffer_2022_06_09_14_28_42/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/TIRFM/20220609_ibd12_PFF_seeded/A3+ buffer_2022_06_09_14_56_35/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/TIRFM/20220609_ibd12_PFF_seeded/A3+ buffer_2022_06_09_15_17_42/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/TIRFM/20220609_ibd12_PFF_seeded/A3no_buffer_2022_06_09_14_20_38/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/TIRFM/20220609_ibd12_PFF_seeded/A4+ buffer_2022_06_09_15_49_20/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/TIRFM/20220609_ibd12_PFF_seeded/A4+ buffer_2022_06_09_16_02_57/")
pathlist.append(r"/Volumes/Noe PhD 1/Microscopes/TIRFM/20220609_ibd12_PFF_seeded/A4no_buffer_2022_06_09_15_42_20/")



def subtract_bg(image):
    
    background = thr.threshold_local(image, 15, offset=np.percentile(image, 1), method='median')
    bg_corrected =image - background
    plt.imshow(bg_corrected)
    plt.suptitle('after')
    plt.show()
    mask_tub_saved = Image.fromarray(bg_corrected)
    mask_tub_saved.save (save_path + '_5_without_bg_TuJ1.tif')
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
    thr_tub_saved.save(save_path + '_5_without_bg_otsu_mask_TuJ1.tif')
    


