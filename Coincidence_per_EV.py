#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 18:08:47 2023

@author: pele

This script will

(1) Threshold image using automated otsu thresholding

(2) Label all particles (EVs) once thresholded

(3) Measure the specified properties of these particles already labelled

"""


from skimage.io import imread
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from skimage import filters,measure
from skimage.filters import threshold_local

######    Functions to be used defined below    ########


# Load image into spyder:
def load_im(to_load):
    
    image = imread(to_load)
    
    return image

    
# Apply threshold to image and obtain binary image
def threshold(input_image):
    
    threshold_value=filters.threshold_otsu(input_image)  
    
    binary_image = input_image > threshold_value

    return threshold_value,binary_image


# Label image to identify all EVs in it
def label_image(input_image):
    
    labelled_image = measure.label(input_image, connectivity = 2)
    
    number_of_features = labelled_image.max()
 
    return number_of_features,labelled_image
    


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






image_tag = "638_cropped.tif"


EV_table = pd.DataFrame(columns=["File", "Number of EVs", "ID"])


for path in pathlist:
    
    image = path + image_tag
    
    # Load image
    im = load_im(image)
    plt.imshow(im)
    
    # Perform thresholding using function defined above
    
    thr, boolean_im = threshold(im)
    
    # Convert boolean thresholded image to binary for labelling
    binary_im = boolean_im.astype(int)

    # Perform labelling using funciton defined above
    features, labels = label_image(binary_im)    
    plt.imshow(labels)
    plt.colorbar()
    plt.show()
    plt.show()
    
    
    
    if str("A2") in path:
        
        EV_table = EV_table.append({"File":path, "Number of EVs": int(features), "ID": str("A2")},ignore_index=True)
    
    if str("B2") in path:
        
        EV_table = EV_table.append({"File":path, "Number of EVs": int(features), "ID": str("B2")},ignore_index=True)
    
    if str("C2") in path:
        
        EV_table = EV_table.append({"File":path, "Number of EVs": int(features), "ID": str("C2")},ignore_index=True)
    
    if str("A4") in path:
        
        EV_table = EV_table.append({"File":path, "Number of EVs": int(features), "ID": str("A4")},ignore_index=True)
    
    if str("B4") in path:
        
        EV_table = EV_table.append({"File":path, "Number of EVs": int(features), "ID": str("B4")},ignore_index=True)
    
    if str("C4") in path:
        
        EV_table = EV_table.append({"File":path, "Number of EVs": int(features), "ID": str("C4")},ignore_index=True)
    
EV_table.to_csv(root_path + "Number of EVs_647.csv", sep = "\t")


data = EV_table

df = pd.DataFrame(data)

# Calculate mean values per condition
mean_values = df.groupby('ID')['Number of EVs'].mean().reset_index()


plt.plot(mean_values["Number of EVs"])

plt.bar(mean_values["ID"], height = mean_values["Number of EVs"])
# Set labels and title

plt.title('Plot of Data Points with Mean per Condition')

plt.axis("on")



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




