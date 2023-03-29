#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:09:18 2023

@author: pele

This code is aimed to make ibd32 and ibd33 specific wells analysis faster because the other script takes too long due to the lat for loop
"""


from skimage.io import imread
import skimage as im
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from skimage import filters,measure
from skimage.filters import threshold_local
import seaborn as sns


# Functions to be used defined below:
    
# To load each image using imread package

def load_image(toload):
    
    image=imread(toload)
    
    return image



# To label and count the features in the thresholded image:
   
def label_image(input_image):
    labelled_image=measure.label(input_image)
    number_of_features=labelled_image.max()

    return number_of_features,labelled_image
   
   
   
# To take a labelled image and the original image and measure intensities, sizes etc.:
# The regionprops_table() module allows for plenty of prperties to be analysed for each labelled object, see package to look for any specific rperty to be analysed
    
def analyse_labelled_image(labelled_image,original_image):
    measure_image=measure.regionprops_table(labelled_image,intensity_image=original_image,properties=('area','perimeter','centroid','orientation','major_axis_length','minor_axis_length','intensity_mean','max_intensity'))
    measure_dataframe=pd.DataFrame.from_dict(measure_image)
    return measure_dataframe

pathlist_ibd32 = []
pathlist_ibd33 = []


# Paths below:


pathlist_ibd32.append("/Volumes/Noe PhD 2/Microscopes/Opera/20221213_ibds32-33/0h/ibidi32_0h__2022-12-13T13_31_11-Measurement 1/")
pathlist_ibd32.append("/Volumes/Noe PhD 2/Microscopes/Opera/20221213_ibds32-33/3h/ibd32_3h__2022-12-13T16_21_01-Measurement 1/")
pathlist_ibd32.append(r"/Volumes/Noe PhD 2/Microscopes/Opera/20221213_ibds32-33/24h/ibd32_24h__2022-12-14T11_53_54-Measurement 1/")
pathlist_ibd32.append(r"/Volumes/Noe PhD 2/Microscopes/Opera/20221213_ibds32-33/48h/ibd32_48h__2022-12-15T11_47_07-Measurement 1/")
pathlist_ibd32.append(r"/Volumes/Noe PhD 2/Microscopes/Opera/20221213_ibds32-33/72h/ibd32_72h__2022-12-16T12_12_46-Measurement 2/")



pathlist_ibd33.append(r"/Volumes/Noe PhD 2/Microscopes/Opera/20221213_ibds32-33/0h/ibd33_0h__2022-12-13T14_00_05-Measurement 1/")
pathlist_ibd33.append(r"/Volumes/Noe PhD 2/Microscopes/Opera/20221213_ibds32-33/3h/ibd33_3h__2022-12-13T16_49_43-Measurement 1/")
pathlist_ibd33.append(r"/Volumes/Noe PhD 2/Microscopes/Opera/20221213_ibds32-33/24h/ibd33_24h__2022-12-14T12_29_15-Measurement 1/")
pathlist_ibd33.append(r"/Volumes/Noe PhD 2/Microscopes/Opera/20221213_ibds32-33/48h/ibid33_48h__2022-12-15T12_22_16-Measurement 1/")
pathlist_ibd33.append(r"/Volumes/Noe PhD 2/Microscopes/Opera/20221213_ibds32-33/72h/ibd33_72h__2022-12-16T12_54_19-Measurement 1/")




# Concatenate all paths together into the same one under the name "pathlist":

pathlist = []

pathlist.append(pathlist_ibd32)
pathlist.append(pathlist_ibd33)



# Define a paths where to save all data:

to_save = "/Volumes/Noe PhD 2/Microscopes/Opera/20221213_ibds32-33/"
to_save_E = r"/Volumes/Noe PhD 2/Microscopes/Opera/20221213_ibds32-33/E populations/"

# Dataframes to be used to save FRET data below:

    # Timepoints used in the experiment (used to add values accordingly to FRET df)
Timepoints = ["0h", "3h", "24h","48h","72h"]
    
    # Low FRET dfs:
low_FRET_all = []
Final_low_df_FRET = pd.DataFrame(columns=["Time Point", "E"])


    # High FRET dfs:
        
high_FRET_all = []
Final_high_df_FRET = pd.DataFrame(columns=["Time Point", "E"])



events_low = pd.DataFrame(columns = ["FOV", "Time Point","# events", "E type"])
events_high = pd.DataFrame(columns = ["FOV", "Time Point","# events", "E type"])

Final_events = pd.DataFrame(columns = ["FOV", "Time Point","# events", "E type"])

# x is used as a number to track the path being used in order to track the time point
x = 0


# Value used for splitting the two fret populations (between 0.2-0.4):
split_value = 0.3

for path in pathlist_ibd33:
    
    
    well_ID = ["A4"]#,"A2","A3","A4","B1","B2","B3","B4"]

    
    
    FOV = range(1,31,1)
      
    FRET_FOV_individual = pd.DataFrame(columns=["FOV","Time","E"])

    subplot_list = []
    
    fig = plt.figure()
        
    # DFs that will be overwritten when path changes (i.e. for each time point)
    

    low_FRET = []
    high_FRET = []
    
    df_low_FRET = pd.DataFrame(columns=["Time Point", "E"])
    df_high_FRET = pd.DataFrame(columns=["Time Point", "E"])
    
    
    for j in FOV:
        
        
        pre_string = str(well_ID[0]) + str("_channels/" )+ str(well_ID[0]) + str("F") + str(j) + str("_")
        
        
        # Load donor image (i.e. AF488 exc + emission)
        
        
        donor=load_image(path+pre_string+'AF488.tif') 
        
        # Calculate mean and std values of donor:
            
        ave_donor = donor.mean()
        std_donor = donor.std()
        
        # Threshold donor image - done in one line first mean and std used to generate mask and then multiplied with intensities to threshold:
            
        donor_thr = donor * (donor > ave_donor + 2 * std_donor)
        
        
        
        # Load acceptor image (i.e. 647 exc + emission)
        acceptor = load_image(path + pre_string + "AF647.tif") 
                        
        # Calculate mean and std values of acceptor:                
        ave_acceptor = acceptor.mean()
        std_acceptor = acceptor.std()
        
        # Threshold acceptor image - done in one line first mean and std used to generate mask and then multiplied with intensities to threshold:

        acceptor_thr = acceptor * (acceptor>ave_acceptor + 2 * std_acceptor)
       
        
        
        # Load FRET image (i.e. AF488 exc + 647 emission)
        FRET=load_image(path+pre_string+'FRET.tif') 
        
      
        
        # Calculate mean and std values of FRET:
            
        ave_FRET = FRET.mean()
        std_FRET = FRET.std()
        
        # Threshold FRET image - done in one line first mean and std used to generate mask and then multiplied with intensities to threshold:

        FRET_thr = FRET * (FRET > ave_FRET + 2 * std_FRET)
    
    


        # Calculate FRET efficiency using both FRET and donor images (paper's formula)
        # Use thresholded images, these have been subtracted all background using masks
        
       
        fret_im=FRET/(FRET + donor)
        
        fret_im_thresh=fret_im*(acceptor>ave_acceptor + 2 * std_acceptor)*(donor > ave_donor + 2 * std_donor)
        
        fret_no0s = fret_im_thresh[fret_im_thresh>0]
        
        subplot_list.append(fret_no0s)
        
        fret_list = fret_no0s.tolist()
        # plt.hist(fret_list, bins = 50, rwidth=0.9,color = 'skyblue')
        # plt.show()
        
        # Split fret_list into 2 datasets (high and low E):
                      
        df_low_FRET_all = pd.DataFrame(columns=["Time Point", "E"])
        df_high_FRET_all = pd.DataFrame(columns=["Time Point", "E"])
        
        
        for value in fret_list:
                
            if value < split_value:
                low_FRET.append(value)                                
                
            else:
                high_FRET.append(value)
                
        events_low = events_low.append({"FOV": j, "Time Point": Timepoints[x], "# events": int(len(low_FRET)), "E type": "low"}, ignore_index=True)
        events_high = events_high.append({"FOV": j, "Time Point": Timepoints[x], "# events": int(len(high_FRET)), "E type": "high"}, ignore_index=True)
    
    Events_FRET = pd.DataFrame(columns=["FOV", "Time Point","# events", "E type"])
    Events_FRET = Events_FRET.append(events_low)
    Events_FRET = Events_FRET.append(events_high)
    

    
    df_low_FRET_all['E'] = low_FRET
    df_low_FRET_all["Time Point"] = str(Timepoints[x])
    
    df_high_FRET_all['E'] = high_FRET
    df_high_FRET_all["Time Point"] = str(Timepoints[x])
    
    
    
    Final_low_df_FRET = Final_low_df_FRET.append(df_low_FRET_all)
    Final_high_df_FRET = Final_high_df_FRET.append(df_high_FRET_all)
        

    print("Finished " + str(well_ID[0]) + " @ " + str(Timepoints[x]))    
    
    

    
    Final_low_df_FRET["E type"] = str("Low")
    Final_high_df_FRET["E type"] = str("High")
    
    Final_Es = pd.DataFrame()
    Final_Es = Final_Es.append(Final_low_df_FRET)
    Final_Es = Final_Es.append(Final_high_df_FRET)
    
    # Final_Es.to_csv(to_save + "all_E.csv", sep="\t")
    
    
    
    Final_events = Final_events.append(Events_FRET)
    x += 1

    
# Plot a boxplot:
sns.boxplot(data = Final_events, x ="Time Point", y = "# events", hue = "E type", width = 0.5, palette ='pastel', dodge = False).set(title = 'E populations over time')
plt.ylim(0, 200000)
plt.savefig(to_save_E + "ibd33" + str(well_ID[0]) + "_" + str(split_value) + "_E_populations.tif")

    
print(str(well_ID[0]) + "plotted!")

    # Plot individual points in a strip plot
    # sns.stripplot(data = Final_events, x ="Time Point", y = "# events", hue = "E type").set(title='E populations over time')
    

# Events_FRET["E type"] = "High", "Low"

# Events_FRET.loc[0,"# events"] = int(len(Final_Es[Final_Es["E type"] == "High"]))
# Events_FRET.loc[1,"# events"] = int(len(Final_Es[Final_Es["E type"] == "Low"]))
                    
# sns.boxplot(data = Final_Es, x ="Time Point", y = "E", hue = "E type", width = 0.5, palette ='pastel', dodge = False)





# sns.stripplot(data = Final_Es, x ="Time Point", y = "E", hue = "E type")

# low_FRET_plot = Final_low_df_FRET.boxplot(column=["E"], by = "Time Point")
# low_FRET_plot = Final_high_df_FRET.boxplot(column=["E"], by = "Time Point")
# plt.title(str(well_ID))

# plt.show()
# # plt.savefig(directory + str(i) + "population_E_histogram.png")









































