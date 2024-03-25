#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 22:13:52 2024

@author: pele
"""



from skimage.io import imread
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from skimage import filters,measure
import skimage.filters as thr
import seaborn as sns

######    Functions to be used defined below    ########


# Load image into spyder:
def load_im(to_load):
    
    image = imread(to_load)
    
    return image

def threshold_561(image_DL):
    
    background = thr.threshold_local(image_DL, 5, offset=np.percentile(image_DL, 1), method='median')
    
    image_no_bg = image_DL - background
    
    threshold_value = thr.threshold_otsu(image_no_bg)
    
    image_thr = image_no_bg > threshold_value
    
    
    return threshold_value, image_thr
    
def threshold_638(image_DL):
    
    background = thr.threshold_local(image_DL, 5, offset=np.percentile(image_DL, 1), method='median')
    
    image_no_bg = image_DL - background
    
    threshold_value = thr.threshold_otsu(image_no_bg)
    
    image_thr = image_no_bg > threshold_value
    
    
    return threshold_value, image_thr


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
    total_labels=len(labelled_image1)
    total_labels_coinc=len(coinc_list)
    fraction_coinc=total_labels_coinc/total_labels
    
    
    # Generate the images
    coinc_list[0]=1000000   # First value is zero- don't want to count these. 
    coincident_features_image=np.isin(labelled_image1,coinc_list)   # Generates binary image only from labels in coinc list
    coinc_list[0]=0
    non_coincident_features_image=~np.isin(labelled_image1,coinc_list)  # Generates image only from numbers not in coinc list.
    
    return total_labels_coinc,coincident_image

def analyse_labelled_image(labelled_image,original_image):
    measure_image=measure.regionprops_table(labelled_image,intensity_image=original_image,properties=('area','perimeter','centroid','orientation','major_axis_length','minor_axis_length','mean_intensity','max_intensity'))
    measure_dataframe=pd.DataFrame.from_dict(measure_image)
    return measure_dataframe


root_path = r"/Volumes/Noe PhD 4/Microscopes/ONI/20240308_NPH_SiMPull_EVs_ID3/"

# inpaths to analyse

pathlist=[]

# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/ONI/20240308_NPH_SiMPull_EVs_ID3/B2+5uM_DiD_prewash/Processed images/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/ONI/20240308_NPH_SiMPull_EVs_ID3/B2+5uM_DiD_wash/Processed images/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/ONI/20240308_NPH_SiMPull_EVs_ID3/B2_only/Processed images/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/ONI/20240308_NPH_SiMPull_EVs_ID3/B3+5nM_NR_prewash/Processed images/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/ONI/20240308_NPH_SiMPull_EVs_ID3/B3+5nM_NR_wash/Processed images/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/ONI/20240308_NPH_SiMPull_EVs_ID3/B3_only/Processed images/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/ONI/20240308_NPH_SiMPull_EVs_ID3/B4+150nM_Apo-15_prewash-1/Processed images/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/ONI/20240308_NPH_SiMPull_EVs_ID3/B4+150nM_Apo-15_wash/Processed images/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/ONI/20240308_NPH_SiMPull_EVs_ID3/B4+150nM_Apo-15_wash-2/Processed images/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/ONI/20240308_NPH_SiMPull_EVs_ID3/B4_only/Processed images/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/ONI/20240308_NPH_SiMPull_EVs_ID3/B5_only/Processed images/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/ONI/20240308_NPH_SiMPull_EVs_ID3/B4+150nM_Apo-15_wash-1_100_frames/Processed images/")



image_tag_638 = "647_projection.tif"
image_tag_561 = "488_projected.tif"

EV_table = pd.DataFrame(columns=["File", "Number of EVs", "Coincidence", "Fraction coincidence", "ID"])

all_measurements = pd.DataFrame(columns = ['file','area','perimeter','centroid','orientation','major_axis_length','minor_axis_length','mean_intensity','max_intensity'])



for path in pathlist:
    
    # Make dataframe for measure here
    
    measurement_table = pd.DataFrame(columns = ['file','area','perimeter','centroid','orientation','major_axis_length','minor_axis_length','mean_intensity','max_intensity'])
    
    
    for i in range(0,2):
  
        path_within = path + 'pos_' + str(i) + "_"
        print(path)
        
        image_638 = path_within + image_tag_638
        image_561 = path_within + image_tag_561
        
        
        # Load image
        im_638 = load_im(image_638)
        plt.imshow(im_638)
        
        # Perform thresholding using function defined above
        thr_638, boolean_im_638 = threshold_638(im_638)
        
        # Convert boolean thresholded image to binary for labelling
        binary_im_638 = boolean_im_638.astype(int)
    
        # Calculate coincidence using coincidence function
            # First we need to threshold the green channel (561) using threshold function as done for red channel
        
        im_561 = load_im(image_561)
        
        thr_561, boolean_im_561 = threshold_561(im_561)
        
        binary_im_561 = boolean_im_561.astype(int)
        
        total_features, labelled_561 = label_image(binary_im_561)
        
        coinc_image = binary_im_561 * binary_im_638
        
        features_coinc, labelled_coinc = label_image(coinc_image)
        
        fract_coinc = features_coinc/total_features
        
        EV_table = EV_table.append({"File":path_within, "Number of EVs": int(total_features),"Coincidence": int(features_coinc), "Fraction coincidence": fract_coinc, "ID": str(path[64] + path[65])},ignore_index=True)

EV_table.to_csv(root_path + "Coincidence_per_EV_B2.csv", sep = "\t")
        
        
        