#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 18:08:47 2023

@author: pele

This script will

(1) Threshold image using automated otsu thresholding

(2) Label all particles (EVs) once thresholded

(3) Measure the specified properties of these particles already labelled, including intensity


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

def analyse_labelled_image(labelled_image,original_image):
    measure_image=measure.regionprops_table(labelled_image,intensity_image=original_image,properties=('area','perimeter','centroid','orientation','major_axis_length','minor_axis_length','mean_intensity','max_intensity'))
    measure_dataframe=pd.DataFrame.from_dict(measure_image)
    return measure_dataframe


root_path = r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/"

# inpaths to analyse

pathlist=[]

pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/")



thr_set_638 = 882.9230769230769
thr_set_561 = 6407.307692307692


image_tag_638 = "638_cropped.tif"
image_tag_561 = "561_cropped.tif"

EV_table = pd.DataFrame(columns=["File", "Number of EVs", "Coincidence", "Fraction coincidence", "ID"])

all_measurements = pd.DataFrame(columns = ['file','area','perimeter','centroid','orientation','major_axis_length','minor_axis_length','mean_intensity','max_intensity'])



for path in pathlist:
    
    # Make dataframe for measure here
    
    measurement_table = pd.DataFrame(columns = ['file','area','perimeter','centroid','orientation','major_axis_length','minor_axis_length','mean_intensity','max_intensity'])
    
    
    for i in range(0,25):
  
        path_within = path + 'pos_' + str(i) + '/'
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
        
        
            # Use coincidence features function -- Still trying to understand fully how this works -- 
        
        red_coinc_list, coinc_image=feature_coincidence(binary_im_638,binary_im_561)
        
        # Now, to obtain properties about coincidence image:
            #  First, run label image:
        
        features, labels_red = label_image(coinc_image)
        
            # Then, analyse labelled image using function
        
        measurements_red=analyse_labelled_image(labels_red,im_561)
        
        # From coinc function, calculate fraction of coincidence
        
        if features == 0:
            
            fraction = 0
        
        else:
            
            fraction = red_coinc_list/features
        
        # Round it up to fit decimals (it's numbers between 1 & 0 so you need decimals on!)
        fraction_rounded = round(fraction, 4)
        
        # Concatenate all measurement files        
        measurement_table = pd.concat([measurement_table, measurements_red], axis=0)
        measurement_table["file"] = str(path)
    
    # Save concatenated dataframe 
    measurement_table.to_csv(path + "All_measurements.csv", sep = "\t")
    
    all_measurements = pd.concat([all_measurements,measurement_table], axis = 0)
    
    # Mean, SD etc. of intensities. 
    

        
    if str("A2") in path:
        
        EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": fraction_rounded, "ID": str("EVs only")},ignore_index=True)
    
    if str("B2") in path:
        
        EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": fraction_rounded, "ID": str("No EVs")},ignore_index=True)
    
    if str("C2") in path:
        
        EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": fraction_rounded, "ID": str("0.005% Triton")},ignore_index=True)
    
    if str("A4") in path:
        
        EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": fraction_rounded, "ID": str("0.01% Triton")},ignore_index=True)
    
    if str("B4") in path:
        
        EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": fraction_rounded, "ID": str("0.05% Triton")},ignore_index=True)
    
    if str("C4") in path:
        
        EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": fraction_rounded, "ID": str("0.1% Triton")},ignore_index=True)


pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/")


    
EV_table.to_csv(root_path + "Coincidence_per_EV_C2_only.csv", sep = "\t")
all_measurements.to_csv(root_path + 'all_measurements.csv', sep = '\t')

sns.boxplot(x='file', y='mean_intensity', data=all_measurements, showcaps=True, showmeans=True)
sns.stripplot(x='file', y='mean_intensity', data=all_measurements, color='black', alpha=0.5)
plt.xticks(rotation=45)
plt.xticks(ticks=[0, 1, 2, 3, 4], labels=['No perm', '0.01% Triton', 'No EVs','0.05% Triton', '0.1% Triton'])  # Replace with your specific names
plt.xlabel('')  # Set an empty string as x-axis label
plt.legend()
plt.tight_layout()
plt.savefig(root_path + 'Intensity_exWAGO.png', dpi=300)
plt.show()


# data = EV_table

# df = pd.DataFrame(data)

# mean_values = df.groupby('ID')['Number of EVs'].mean().reset_index()


# Plot total No EVs:

# sns.boxplot(x='ID', y='Number of EVs', data=df, showcaps=True, showmeans=True)
# sns.stripplot(x='ID', y='Number of EVs', data=df, color='black', alpha=0.5)
# plt.xticks(rotation=45)
# plt.xlabel('')  # Set an empty string as x-axis label
# plt.tight_layout()
# plt.legend()
# # plt.savefig(root_path + 'Number_of_EVs.png', dpi=300)
# plt.show()



# Plot the fraction coincidence


# sns.boxplot(x='ID', y='Fraction coincidence', data=df, showcaps=True, showmeans=True)
# sns.stripplot(x='ID', y='Fraction coincidence', data=df, color='black', alpha=0.5)
# plt.xticks(rotation=45)
# plt.xlabel('')  # Set an empty string as x-axis label
# plt.tight_layout()
# plt.savefig(root_path + 'Fraction exWAGO.png', dpi=300)
# plt.show()



