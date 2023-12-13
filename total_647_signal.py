#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 16:44:31 2023

@author: pele

This script will take an image, apply a threshold to mask an image and then 
on the masked image it will calculate the total signal intensity for that channel

"""

import os
from skimage.io import imread
from PIL import Image
import matplotlib.pyplot as plt
from skimage import color, io
from skimage.filters import try_all_threshold, threshold_otsu, threshold_mean
import numpy as np
from tabulate import tabulate
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
from skimage.filters import threshold_local


root_path = r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/"
# inpaths to analyse
pathlist=[]



pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_10/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_11/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_12/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_13/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_14/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_15/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_16/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_17/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_18/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_19/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_20/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_21/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_22/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_23/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_24/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_9/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_10/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_11/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_12/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_13/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_14/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_15/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_16/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_17/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_18/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_19/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_20/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_21/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_22/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_23/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_24/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_9/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_10/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_11/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_12/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_13/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_14/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_15/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_16/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_17/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_18/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_19/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_20/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_21/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_22/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_23/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_24/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_9/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_10/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_11/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_12/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_13/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_14/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_15/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_16/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_17/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_18/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_19/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_20/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_21/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_22/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_23/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_24/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_9/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_10/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_11/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_12/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_13/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_14/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_15/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_16/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_17/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_18/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_19/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_20/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_21/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_22/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_23/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_24/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_9/")

image_638 = "638_cropped.tif"


intensity_table = pd.DataFrame(columns=["File", "Intensity", "ID"])


def load_image(toload):
    image=imread(toload).astype("float32")
    return image
    
def threshold(image):
    threshold = threshold_otsu(image)
    thr_image =image > threshold
    return thr_image

for path in pathlist:
    
    print(path)
    
    # Define paths for both images:

    path_638 = path + image_638
    
    # Load 638 image and mask it (average + 2* std formulae):
        
    im_638 = load_image(path_638)
    plt.imshow(im_638)
    plt.title("638")
    plt.axis('off')
    plt.show()
    
    
    ave_638 = im_638.mean()
    std_638 = im_638.std()
    
    masked_638 = im_638 > ave_638 +  2 * std_638
    plt.imshow(masked_638)
    plt.colorbar()
    plt.show()
    
    masked_image = im_638 * masked_638
    plt.imshow(masked_image)
    plt.colorbar()
    plt.show()
    plt.show()
    
    signal = sum(sum(masked_image))
    print("Manual thresholded image signal is " + str(signal))
    
    # Trying new thresholding automated instead:
    
    auto_thresholded_im = threshold(im_638)
    plt.imshow(auto_thresholded_im)
    plt.colorbar()
    plt.show()
    plt.show()
    
    auto_masked_im = im_638 * auto_thresholded_im
    plt.imshow(auto_masked_im)
    plt.colorbar()
    plt.show()
    plt.show()
    
    signal_auto = sum(sum(auto_masked_im))
    print("Auto thresholded image signal is " + str(signal_auto))
    
    total_intensity = sum(sum(masked_image))
    
    # Add intensity value to table
    if str("A2") in path:
        
        intensity_table = intensity_table.append({"File":path, "Intensity": int(total_intensity), "ID": str("A2")},ignore_index=True)
    
    if str("B2") in path:
        
        intensity_table = intensity_table.append({"File":path, "Intensity": int(total_intensity), "ID": str("B2")},ignore_index=True)
    
    if str("C2") in path:
        
        intensity_table = intensity_table.append({"File":path, "Intensity": int(total_intensity), "ID": str("C2")},ignore_index=True)
    
    if str("A4") in path:
        
        intensity_table = intensity_table.append({"File":path, "Intensity": int(total_intensity), "ID": str("A4")},ignore_index=True)
    
    if str("B4") in path:
        
        intensity_table = intensity_table.append({"File":path, "Intensity": int(total_intensity), "ID": str("B4")},ignore_index=True)
    
    if str("C4") in path:
        
        intensity_table = intensity_table.append({"File":path, "Intensity": int(total_intensity), "ID": str("C4")},ignore_index=True)
    
intensity_table.to_csv(root_path + "Intensity_647.csv", sep = "\t")



# Plot graph for coincidence values

data = intensity_table

df = pd.DataFrame(data)

# Calculate mean values per condition
mean_values = df.groupby('ID')['Intensity'].mean().reset_index()


plt.plot(mean_values["Intensity"])

plt.bar(mean_values["ID"], height = mean_values["Intensity"])
# Set labels and title

plt.title('Plot of Data Points with Mean per Condition')

plt.axis("on")





