#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:59:23 2024

@author: pele

Purpose: 
    
    (1) To load DBSCAN table with all clusters 
    (2) To filter out eccentricity values below specific value to exclude EVs that are not rounded
    (3) To plot clusters above that specific ecc value
    (4) Save clusters data (as table) and clusters image (as tiff)
    
"""


import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from sklearn.cluster import DBSCAN
from skimage import filters,measure


# Camera settings (TIRFM)
Pixel_size=103
camera_gain=2.17
camera_sensitivity=11.5
camera_offset=500


# Options (set to 1 to perform)


   

# Settings
image_width=512
image_height=512
gradient=7500
drift_correction=0
scale=8
# precision_threshold=250 --> It is not used throughout the script
eps_threshold=1
minimum_locs_threshold=5
prec_thresh=30

rows = range(1,4)
wells = range(1,4)


pathlist = []

pathlist.append


# Functions to be used:

def gkern(l,sigx,sigy):
    
    """\
    creates gaussian kernel with side length l and a sigma of sig
    """

    # ax = np.linspace(-(l - 1) / 2., (l - 1) / 2., l)
    ax = np.linspace(-(l - 1) / 2., (l - 1) / 2., l)
    xx, yy = np.meshgrid(ax, ax)

    kernel = np.exp(-0.5 * (np.square(xx)/np.square(sigx) + np.square(yy)/np.square(sigy)) )
    # print(np.sum(kernel))
    # test=kernel/np.max(kernel)
    # print(test.max())
    return kernel/np.sum(kernel)
    
def generate_SR_prec_cluster(coords,precsx,precsy,clusters):
    box_size=50
    SR_prec_plot_def=np.zeros((image_width*scale+100,image_height*scale+100),dtype=float)
    SR_fwhm_plot_def=np.zeros((image_width*scale+100,image_height*scale+100),dtype=float)

    j=0
    for clu in clusters:
        if clu>-1:
       
            precisionx=precsx[j]/Pixel_size*scale
            precisiony=precsy[j]/Pixel_size*scale
            xcoord=coords[j,0]
            ycoord=coords[j,1]
            scale_xcoord=round(xcoord*scale)+50
            scale_ycoord=round(ycoord*scale)+50
            
            sigmax=precisionx
            sigmay=precisiony
            
            
            # tempgauss=SRGaussian((2*box_size,2*box_size), (sigmax,sigmay),(box_size,box_size))
            tempgauss=gkern(2*box_size,sigmax,sigmay)
            ybox_min=scale_ycoord-box_size
            ybox_max=scale_ycoord+box_size
            xbox_min=scale_xcoord-box_size
            xbox_max=scale_xcoord+box_size 
        
        
            if(np.shape(SR_prec_plot_def[ybox_min:ybox_max,xbox_min:xbox_max])==np.shape(tempgauss)):
                SR_prec_plot_def[ybox_min:ybox_max,xbox_min:xbox_max]=SR_prec_plot_def[ybox_min:ybox_max,xbox_min:xbox_max]+tempgauss
                
            tempfwhm_max=tempgauss.max()
            tempfwhm=tempgauss>(0.5*tempfwhm_max)
            
            tempfwhm_num=tempfwhm*(clu+1)
           
            
            if(np.shape(SR_fwhm_plot_def[ybox_min:ybox_max,xbox_min:xbox_max])==np.shape(tempfwhm)):
               plot_temp=np.zeros((2*box_size,2*box_size),dtype=float)
               plot_add=np.zeros((2*box_size,2*box_size),dtype=float)
               plot_temp=SR_fwhm_plot_def[ybox_min:ybox_max,xbox_min:xbox_max]
               plot_add_to=plot_temp==0
               
               plot_add1=plot_temp+tempfwhm_num
               
               plot_add=plot_add1*plot_add_to
               
               SR_fwhm_plot_def[ybox_min:ybox_max,xbox_min:xbox_max]=SR_fwhm_plot_def[ybox_min:ybox_max,xbox_min:xbox_max]+plot_add
                
                
                # (SR_fwhm_plot_def[scale_ycoord-box_size:scale_ycoord+box_size,scale_xcoord-box_size:scale_xcoord+box_size]+tempfwhm_num).where(SR_fwhm_plot_def[scale_ycoord-box_size:scale_ycoord+box_size,scale_xcoord-box_size:scale_xcoord+box_size]==0)
                # SR_tot_plot_def[scale_ycoord-box_size:scale_ycoord+box_size,scale_xcoord-box_size:scale_xcoord+box_size]=SR_tot_plot_def[scale_ycoord-box_size:scale_ycoord+box_size,scale_xcoord-box_size:scale_xcoord+box_size]+tempfwhm
            
            # SR_tot_plot_def[SR_tot_plot_def==0]=1
            labelled=SR_fwhm_plot_def
            
            SR_prec_plot=SR_prec_plot_def[50:image_width*scale+50,50:image_height*scale+50]
            labelled=labelled[50:image_width*scale+50,50:image_height*scale+50]
            
            
        j+=1
    
    return SR_prec_plot,labelled,SR_fwhm_plot_def



for path in pathlist:
    
    for row in rows:
        
        for well in wells:
            
            FOV = "X0Y0R" + str(row) + "W" + str(well) + "_"
            
            DBSCAN_folder = path + FOV + "515_DBSCAN_new_mapped/"
            
            clu_data_path = DBSCAN_folder + "1_5_515_Metrics.csv"
            
            clu_data = pd.read_table(clu_data_path)
            
            new_clu_data = clu_data["Eccentricity"] > 0.6
            
            
            


