#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 17:39:33 2023

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



# Root path - where to save

root_path="/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_0/"

# These are the names of the files to image:

green_image="561_mapped.tif"
red_image="638_cropped.tif"




# Folders to analyse:
    
def load_image(toload):
    
    image=imread(toload)
    
    return image

def z_project(image):
    
    mean_int=np.mean(image,axis=0)
  
    return mean_int

# Subtract background:
def subtract_bg(image):
    background = threshold_local(image, 11, offset=np.percentile(image, 1), method='median')
    bg_corrected =image - background
    return bg_corrected

def threshold_image_std(input_image):
    # threshold_value=filters.threshold_otsu(input_image)  
    
    threshold_value=input_image.mean()+3*input_image.std()
    print(threshold_value)
    binary_image=input_image>threshold_value

    return threshold_value,binary_image

def threshold_image_standard(input_image,thresh):
     
    binary_image=input_image>thresh

    return binary_image

# Threshold image using otsu method and output the filtered image along with the threshold value applied:
    
def threshold_image_fixed(input_image,threshold_number):
    threshold_value=threshold_number   
    binary_image=input_image>threshold_value

    return threshold_value,binary_image

# Label and count the features in the thresholded image:
def label_image(input_image):
    labelled_image=measure.label(input_image)
    number_of_features=labelled_image.max()
 
    return number_of_features,labelled_image
    
# Function to show the particular image:
def show(input_image,color=''):
    if(color=='Red'):
        plt.imshow(input_image,cmap="Reds")
        plt.show()
    elif(color=='Blue'):
        plt.imshow(input_image,cmap="Blues")
        plt.show()
    elif(color=='Green'):
        plt.imshow(input_image,cmap="Greens")
        plt.show()
    else:
        plt.imshow(input_image)
        plt.show() 
    
        
# Take a labelled image and the original image and measure intensities, sizes etc.

def analyse_labelled_image(labelled_image,original_image):
    measure_image=measure.regionprops_table(labelled_image,intensity_image=original_image,properties=('area','perimeter','centroid','orientation','major_axis_length','minor_axis_length','mean_intensity','max_intensity'))
    measure_dataframe=pd.DataFrame.from_dict(measure_image)
    return measure_dataframe

# This is to look at coincidence purely in terms of pixels

def coincidence_analysis_pixels(binary_image1,binary_image2):
    pixel_overlap_image=binary_image1&binary_image2         
    pixel_overlap_count=pixel_overlap_image.sum()
    pixel_fraction=pixel_overlap_image.sum()/binary_image1.sum()
    
    return pixel_overlap_image,pixel_overlap_count,pixel_fraction

# Look at coincidence in terms of features. Needs binary image input 

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
    
    return coinc_list,coinc_pixels,fraction_coinc,coincident_features_image,non_coincident_features_image,fract_pixels_overlap

# Rotate the image for chance
def rotate(matrix):
    temp_matrix = []
    column = len(matrix)-1
    for column in range(len(matrix)):
       temp = []
       for row in range(len(matrix)-1,-1,-1):
          temp.append(matrix[row][column])
       temp_matrix.append(temp)
    for i in range(len(matrix)):
       for j in range(len(matrix)):
          matrix[i][j] = temp_matrix[i][j]
    return matrix      


Output_all = pd.DataFrame(columns=['Number green','Number red','Number coincident','Number chance','Q'])


for path in root_path:

    save_path = os.path.join(root_path, "coincidence/")
    if not os.path.exists(save_path):
        os.makedirs(save_path)
        
        
        
  # Load the images
    green=load_image(root_path+green_image)
    red=load_image(root_path+red_image)

  # z-project - get the average intensity over the range. 
    
    green_flat=np.mean(green,axis=0)
    red_flat=np.mean(red,axis=0)

  # The excitation is not homogenous, and so need to subtract the background:
    
    green_bg_remove=subtract_bg(green_flat)
    
    red_bg_remove=subtract_bg(red_flat)
    
  # Threshold each channel: 
    
    thr_gr,green_binary=threshold_image_std(green_bg_remove)
    
    thr_red,red_binary=threshold_image_std(red_bg_remove)
   
  # Save the images 
    
    imsr = Image.fromarray(green_bg_remove)
    imsr.save(save_path +'_BG_Removed.tif')
    
    imsr = Image.fromarray(red_bg_remove)
    imsr.save(save_path+'_BG_Removed.tif')
    
    
    imsr = Image.fromarray(green_binary)
    imsr.save(save_path+'_Binary.tif')
    
    imsr = Image.fromarray(red_binary)
    imsr.save(save_path+'_Binary.tif')
    
  # Perform analysis 
   
    number_green,labelled_green=label_image(green_binary)
    print("%d feautres were detected in the green image."%number_green)
    measurements_green=analyse_labelled_image(labelled_green,green_flat)
    
       
    number_red,labelled_red=label_image(red_binary)
    print("%d feautres were detected in the red image."%number_red)
    measurements_red=analyse_labelled_image(labelled_red,red_flat)
    
  # Perform coincidence analysis
    
    green_coinc_list,green_coinc_pixels,green_fraction_coinc,green_coincident_features_image,green_non_coincident_features_image,green_fract_pixels_overlap=feature_coincidence(green_binary,red_binary)
    red_coinc_list,red_coinc_pixels,red_fraction_coinc,red_coincident_features_image,red_non_coincident_features_image,red_fract_pixels_overlap=feature_coincidence(red_binary,green_binary)
   
    number_of_coinc=len(green_coinc_list)
    
  # Need to account for chance due to high density

    green_binary_rot=rotate(green_binary) 
    
    chance_coinc_list,chance_coinc_pixels,chance_fraction_coinc,chance_coincident_features_image,chance_non_coincident_features_image,chance_fract_pixels_overlap=feature_coincidence(green_binary_rot,red_binary)
    
    number_of_chance=len(chance_coinc_list)
    
#  Calculate an association quotient 

    Q=(number_of_coinc-number_of_chance)/(number_green+number_red-(number_of_coinc-number_of_chance))
    

    imsr = Image.fromarray(green_coincident_features_image)
    imsr.save(save_path+'_Coincident.tif')
   
    imsr = Image.fromarray(red_coincident_features_image)
    imsr.save(save_path+'_Coincident.tif')
    
    
    
# Output

    Output_all = Output_all.append({'Number green':number_green,'Number red':number_red,'Number coincident':number_of_coinc,'Number chance':number_of_chance,'Q':Q},ignore_index=True)


    Output_all.to_csv(save_path + 'All.csv', sep = '\t')



