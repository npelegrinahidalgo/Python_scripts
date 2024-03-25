#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 18:08:47 2023

@author: pele

This script will

(1) Take clustered NR data & use as mask.

(2) Label all particles (EVs) once thresholded

(3) Measure the specified properties of these particles already labelled, including intensity

Done on SR images (check if clustered or FitResults data)

No need to threshold since it has already been reconstructed and clustered (i.e. double filter)


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

image_height=512
image_width=512
Pixel_size=103
scale=8
precision_threshold=250
eps_threshold=0.5
minimum_locs_threshold=15
prec_thresh=40



######    Functions to be used defined below    ########


# Load image into spyder:
def load_im(to_load):
    
    image = imread(to_load)
    
    return image

# Load and generate SR image (non-clustered one):
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
    
    return number_of_features, coincident_features_image

def analyse_labelled_image(labelled_image,original_image):
    measure_image=measure.regionprops_table(labelled_image,intensity_image=original_image,properties=('area','perimeter','centroid','orientation','major_axis_length','minor_axis_length','mean_intensity','max_intensity'))
    measure_dataframe=pd.DataFrame.from_dict(measure_image)
    return measure_dataframe


root_path = r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/"

# inpaths to analyse

pathlist=[]

# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/A2_NoEVs+D6G4AB(2nM)+nB(6nM)+E2285(1nM)_2024-02-16_14-38-34/Processed images/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/B2+D6G4AB(2nM)+nB(6nM)+E2285(1nM)+NR(5nM)_2024-02-16_15-22-12/Processed images/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/B2+D6G4AB(5nM)+nB(15nM)+D7674(1nM)+NR(5nM)_2024-02-16_19-00-33/Processed images/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/B3+UE3R2AB(2nM)+nB(6nM)+D7674(1nM)+NR(5nM)_2024-02-16_18-02-44/Processed images/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/B4+D6G4AB(2nM)+AF647+NR(5nM)_2024-02-16_16-47-47/Processed images/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/C2+D6G4AB(2nM)+nB(6nM)+E2285(1nM)+NR(5nM)_2024-02-16_15-47-51/Processed images/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/A3+UE3R2AB(2nM)+nB(6nM)+D7674(1nM)+NR(5nM)_2024-02-16_20-40-14/Processed images/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/C2+D6G4AB(5nM)+nB(15nM)+D7674(1nM)+NR(5nM)_2024-02-16_19-44-36/Processed images/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/C3+UE3R2AB(2nM)+nB(6nM)+D7674(1nM)+NR(5nM)_2024-02-16_18-18-46/Processed images/")
# pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/C4+D6G4AB(2nM)+AF647+NR(5nM)_2024-02-16_17-40-43/Processed images/")




image_tag_638 = "638_0_FitResults.txt"
image_tag_515 = "1_5_515_SR_width_python_clustered.tif"

EV_table = pd.DataFrame(columns=["File", "Number of EVs", "Coincidence", "Fraction coincidence", "ID"])

all_measurements = pd.DataFrame(columns = ['file','area','perimeter','centroid','orientation','major_axis_length','minor_axis_length','mean_intensity','max_intensity'])



for path in pathlist:
    
    # Make dataframe for measure here
    
    measurement_table = pd.DataFrame(columns = ['file','area','perimeter','centroid','orientation','major_axis_length','minor_axis_length','mean_intensity','max_intensity'])
    
    
    print(path)
    check_file = os.path.join(path,"X0Y0R3W3_638_0_SR.tif")
    
    if os.path.isfile(check_file):
        
        rows = range(1,4)
        wells = range(1,4)
    else:
        
        rows = range(1,3)
        wells = range(1,3)
    
    for row in rows:
        
        for well in wells:
            
            well=1
            row=1
            
            FOV = "X0Y0R" + str(row) + "W" + str(well) + "_"
            
            DBSCAN_folder = FOV + str("1_5_515_DBSCAN")
            
            # Define paths to each image from eahc channel
            path_638 = os.path.join(path, FOV + image_tag_638)
            path_515 = os.path.join(path, DBSCAN_folder, image_tag_515)
            
            
            # Generate SR image:
                # Load coords first:
            fits_path= path_638
            loc_data=pd.read_table(fits_path)
                
            coords= np.array(list(zip(loc_data['X'],loc_data['Y'])))
                
                # Generate SR using function & convert to image from array:
            SR_638 = generate_SR(coords)
            # SR_img = Image.fromarray(SR_638)
            
            # Load clustered image:
            NR_clusters = load_im(path_515)
            
            # Convert images to numPy arrays first:
            
            SR_np = np.array(SR_638)
            NR_np = np.array(NR_clusters)
            
            # Convert to binary:
            
            SR_binary = np.where(SR_np>0, 1, 0)
            NR_binary = np.where(NR_np>0, 1, 0)

            
            # Use coincidence features function -- Still trying to understand fully how this works -- 
            
            red_coinc_list, coinc_image=feature_coincidence(NR_binary,SR_binary)
            
            # Now, to obtain properties about coincidence image:
                #  First, run label image:
            
            features, labels_red = label_image(coinc_image)
            
                # Then, analyse labelled image using function
            
            measurements_red=analyse_labelled_image(labels_red,NR_np)
            
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
            measurement_table.to_csv(path + FOV + "All_measurements.csv", sep = "\t")
            
            all_measurements = pd.concat([all_measurements,measurement_table], axis = 0)
            
            # Mean, SD etc. of intensities. 
            
        
                
            if str("A2") in path:
                
                EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": fraction_rounded, "ID": str("No EVs")},ignore_index=True)
            
            if str("B2") in path:
                
                EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": fraction_rounded, "ID": str("D6G4 No Perm")},ignore_index=True)
            
            if str("C2") in path:
                
                EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": fraction_rounded, "ID": str("0.1% Triton")},ignore_index=True)
            
            if str("A3") in path:
                
                EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": fraction_rounded, "ID": str("No EVs")},ignore_index=True)
            
            if str("B3") in path:
                
                EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": fraction_rounded, "ID": str("UE3R2 No Perm")},ignore_index=True)
            
            if str("C3") in path:
                
                EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": fraction_rounded, "ID": str("UE3R2 0.1% Triton")},ignore_index=True)
            
            if str("A4") in path:
                
                EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": fraction_rounded, "ID": str("No EVs")},ignore_index=True)
            
            if str("B4") in path:
                
                EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": fraction_rounded, "ID": str("D6G4 DL No Perm")},ignore_index=True)
            
            if str("C4") in path:
                
                EV_table = EV_table.append({"File":path, "Number of EVs": int(features),"Coincidence": int(red_coinc_list), "Fraction coincidence": fraction_rounded, "ID": str("D6G4 DL 0.1% Triton")},ignore_index=True)
    

EV_table.to_csv(root_path + "Coincidence_per_EV.csv", sep = "\t")

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

