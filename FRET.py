#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 22:04:41 2022

@author: pele
"""


import skimage as im
import skimage.io as io
import os
import pandas as pd
# from picasso import render
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from sklearn.cluster import DBSCAN
from skimage import filters,measure
from skimage.filters import threshold_local


# Functions to be used below:
    
# To load each image using imread package

def load_image(toload):
    
    image=io.imread(toload)
    im.io.imshow(image)
    image_bright = im.exposure.adjust_gamma(image, gamma=0.5,gain=1)
    plt.suptitle(toload)
    # plt.colorbar()
    plt.axis('off')
    plt.show()
    print("done")
    
    return image

path="/Volumes/Noe PhD 2/Microscopes/Opera/20221213_ibds32-33/0h/ibidi32_0h__2022-12-13T13_31_11-Measurement 1/A4F9channels/"
pre_string="A4F9_"

donor=load_image(path+pre_string+'AF488.tif')
acceptor=load_image(path+pre_string+'FRET.tif')
# FRET=load_image(path+pre_string+'FRET.tif')

# donor_flat=np.mean(donor,axis=0)
# acceptor_flat=np.mean(acceptor,axis=0)
# FRET_flat=np.mean(FRET,axis=0)


donor_binary=donor>150
plt.imshow(donor_binary)
plt.suptitle("donor_binary")
# plt.colorbar()
plt.axis('off')
plt.show()



acceptor_binary=acceptor>150
plt.imshow(donor_binary)
plt.suptitle("acceptor_binary")
# plt.colorbar()
plt.axis('off')
plt.show()

both_binary=donor_binary*acceptor_binary



fret_im=acceptor/(acceptor+donor)
plt.imshow(fret_im)
plt.suptitle("FRET")
plt.colorbar()
plt.axis('off')
plt.show()


fret_im_thresh=both_binary*fret_im
plt.imshow(fret_im)
plt.suptitle("FRET_thr")
plt.colorbar()
plt.axis('off')
plt.show()


imsr2 = Image.fromarray(fret_im_thresh)
plt.show()

# imsr2.save(path+pre_string+'_FRET.tif')

labelled_image=measure.label(both_binary)
number_of_features=labelled_image.max()
print("%d features were detected in the image."%number_of_features)

# imsr2 = Image.fromarray(labelled_image)
# imsr2.save(path+pre_string+'_label.tif')
imsr2 = Image.fromarray((labelled_image * 255).astype(np.uint8))

# measurements=analyse_labelled_image(labelled,fret_im)





# # To label and count the features in the thresholded image:
    
# def label_image(input_image):
#     labelled_image=measure.label(input_image)
#     number_of_features=labelled_image.max()
 
#     return number_of_features,labelled_image
    

# # To take a labelled image and the original image and measure intensities, sizes etc.:
    
# def analyse_labelled_image(labelled_image,original_image):
#     measure_image=measure.regionprops_table(labelled_image,intensity_image=original_image,properties=('area','perimeter','centroid','orientation','major_axis_length','minor_axis_length','mean_intensity','max_intensity'))
#     measure_dataframe=pd.DataFrame.from_dict(measure_image)
#     return measure_dataframe



    
# path="/Volumes/Noe PhD 2/Microscopes/Opera/20221209_ibd31_fixed_test/ibd31_A1__2022-12-09T15_02_27-Measurement 1/A1F1channels/"
# pre_string="A1F1_"

# donor=load_image(path+pre_string+'AF488.tif')
# acceptor=load_image(path+pre_string+'AF647.tif')
# FRET=load_image(path+pre_string+'FRET.tif')


# donor_flat=np.mean(donor,axis=0)
# acceptor_flat=np.mean(acceptor,axis=0)
# FRET_flat=np.mean(FRET,axis=0)


# donor_binary=donor_flat>2000

# acceptor_binary=acceptor_flat>1000


# both_binary=donor_binary*acceptor_binary


# fret_im=acceptor_flat/(acceptor_flat+donor_flat)


# fret_im_thresh=both_binary*fret_im

# imsr2 = Image.fromarray(fret_im_thresh)
# imsr2.save(path+pre_string+'_FRET.tif')


# number,labelled=label_image(both_binary)
# print("%d features were detected in the image."%number)

# # imsr2 = Image.fromarray(labelled)
# # imsr2.save(path+pre_string+'_label.tif')

# measurements=analyse_labelled_image(labelled,fret_im)


       
# frets=measurements['mean_intensity']
# plt.hist(frets, bins = 20,range=[0,1], rwidth=0.9,color='#ff0000')
# plt.xlabel('FRET Efficiency',size=20)
# plt.ylabel('Number of Features',size=20)
# plt.savefig(path+pre_string+"_FRET_hist.pdf")
# plt.show()

# areas=measurements['area']
# plt.hist(areas, bins = 30,range=[0,30], rwidth=0.9,color='#ff0000')
# plt.xlabel('Area (pixels)',size=20)
# plt.ylabel('Number of Features',size=20)
# plt.savefig(path+pre_string+"_area_hist.pdf")
# plt.show()



# length=measurements['major_axis_length']
# plt.hist(length, bins = 5,range=[0,10], rwidth=0.9,color='#ff0000')
# plt.xlabel('Length',size=20)
# plt.ylabel('Number of Features',size=20)
# plt.title('Cluster lengths',size=20)
# plt.savefig(path+pre_string+"Lengths.pdf")
# plt.show()



# measurements.to_csv(path + '/' + pre_string+'_Metrics.csv', sep = '\t')









