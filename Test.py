#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:05:47 2024

@author: pele
"""

from skimage.io import imread
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from skimage import filters,measure
from skimage.filters import threshold_local

image_height=512
image_width=512
Pixel_size=103
scale=8
precision_threshold=250
eps_threshold=0.5
minimum_locs_threshold=15
prec_thresh=40


path_638 = r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/C2+D6G4AB(5nM)+nB(15nM)+D7674(1nM)+NR(5nM)_2024-02-16_19-44-36/Processed images/X0Y0R1W1_638_0_FitResults.txt"
path_515 = r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/C2+D6G4AB(5nM)+nB(15nM)+D7674(1nM)+NR(5nM)_2024-02-16_19-44-36/Processed images/X0Y0R1W1_1_5_515_DBSCAN/1_5_515_SR_width_python_clustered.tif"    



def generate_SR(coords):
    SR_plot_def=np.zeros((image_height*scale,image_width*scale),dtype=float)
    j=0
    for i in coords:
        
        xcoord=coords[j,0]
        ycoord=coords[j,1]
        scale_xcoord=round(xcoord*scale)
        scale_ycoord=round(ycoord*scale)
        # if(scale_xcoord<image_height and scale_ycoord<image_width):
        SR_plot_def[scale_ycoord,scale_xcoord]+=1
        
        j+=1
    return SR_plot_def


def label_image(input_image):
    
    labelled_image = measure.label(input_image, connectivity = 2)
    
    number_of_features = labelled_image.max()
 
    return number_of_features,labelled_image





# def feature_coincidence(binary_image1,binary_image2):
    
#     number_of_features,labelled_image1=label_image(binary_image1)          # Labelled image is required for this analysis
#     coincident_image=binary_image1 & binary_image2        # Find pixel overlap between the two images
#     coincident_labels=labelled_image1*coincident_image   # This gives a coincident image with the pixels being equal to label
#     coinc_list, coinc_pixels = np.unique(coincident_labels, return_counts=True)     # This counts number of unique occureences in the image
    
#     # Now for some statistics
#     total_labels=labelled_image1.max()
#     total_labels_coinc=len(coinc_list)
#     fraction_coinc=total_labels_coinc/total_labels
    
#     # Now look at the fraction of overlap in each feature
#     # First of all, count the number of unique occurances in original image
#     label_list, label_pixels = np.unique(labelled_image1, return_counts=True)
#     fract_pixels_overlap=[]
#     for i in range(len(coinc_list)):
#         overlap_pixels=coinc_pixels[i]
#         label=coinc_list[i]
#         total_pixels=label_pixels[label]
#         fract=1.0*overlap_pixels/total_pixels
#         fract_pixels_overlap.append(fract)
    
    
#     # Generate the images
#     coinc_list[0]=1000000   # First value is zero- don't want to count these. 
#     coincident_features_image=np.isin(labelled_image1,coinc_list)   # Generates binary image only from labels in coinc list
#     coinc_list[0]=0
#     non_coincident_features_image=~np.isin(labelled_image1,coinc_list)  # Generates image only from numbers not in coinc list.
    
#     return number_of_features, coincident_features_image


# Generate SR image:
fits_path= path_638
loc_data=pd.read_table(fits_path)
    
coords= np.array(list(zip(loc_data['X'],loc_data['Y'])))


# Load images:
SR_638 = generate_SR(coords)

NR_img = imread(path_515)

# Convert to binary:

SR_binary = SR_638 > 0

NR_binary = NR_img > 0

# Perform coincidence analysis:
number_of_features,labelled_image1= label_image(NR_binary)

coincident_image_bool = NR_binary & SR_binary
coincident_labels=labelled_image1*coincident_image_bool
 
coincidence = np.unique(coincident_labels)

coinc_total = len(coincidence)

fraction_coinc = coinc_total/number_of_features









