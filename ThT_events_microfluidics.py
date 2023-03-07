#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 08:32:47 2020

@author: Mathew
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import os
pathlist=[]
#This code is using a threshold within each sample as a limit threshold to count the events

# Where to store the overall file containing means etc. for each experiment. 
# Saving directory:
path_root=r"/Volumes/Noelia PhD/Microscopes/CONFOCAL/20220408_PFF/"

# # Foldert to analyse here:
pathlist.append(r"/Volumes/Noelia PhD/Microscopes/CONFOCAL/20220408_PFF/In_house_pre_cent/")
pathlist.append(r"/Volumes/Noelia PhD/Microscopes/CONFOCAL/20220408_PFF/in_house_spnt/")
pathlist.append(r"/Volumes/Noelia PhD/Microscopes/CONFOCAL/20220408_PFF/In-house_pell/")
pathlist.append(r"/Volumes/Noelia PhD/Microscopes/CONFOCAL/20220408_PFF/rPep/")
pathlist.append(r"/Volumes/Noelia PhD/Microscopes/CONFOCAL/20220408_PFF/rpep_snt/")
pathlist.append(r"/Volumes/Noelia PhD/Microscopes/CONFOCAL/20220408_PFF/rpep_pell/")


file_stem="tht"          # This is the part of the filename that will be searched for in each folder.
# number_of_files=5       # Number of files in the folder (could make this automatic in the future).

# Thresholds and other parameters:
    
# channelA_thresh=200      # Threshold for Channel A (Green).
channelB_thresh=0     # Threshold for Channel B (Red).
channelA_AF=0.40        # Autofluorescence
channelB_AF=2.75
xtalk=0.03             # Cross-talk from A to B
size_split_med=5
size_split_lar=20

def load_files(filename_contains,path):
    print(path)
    num=0
    channelA_sample=[]             # Where channel A data will be stored
    channelB_sample=[]             # Where channel B data will be stored
    for root, dirs, files in os.walk(path):
      for name in files:
              # print(name)
              if filename_contains or 'ThT' in name:
                  if 'pdf' not in name:
                      resultsname = name
                      print(name)
                      num+=1
                      a=0
                      with open(path+name) as csvDataFile:                                                # Opens the file as a CSV
                            csvReader = csv.reader(csvDataFile,delimiter='\t')                           # Assigns the loaded CSV file to csvReader. 
                            for row in csvReader:
                                channelA_sample.append(row[0])                                                     # For every row in in csvReader, the values are apended to green and red.         
                                channelB_sample.append(row[1])
                                a+=1
            
                            print ("Loaded %s, which contains %s rows."%(resultsname,a))
    rows=len(channelA_sample)
    print("Loaded %s files in total, with a total of %s rows"%(num,rows))
    
    
    channelA_arr_sample=np.asarray(channelA_sample,dtype=np.float32)                              # Converts these to numpy arrays for vector calcs.
    channelB_arr_sample=np.asarray(channelB_sample,dtype=np.float32)
    return channelA_arr_sample,channelB_arr_sample,num

def maxQ():
    q_vals = np.zeros(shape=(20,20))

    for A in range(20):
        for B in range(20):
            channelA_only_events=channelA_arr[(channelA_arr>A)]                       # Total A events
            channelB_only_events=channelB_arr[(channelB_arr>B)]                       # Total B events
            channelA_events=channelA_arr[np.logical_and(channelA_arr>A, channelB_arr>B)]  # A coincident events             
            
            
            # Now need to account for chance events:
            
            channelB_shuffle=channelB_arr.copy()
            np.random.shuffle(channelB_shuffle)
            
            channelA_chance=channelA_arr[np.logical_and(channelA_arr>A, channelB_shuffle>B)]    # These are the chance events    
            
            # Now need to calculate Q value:
            
            var_real_events=float(len(channelA_events))
            var_A_events=float(len(channelA_only_events))
            var_B_events=float(len(channelB_only_events))
            var_chance_events=float(len(channelA_chance))
            Q=float((var_real_events-var_chance_events)/(var_A_events+var_B_events-(var_real_events-var_chance_events)))
    
            q_vals[A][B]=Q
            

    maximum_Q=np.amax(q_vals)
    result=np.where(q_vals == np.amax(q_vals))
    ThresholdA,ThresholdB=result
    
    print('The maximum value of Q is %.3f, with a threshold of %s in channel A, and %s in channel B.'%(maximum_Q,str(ThresholdA),ThresholdB))
    
    
    contourplot = plt.contourf(q_vals,20,origin='lower')
    cbar = plt.colorbar(contourplot)
    plt.xlabel("Channel B Threshold")
    plt.ylabel("Channel A Threshold")
    cbar.ax.set_ylabel('Q')
    
