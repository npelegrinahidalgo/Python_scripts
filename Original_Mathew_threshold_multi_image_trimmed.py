#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 10:30:00 2021

@author: Mathew
"""
from PIL import Image
import matplotlib.pyplot as plt
from skimage import color, io
from skimage.filters import try_all_threshold, threshold_otsu
import numpy as np
import glob
import os
import fnmatch


# Paths to analyse
# Make an array
pathlist=[]

pathlist.append("/Volumes/NOE/aSyn_cell/Pre-Python/1/")


for path in pathlist:
    
    im_dapi_path=path+"DAPI_1_0.tif"
    im_asyn_path=path+"1_0_asyn.tif"
    

    # Load the image:
    im_DAPI = io.imread(im_dapi_path)
    
    # Crop the image:
    
    im_crop=im_DAPI[0:100,0:100]
    
    # Show the image:
    plt.imshow(im_crop,vmin=0,vmax=1000)
    plt.colorbar()
    plt.savefig(path+"crop.tif")
    plt.show()
    
    # Manually threshold the image
    
    threshold_value=700
    
    binary_image=im_DAPI>threshold_value
    
    plt.imshow(binary_image)
    plt.show()
    # Get the intensity image as thresholded
    
    thresholded_im=binary_image*im_DAPI
    
    plt.imshow(thresholded_im)
    plt.colorbar()
    plt.show()
    
    # Automatic thresholding:
    Auto_threshold=threshold_otsu(im_DAPI)
    binary_image_auto=im_DAPI>Auto_threshold
    plt.imshow(binary_image_auto)
    plt.show()
    
    thresholded_im_auto=binary_image_auto*im_DAPI
    plt.imshow(thresholded_im_auto)
    plt.colorbar()
    plt.show()
    
    # Open up the asyn image
    
    im_syn = io.imread(im_asyn_path)
    
    syn_threshold=threshold_otsu(im_syn)
    binary_syn=im_syn>syn_threshold
    
    
    
    syn_thresholded=binary_syn*im_syn
    plt.imshow(syn_thresholded)
    plt.colorbar()
    plt.show()
    
    # Find where coincidence
    coincidence=syn_thresholded*binary_image_auto
    plt.imshow(coincidence)
    plt.show()
    
    # Select cytos
    
    cyto_binary=binary_image_auto<1
    
    
    
    
    cyto_coinc=syn_thresholded*cyto_binary
    
    
    fig, ax = plt.subplots(1,2)
    ax[0].imshow(coincidence)
    ax[1].imshow(cyto_coinc)
    plt.savefig(path+"thresholded.png")
    plt.show()
    # Histogram of intensities
    
    # Extract values from image into 1D array
    cyto_values=cyto_coinc.flatten()
    
    plt.hist(cyto_values, bins = 100,range=[800,1500], rwidth=0.9,ec='black',color='#ff0000',alpha=0.8)
    plt.show()
    
    # Extract values from image into 1D array
    nuc_values=coincidence.flatten()
    
    plt.hist(nuc_values, bins = 100,range=[800,1500], rwidth=0.9,ec='black',color='#ff0000',alpha=0.8)
    plt.show()
    
    # Convert integers to float
    cyto_values_float=cyto_values.astype('float')
    cyto_values_float[cyto_values_float==0]=np.nan
    np.nanmean(cyto_values_float)
    
    coincidence_values=coincidence.flatten()
    coincidence_values_float=coincidence_values.astype('float')
    coincidence_values_float[coincidence_values_float==0]=np.nan
    np.nanmean(coincidence_values_float)
    
    
    # save an image as a real .tif
    # Convert np.array into image:
    imsr = Image.fromarray(cyto_coinc)
    # Save image
    imsr.save(path+'Cytos.tif')
        