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
import seaborn as sns

######    Functions to be used defined below    ########


# Load image into spyder:
def load_im(to_load):
    
    image = imread(to_load)
    
    return image

    
# Apply threshold to image and obtain binary image
def threshold_638(input_image):
    
    threshold_value_638 = thr_set_638
    
    binary_image_638 = input_image > threshold_value_638

    return threshold_value_638,binary_image_638

def threshold_561(input_image):
    
    threshold_value_561 = thr_set_561
    
    binary_image_561 = input_image > threshold_value_561

    return threshold_value_561,binary_image_561


# Label image to identify all EVs in it
def label_image(input_image):
    
    labelled_image = measure.label(input_image, connectivity = 2)
    
    number_of_features = labelled_image.max()
 
    return number_of_features,labelled_image
    

def feature_coincidence(binary_image1,binary_image2):
    number_of_features,labelled_image1=label_image(binary_image1)          # Labelled image is required for this analysis
    coincident_image=binary_image1 & binary_image2        # Find pixel overlap between the two images
    coincident_labels=labelled_image1*coincident_image   # This gives a coincident image with the pixels being equal to label
    coinc_list, coinc_pixels = np.unique(coincident_labels, return_counts=True)     # This counts number of unique occureences in the image
    # Now for some statistics
    total_labels=labelled_image1.max()
    total_labels_coinc=len(coinc_list)
    fraction_coinc=total_labels_coinc/total_labels
    
    # Now look at the fraction of overlap in each feature
    # First of all, count the number of unique occurances in original image
    label_list, label_pixels = np.unique(labelled_image1, return_counts=True)
    fract_pixels_overlap=[]
    for i in range(len(coinc_list)):
        overlap_pixels=coinc_pixels[i]
        label=coinc_list[i]
        total_pixels=label_pixels[label]
        fract=1.0*overlap_pixels/total_pixels
        fract_pixels_overlap.append(fract)
    
    
    # Generate the images
    coinc_list[0]=1000000   # First value is zero- don't want to count these. 
    coincident_features_image=np.isin(labelled_image1,coinc_list)   # Generates binary image only from labels in coinc list
    coinc_list[0]=0
    non_coincident_features_image=~np.isin(labelled_image1,coinc_list)  # Generates image only from numbers not in coinc list.
    
    return total_labels,coincident_features_image

def calculate_intensity_coinc(coinc_im,image):
    
    int_coinc_im = coinc_im*image
    
    int_coinc_values = int_coinc_im
    
    for i in range(len(int_coinc_im)):
        for j in range(len(int_coinc_im[i])):
            
        
            if int_coinc_im[i][j] > 0:
                               
                int_coinc_values[i][j] = int_coinc_im[i][j]
        
    mean_int = sum(int_coinc_values)/len(int_coinc_values)
    
    return int_coinc_im, mean_int
    
    

root_path = r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/"

# inpaths to analyse
pathlist=[]

pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_10/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_11/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_12/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_13/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_14/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_15/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_16/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_17/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_18/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_19/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_20/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_21/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_22/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_23/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_24/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_4/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_5/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_6/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_7/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_8/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_9/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_10/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_11/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_12/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_13/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_14/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_15/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_16/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_17/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_18/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_19/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_20/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_21/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_22/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_23/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_24/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_4/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_5/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_6/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_7/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_8/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_9/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_4/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_5/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_6/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_10/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_11/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_12/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_13/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_14/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_15/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_16/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_17/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_18/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_19/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_20/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_21/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_22/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_23/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_24/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_4/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_5/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_6/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_7/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_8/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_9/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_10/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_11/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_12/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_13/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_14/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_15/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_16/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_17/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_18/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_19/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_20/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_21/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_22/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_23/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_24/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_4/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_5/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_6/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_7/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_8/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_9/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_10/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_11/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_12/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_13/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_14/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_15/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_16/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_17/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_18/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_19/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_20/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_21/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_22/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_23/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_24/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_4/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_5/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_6/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_7/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_8/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_9/")






thr_set_638 = 882.9230769230769
thr_set_561 = 6407.307692307692

image_tag_638 = "638_cropped.tif"
image_tag_561 = "561_cropped.tif"

EV_table = pd.DataFrame(columns=["File", "Number of EVs", "Coincidence", "Fraction coincidence", "ID"])