Output_all = pd.DataFrame(columns=['Path','Number_of_files','Threshold_A','Threshold_B','Events_A','Events_B','Events_coincindent',
                                       'Events_chance','Q','Total_Intensity_mean','Total_Intensity_SD','Total_Intensity_med','Intensity_A_mean','Intensity_A_SD','Intensity_A_med','Intensity_B_mean','Intensity_B_SD','Intensity_B_med',
                                       'Sizes_mean','Sizes_SD','Sizes_med','A_ave','B_ave','small','medium','large'])

for path in pathlist:
    # path=path.replace('/Ab/','/ThT/')
    print(path)
    channelA_arr,channelB_arr,num=load_files(file_stem,path)
    
    
    
    # Now need to account for autofluorescence and crosstalk etc. 
    
    channelB_arr=(channelB_arr-xtalk*channelA_arr)-channelB_AF
    channelA_arr=channelA_arr-channelA_AF
    
    
    
    
    #This part is for the thresholding:
    
    channelA_thresh=channelA_arr.mean() + 5 * channelA_arr.std()
    print(channelA_thresh)
    channelA_only_events=channelA_arr[(channelA_arr>channelA_thresh)]                       # Total A events
    channelB_only_events=channelB_arr[(channelB_arr>channelB_thresh)]                       # Total B events
    channelA_events=channelA_arr[np.logical_and(channelA_arr>channelA_thresh, channelB_arr>channelB_thresh)]  # A coincident events             
    channelB_events=channelB_arr[np.logical_and(channelA_arr>channelA_thresh, channelB_arr>channelB_thresh)]  # B coincident events
    
    channelA_only_minus_events=channelA_arr[np.logical_and(channelA_arr>channelA_thresh, channelB_arr<channelB_thresh)] # Non-oincidence events
    channelB_only_minus_events=channelB_arr[np.logical_and(channelA_arr<channelA_thresh, channelB_arr>channelB_thresh)] # Non-oincidence events
    
    channelA_brightness=channelA_only_minus_events.mean()
    channelB_brightness=channelB_only_minus_events.mean()
    
    
    channelA_mean=channelA_events.mean()
    channelA_SD=channelA_events.std()
    channelA_med=np.median(channelA_events)
    
    channelB_mean=channelB_events.mean()
    channelB_SD=channelB_events.std()
    channelB_med=np.median(channelB_events)
    # Now need to account for chance events:
    
    channelB_shuffle=channelB_arr.copy()
    np.random.shuffle(channelB_shuffle)
    
    channelA_chance=channelA_arr[np.logical_and(channelA_arr>channelA_thresh, channelB_shuffle>channelB_thresh)]    # These are the chance events    
    channelB_chance=channelB_shuffle[np.logical_and(channelA_arr>channelA_thresh, channelB_shuffle>channelB_thresh)]
    
    # Now need to calculate Q value:
    
    var_real_events=float(len(channelA_events))
    var_A_events=float(len(channelA_only_events))
    var_B_events=float(len(channelB_only_events))
    var_chance_events=float(len(channelA_chance))
    Q=float((var_real_events-var_chance_events)/(var_A_events+var_B_events-(var_real_events-var_chance_events)))
    
    print(('There were %s A events, %s B events, %s coincidence events, and %s chance events. Q = %f.')%(var_A_events,var_B_events,var_real_events,var_chance_events,Q))
    
    
    # Now want histograms etc. 
    
    ln_events=np.log(channelB_events/channelA_events)
    ln_chance=np.log(channelB_chance/channelA_chance)
    
    textstr='Q = %.3f'%Q
    
    plt.rcParams["font.family"] = "Arial"
    plt.rcParams["font.size"] = "12"
    plt.figure(figsize=(8, 6))
    plt.hist(ln_events, bins = 60,range=[-3,3], rwidth=0.9,ec='black',color='#ff0000',alpha=0.8,label="Real Events")
    plt.hist(ln_chance, bins = 60,range=[-3,3], rwidth=0.9,ec='black',color='#cccccc',alpha=0.5,label="Chance Events")
    plt.text(0.05,0.90, textstr,transform=plt.gca().transAxes)
    plt.legend(loc='upper right')         
    plt.xlabel('Z=$ln(I_{B}/I_{A}$)')
    plt.ylabel('Number of events')
    plt.savefig(path+'/'+'lnz.pdf')
    plt.show()
    
    
    channelB_arr_inv=channelB_arr*(-1)
    
    plt.plot(channelA_arr,color='green')
    plt.plot(channelB_arr_inv,color='red')
    plt.xlabel('Bin number')
    plt.ylabel('Intensity (photons)')
    plt.xlim(0,500)
    plt.ylim(-100,100)
    plt.savefig(path+'/'+'example_trace.pdf')
    plt.suptitle(path)
    plt.show()
    
    
    
    
    total_intensity=channelB_events+channelA_events
    plt.hist(total_intensity, bins = 60,range=[0,1000], rwidth=0.9,ec='black',color='#ff0000',alpha=0.8,)
    plt.yscale('log')
    plt.xlabel('Total intensity (photons)')
    plt.ylabel('Number of events')
    plt.savefig(path+'/'+'Intensity.pdf')
    plt.show()
    
    total_mean=total_intensity.mean()
    total_SD=total_intensity.std()
    total_med=np.median(total_intensity)
    
    sizes=channelB_events/channelB_brightness+channelA_events/channelA_brightness
    plt.hist(sizes, bins = 20,range=[0,50], rwidth=0.9,ec='black',color='#ff0000',alpha=0.8,)
    plt.yscale('log')
    plt.xlabel('Approximate size (monomers)')
    plt.ylabel('Number of events')
    plt.savefig(path+'/'+'Sizes.pdf')
    plt.show()
    
    
    plt.plot(channelA_arr[0:80000])
    plt.suptitle(path)
    plt.show()
    
    
    sizes_small=sizes[(sizes<size_split_med)] 
    sizes_med=sizes[np.logical_and(sizes<size_split_lar,sizes>size_split_med)]
    sizes_large=sizes[(sizes>size_split_lar)] 
    
    small_num=len(sizes_small)
    med_num=len(sizes_med)
    large_num=len(sizes_large)
    
    sizes_mean=sizes.mean()
    sizes_SD=sizes.std()
    sizes_med=np.median(sizes)
    Output_all= Output_all.append({'Path':path,'Number_of_files':num,'Threshold_A':channelA_thresh,'Threshold_B':channelB_thresh,'Events_A':var_A_events,'Events_B':var_B_events,'Events_coincindent':var_real_events,'Q':Q,
                                       'Events_chance':var_chance_events,'Total_Intensity_mean':total_mean,'Total_Intensity_SD':total_SD,'Total_Intensity_med':total_med,'Intensity_A_mean':channelA_mean,'Intensity_A_SD':channelA_SD,'Intensity_A_med':channelA_med,'Intensity_B_mean':channelB_mean,'Intensity_B_SD':channelB_SD,'Intensity_B_med':channelB_med,'Sizes_mean':sizes_mean,'Sizes_SD':sizes_SD,'Sizes_med':sizes_med,'A_ave':channelA_brightness,'B_ave':channelB_brightness,
                                       'small':small_num,'medium':med_num,'large':large_num},ignore_index=True)

    Output_all.to_csv(path_root + '/' + 'all_metrics_10_10.csv', sep = '\t')
    Output_all.to_excel(path_root + '/' +'thr_varied' +'_all_metrics_10_10.xlsx')



    x_bins = np.linspace(0,100,20)
    y_bins = np.linspace(0,100,20)
    plt.hist2d(channelA_events, channelB_events, bins=[x_bins,y_bins], cmap=plt.cm.Greys)
    plt.colorbar()
    plt.savefig(path+'/'+'2D_Sizes.pdf')
    
    
