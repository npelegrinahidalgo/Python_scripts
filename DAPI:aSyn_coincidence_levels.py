#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 16:08:53 2022

@author: pele
"""


from PIL import Image
import matplotlib.pyplot as plt
from skimage import color, io
from skimage.filters import try_all_threshold, threshold_otsu
import numpy as np
from tabulate import tabulate
import pandas as pd


# inpaths to analyse


inpath = "/Volumes/Noelia PhD/Microscopy/CRM/Nikon Tie/20220211 test aSyn Dox/Post-crop (Fiji)/"
outpath = "/Volumes/Noelia PhD/Analysis/2022025/Nikon/Coincidence/"
    
Wells= ["A1","B2","C3","D4","A5","B6","C7","D8"]
Positions= ["_1","_2","_3","_4","_5","_6","_7","_8","_9"]

Coincidence = np.zeros((len(Wells),len(Positions)))


# Create an array and use it to get all the ininpath and name the files per channel
# instead of using for loop

for i,well in enumerate(Wells):
    for j,position in  enumerate(Positions):
        
     
        DAPI = inpath + well + position + "_DAPI.tif"
        asyn = inpath + well + position + "_aSyn.tif"
        
        
        im_DAPI = io.imread(DAPI)
        im_asyn = io.imread(asyn)
        
        plt.imshow(im_DAPI)
        plt.suptitle(well + position)
        plt.axis('off')
        plt.show()
        
        plt.imshow(im_asyn)
        plt.suptitle(well + position)
        plt.axis('off')
        plt.show()
        
        # Appply threshold (I will do both: auto-otsu threshold and manual one --> the
        # manual one is done by looking at images and checking what works best)
        
        
        # otsu_thr_DAPI = threshold_otsu(im_DAPI)
        # otsu_thr_im_DAPI = im_DAPI > otsu_thr_DAPI
        # plt.imshow(otsu_thr_im_DAPI)
        # plt.suptitle(well + position)
        # plt.axis('off')
        # plt.show()
        
        # otsu_thr_asyn = threshold_otsu(im_asyn)
        # otsu_thr_im_asyn = im_asyn > otsu_thr_asyn
        # plt.imshow(otsu_thr_im_asyn)
        # plt.suptitle(well + position)
        # plt.axis('off')
        # plt.show()

        DAPI_thr = 10000
        manual_im_DAPI = im_DAPI>DAPI_thr
        plt.imshow(manual_im_DAPI)
        plt.suptitle(well + position)
        plt.axis('off')
        plt.show()
        
        asyn_thr = 13000
        manual_im_asyn = im_asyn>asyn_thr
        plt.imshow(manual_im_asyn)
        plt.suptitle(well + position)
        plt.axis('off')
        plt.show()
        
        # Generate binary images (only doing manual threshold)
        
        bn_im_DAPI = im_DAPI * manual_im_DAPI
        
        bn_im_asyn = im_asyn * manual_im_asyn
        

        # Coincidence between DAPI and asyn binary images
        
        coincidence = bn_im_DAPI * bn_im_asyn
        plt.imshow(coincidence)
        plt.suptitle("Coincidence " + well + position)
        plt.axis('off')
        plt.show()
        
        # I wanna find the way to make my results into a table containing columns 
        # as wells and rows as position within that well. Then this can be used in 
        # Prism for further stats tests - i.e. quantification of aSyn in nucleus
        # or in the cytosol, or total amount of aSyn (to prove the dox system is 
        # working)
        
        coincidence_total = sum(sum(coincidence))
        Coincidence[i][j] = coincidence_total
        
        print(well + position + "done")
        

df = pd.DataFrame(Coincidence)
df.columns=Positions
df.insert(0,"Well", Wells)
df.to_csv(outpath + str(DAPI_thr) + str(asyn_thr) + 'total_coincidence.csv')
        
        
        
        





# By comparing the binary images between themselves and by opening the DAPI image on Fiji
# I see that the otsu threshold seems to be a better option for now. I will use this
# option for all the channels and then see if it is doing a good job!

