for path in pathlist:
    
    image_638 = path + image_tag_638
    image_561 = path + image_tag_561
    
    
    # Load image
    im_638 = load_im(image_638)
    plt.imshow(im_638)
    
    # Perform thresholding using function defined above
    
    thr_638, boolean_im_638 = threshold_638(im_638)
    
    # Convert boolean thresholded image to binary for labelling
    binary_im_638 = boolean_im_638.astype(int)

    # Perform labelling using funciton defined above
    features, labels = label_image(binary_im_638)    
    plt.imshow(labels)
    plt.colorbar()
    plt.show()
    plt.show()
    
    # Calculate coincidence using coincidence function
        # First we need to threshold the green channel (561) using threshold function
    
    im_561 = load_im(image_561)
    
    thr_561, boolean_im_561 = threshold_561(im_561)
    
    binary_im_561 = boolean_im_561.astype(int)
    
    
    # Use coincidence features function -- Still trying to understand fully how this works -- 
    
    red_coinc_list, coinc_image=feature_coincidence(binary_im_638,binary_im_561)

    # From coinc function, calculate fraction of coincidence
    fraction = red_coinc_list/features
    
    # Round it up to fit decimals (it's numbers between 1 & 0 so you need decimals on!)
    fraction_rounded = round(fraction, 2)
    
    # Calculate intensity of each feature
    
    int_coinc_561, mean_int_561 = calculate_intensity_coinc(coinc_image,im_561)
    plt.imshow(int_coinc_561)
    plt.colorbar()
    plt.show()
    
    
    if features == 0:
            
        if str("A2") in path:
            
            EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": 0, "ID": str("EVs only")},ignore_index=True)
        
        if str("B2") in path:
            
            EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": 0, "ID": str("No EVs")},ignore_index=True)
        
        if str("C2") in path:
            
            EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": 0, "ID": str("0.005% Triton")},ignore_index=True)
        
        if str("A4") in path:
            
            EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": 0, "ID": str("0.01% Triton")},ignore_index=True)
        
        if str("B4") in path:
            
            EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": 0, "ID": str("0.05% Triton")},ignore_index=True)
        
        if str("C4") in path:
            
            EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": 0, "ID": str("0.1% Triton")},ignore_index=True)
    

    else:
        
        if str("A2") in path:
            
            EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": fraction_rounded, "ID": str("EVs only")},ignore_index=True)
        
        if str("B2") in path:
            
            EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": fraction_rounded, "ID": str("No EVs")},ignore_index=True)
        
        if str("C3") in path:
            
            EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": fraction_rounded, "ID": str("0.005% Triton")},ignore_index=True)
        
        if str("A4") in path:
            
            EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": fraction_rounded, "ID": str("0.01% Triton")},ignore_index=True)
        
        if str("B4") in path:
            
            EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": fraction_rounded, "ID": str("0.05% Triton")},ignore_index=True)
        
        if str("C4") in path:
            
            EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": fraction_rounded, "ID": str("0.1% Triton")},ignore_index=True)
    

EV_table.to_csv(root_path + "Coincidence_per_EV_C2_only.csv", sep = "\t")



    
data = EV_table

df = pd.DataFrame(data)

mean_values = df.groupby('ID')['Number of EVs'].mean().reset_index()


# Plot total No EVs:

sns.boxplot(x='ID', y='Number of EVs', data=df, showcaps=True, showmeans=True)
sns.stripplot(x='ID', y='Number of EVs', data=df, color='black', alpha=0.5)
plt.xticks(rotation=45)
plt.xlabel('')  # Set an empty string as x-axis label
plt.tight_layout()
plt.legend()
# plt.savefig(root_path + 'Number_of_EVs.png', dpi=300)
plt.show()



# Plot the fraction coincidence


sns.boxplot(x='ID', y='Fraction coincidence', data=df, showcaps=True, showmeans=True)
sns.stripplot(x='ID', y='Fraction coincidence', data=df, color='black', alpha=0.5)
plt.xticks(rotation=45)
plt.xlabel('')  # Set an empty string as x-axis label
plt.tight_layout()
plt.savefig(root_path + 'Fraction exWAGO.png', dpi=300)
plt.show()



