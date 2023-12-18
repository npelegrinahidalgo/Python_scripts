#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 08:57:31 2022

@author: pele
"""
# Script for total aSyn present after threshold in images --> this way I can tell it's not there
# is more aSyn in nucleus but rather there is more aSyn in images as a whole

from PIL import Image
import matplotlib.pyplot as plt
from skimage import color, io
from skimage.filters import try_all_threshold, threshold_otsu
import numpy as np
from tabulate import tabulate
import pandas as pd


# inpaths to analyse


path_asyn = "/Volumes/Noelia PhD/Analysis/2022025 & 0221/Confocal/aSyn_sequences/"
outpath = "/Volumes/Noelia PhD/Analysis/2022025 & 0221/Confocal/Results/"

Wells= ["A1","B2"]#,"C3","D4","A5","B6","C7","D8"]
Positions= list(range(10,32))
aSyn_total = np.zeros((2,22))


# Create an array and use it to get all the path and name the files per channel
# instead of using for loop


# For dox plus treatment
for i,well in enumerate(Wells):
    for j,position in  enumerate(Positions):
   
        asyn = path_asyn + "20220225 " + well + "Dox Plus" + str(position) + ".tif"
        
        
        im_asyn = io.imread(asyn)
               
        
        plt.imshow(im_asyn)
        plt.suptitle(well + str(position))
        plt.axis('off')
        plt.show()
        

       
        
        asyn_thr = 10000 
        
        
        manual_im_asyn = im_asyn>asyn_thr
        plt.imshow(manual_im_asyn)        
        plt.suptitle(well + str(position))
        plt.axis('off')
        plt.show()

        # Generate binary images (only doing manual threshold)
                                         
                                          
        bn_im_asyn = im_asyn * manual_im_asyn
        asyn_total = sum(sum(bn_im_asyn))
        aSyn_total[i][j] = asyn_total

        print(well + str(position) + "done")      

df = pd.DataFrame(aSyn_total)
df.columns=Positions             
df.insert(0,"Well", Wells)           
df.to_csv(outpath + str(asyn_thr) + 'total_asyn_doxplus.csv')
        
        
        





# By comparing the binary images between themselves and by opening the DAPI image on Fiji
# I see that the otsu threshold seems to be a better option for now. I will use this
# option for all the channels and then see if it is doing a good job!

























