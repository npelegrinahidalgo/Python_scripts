#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 18:30:37 2021
@author: Mathew
"""

######## Change the label of the headers file (filename_conatains) and the save folder (save_total) ###########


# Comments highlighted (#~~~) to get code running  --> refer to comments for tweaking code

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from sklearn.cluster import DBSCAN
from skimage import filters,measure


# Camera settings (TIRFM)
Pixel_size=117
camera_gain=2.17
camera_sensitivity=11.5
camera_offset=500


# Options (set to 1 to perform)


to_cluster=1       

# Settings
image_width=684
image_height=428
gradient=7500
drift_correction=0
scale=8
# precision_threshold=250 --> It is not used throughout the script
eps_threshold=1
minimum_locs_threshold=5
prec_thresh=30


# ~~~Make sure this corresponds to the actual filename~~~

filename_contains=r"NR_FitResults.txt"

name_tag = "NR"


# Path to save overall results:
    
save_total = "/Volumes/Noe PhD 3/Microscopes/ONI/20230626_NPH_PLL+EVs#1/"

# Folders:

pathlist=[]


pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230626_NPH_PLL+EVs#1/#1+5nM_NR/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230626_NPH_PLL+EVs#1/#1+5nM_NR/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230626_NPH_PLL+EVs#1/#1+5nM_NR/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230626_NPH_PLL+EVs#1/#1+5nM_NR/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230626_NPH_PLL+EVs#1/#1+5nM_NR/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230626_NPH_PLL+EVs#1/#1+5nM_NR/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230626_NPH_PLL+EVs#1/#1+5nM_NR/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230626_NPH_PLL+EVs#1/#1+5nM_NR/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230626_NPH_PLL+EVs#1/#1+5nM_NR/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230626_NPH_PLL+EVs#1/#1_only/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230626_NPH_PLL+EVs#1/5nM_NR_only/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230626_NPH_PLL+EVs#1/5nM_NR_only/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230626_NPH_PLL+EVs#1/5nM_NR_only/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230626_NPH_PLL+EVs#1/5nM_NR_only/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230626_NPH_PLL+EVs#1/5nM_NR_only/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230626_NPH_PLL+EVs#1/5nM_NR_only/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230626_NPH_PLL+EVs#1/5nM_NR_only/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230626_NPH_PLL+EVs#1/5nM_NR_only/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230626_NPH_PLL+EVs#1/5nM_NR_only/pos_8/")




# Various functions

#  Generate SR image (points)
def generate_SR(coords):
    SR_plot_def=np.zeros((image_width*scale,image_height*scale),dtype=float)
    j=0
    for i in coords:
        
        xcoord=coords[j,0]
        ycoord=coords[j,1]
        scale_xcoord=round(xcoord*scale)
        scale_ycoord=round(ycoord*scale)
        # if(scale_xcoord<image_width and scale_ycoord<image_height):
        SR_plot_def[scale_ycoord,scale_xcoord]+=1
        
        j+=1
    return SR_plot_def

def SRGaussian(size, fwhm, center):

    sizex=size[0]
    sizey=size[1]
    x = np.arange(0, sizex, 1, float)
    y = x[0:sizey,np.newaxis]
    # y = x[:,np.newaxis]


    x0 = center[0]
    y0 = center[1]
    
    wx=fwhm[0]
    wy=fwhm[1]
    
    return np.exp(-0.5 * (np.square(x-x0)/np.square(wx) + np.square(y-y0)/np.square(wy)) )

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

def generate_SR_prec(coords,precsx,precsy):
    box_size=20
    SR_prec_plot_def=np.zeros((image_width*scale,image_height*scale),dtype=float)
    dims=np.shape(SR_prec_plot_def)
    print(dims)
    j=0
    for i in coords:

      
        precisionx=precsx[j]/Pixel_size*scale
        precisiony=precsy[j]/Pixel_size*scale
        xcoord=coords[j,0]
        ycoord=coords[j,1]
        scale_xcoord=round(xcoord*scale)
        scale_ycoord=round(ycoord*scale)
        
        
        
        sigmax=precisionx
        sigmay=precisiony
        
        
        # tempgauss=SRGaussian((2*box_size,2*box_size), (sigmax,sigmay),(box_size,box_size))
        
        tempgauss=gkern(2*box_size,sigmax,sigmay)
        
        # SRGaussian((2*box_size,2*box_size), (sigmax,sigmay),(box_size,box_size))
        
        
        
        ybox_min=scale_ycoord-box_size
        ybox_max=scale_ycoord+box_size
        xbox_min=scale_xcoord-box_size
        xbox_max=scale_xcoord+box_size 
        
        
        if(np.shape(SR_prec_plot_def[ybox_min:ybox_max,xbox_min:xbox_max])==np.shape(tempgauss)):
            SR_prec_plot_def[ybox_min:ybox_max,xbox_min:xbox_max]=SR_prec_plot_def[ybox_min:ybox_max,xbox_min:xbox_max]+tempgauss
        
        
           
        j+=1
    
    return SR_prec_plot_def

# Perform DBSCAN on the coordinates. 

def cluster(coords):
     db = DBSCAN(eps=eps_threshold, min_samples=minimum_locs_threshold).fit(coords)
     labels = db.labels_
     n_clusters_ = len(set(labels)) - (1 if-1 in labels else 0)  # This is to calculate the number of clusters.
     print('Estimated number of clusters: %d' % n_clusters_)
     return labels

def generate_SR_cluster(coords,clusters):
    SR_plot_def=np.zeros((image_width*scale,image_height*scale),dtype=float)
    j=0
    for i in coords:
        if clusters[j]>-1:
            xcoord=coords[j,0]
            ycoord=coords[j,1]
            scale_xcoord=round(xcoord*scale)
            scale_ycoord=round(ycoord*scale)
            # if(scale_xcoord<image_width and scale_ycoord<image_height):
            SR_plot_def[scale_ycoord,scale_xcoord]+=1
        
        j+=1
    return SR_plot_def

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
   
def analyse_labelled_image(labelled_image):
    
    measure_image=measure.regionprops_table(labelled_image,intensity_image=labelled_image,properties=('area','perimeter','centroid','orientation','major_axis_length','minor_axis_length','mean_intensity','max_intensity'))
    measure_dataframe=pd.DataFrame.from_dict(measure_image)
    return measure_dataframe

if to_cluster==1:
    # To store overall medians/means etc. 
    Output_all_cases = pd.DataFrame(columns=['Path','Number_of_clusters','Points_per_cluster_mean','Points_per_cluster_SD','Points_per_cluster_med',
                                       'Area_mean','Area_sd','Area_med','Length_mean','Length_sd','Length_med','Ratio_mean','Ratio_sd','Ratio_med'])


for path in pathlist:
    print(path)
    # Below is the path where I want all the DBSCAN files/images to be saved at:
    
    save_path = os.path.join(path, str(eps_threshold) + "_"+ str(minimum_locs_threshold) + str(name_tag) + "_DBSCAN/")
    if not os.path.exists(save_path):
        os.makedirs(save_path)
  
    
    # Perform the fitting

    # Load the fits:
    for root, dirs, files in os.walk(path):
        for name in files:
            if filename_contains in name:
                if ".txt" in name:
                    if not "._" in name:
                                # ~~~ 'if not' added because there are hidden files in my directory that are being imported instead of the actual file containing the localisations (i.e. Fit_Results file)
                                
                                
                        resultsname = name
                        print(resultsname)
    
    fits_path= path + resultsname
    
    print(fits_path)
    
    # ~~~ Make sure data importe the right way, check separator/delimiter~~~
    
    loc_data = pd.read_table(fits_path, sep = '\t')
    
    if len(loc_data["Source"]) > 1:
            
        index_names = loc_data[loc_data['Precision (nm)']>prec_thresh].index
        loc_data.drop(index_names, inplace = True)
       
        path=path+"GDSCSMLM_"
    
        # Extract useful data:
        coords = np.array(list(zip(loc_data['X'],loc_data['Y'])))
        
        
        # ~~~ Removed '(nm)' from 'Precision' column header (it is not there)~~~
        
        precsx= np.array(loc_data['Precision (nm)'])
        precsy= np.array(loc_data['Precision (nm)'])
        xcoords=np.array(loc_data['X'])
        ycoords=np.array(loc_data['Y'])
        
        
        precs_nm=precsx
        
        plt.hist(precs_nm, bins = 50,range=[0,100], rwidth=0.9,color='#ff0000')
        plt.xlabel('Precision (nm)',size=20)
        plt.ylabel('Number of Features',size=20)
        plt.title('Localisation precision',size=20)
        # plt.savefig(save_path +str(eps_threshold) + "_" + str(minimum_locs_threshold)+ name_tag +"Precision.pdf")
        plt.show()
            
        # Generate points SR (ESMB method):
        # SR=generate_SR(coords)
        
        # imsr = Image.fromarray(SR)
        # imsr.save(save_path + 'SR_points_python.tif')
        
        # SR_prec=generate_SR_prec(coords,precsx,precsy)
        
        # imsr = Image.fromarray(SR_prec)
        # imsr.save(save_path +str(eps_threshold) + "_" + str(minimum_locs_threshold)+'SR_width_python.tif')
        
        # Cluster analysis
        if to_cluster==1:
            clusters=cluster(coords)
        
            # Check how many localisations per cluster
         
            cluster_list=clusters.tolist()    # Need to convert the dataframe into a list- so that we can use the count() function. 
            maximum=max(cluster_list)+1  
            
            
            cluster_contents=[]         # Make a list to store the number of clusters in
            
            for i in range(0,maximum):
                n=cluster_list.count(i)     # Count the number of times that the cluster number i is observed
               
                cluster_contents.append(n)  # Add to the list. 
            
            if len(cluster_contents)>0:
                average_locs=sum(cluster_contents)/len(cluster_contents)
         
                plt.hist(cluster_contents, bins = 20,range=[0,200], rwidth=0.9,color='#607c8e') # Plot a histogram. 
                plt.xlabel('Localisations per cluster')
                plt.ylabel('Number of clusters')
                # plt.savefig(save_path +str(eps_threshold) + "_" + str(minimum_locs_threshold)+ name_tag + 'Localisations.pdf')
                plt.show()
                
                cluster_arr=np.array(cluster_contents)
            
                median_locs=np.median(cluster_arr)
                mean_locs=cluster_arr.mean()
                std_locs=cluster_arr.std()
                
            
                # Generate the SR image.
                SR_Clu=generate_SR_cluster(coords,clusters)
                plt.imshow(SR_Clu,vmin=0, vmax=0.1)
                
                plt.show()
                
                imsr = Image.fromarray(SR_Clu)
                # imsr.save(save_path +str(eps_threshold) + "_" + str(minimum_locs_threshold)+ name_tag +'SR_points_python_clustered.tif')
                
                
                SR_clu_prec,labelled,SR_prec_plot=generate_SR_prec_cluster(coords,precsx,precsy,clusters)
                
                
                
                imsr = Image.fromarray(SR_prec_plot)
                # imsr.save(save_path +str(eps_threshold) + "_" + str(minimum_locs_threshold)+ name_tag +'Test_prec.tif')
                
            
         
            
                
                # imsr = Image.fromarray(SR_clu_prec)
                # imsr.save(save_path +str(eps_threshold) + "_" + str(minimum_locs_threshold)+ name_tag +'SR_width_python_clustered.tif')
                
                # imsr = Image.fromarray(labelled)
                # imsr.save(save_path +str(eps_threshold) + "_" + str(minimum_locs_threshold) + name_tag +'SR_fwhm_python_clustered.tif')
                
                labeltot=labelled.max()+1
            
                print('Total number of clusters in labelled image: %d'%labeltot)
                
                
                labelled_to_analyse=labelled.astype('int')
                measurements=analyse_labelled_image(labelled_to_analyse)
            
            
                # Make and save histograms
                
                areas=measurements['area']*((Pixel_size/(scale*1000))**2)
                plt.hist(areas, bins = 20,range=[0,0.1], rwidth=0.9,color='#ff0000')
                plt.xlabel('Area (\u03bcm$^2$)',size=20)
                plt.ylabel('Number of Features',size=20)
                plt.title('Cluster area',size=20)
                # plt.savefig(save_path +str(eps_threshold) + "_" + str(minimum_locs_threshold) + name_tag +"Area.pdf")
                plt.show()
                
                median_area=areas.median()
                mean_area=areas.mean()
                std_area=areas.std()
                
                
                length=measurements['major_axis_length']*((Pixel_size/8))
                plt.hist(length, bins = 20,range=[0,1000], rwidth=0.9,color='#ff0000')
                plt.xlabel('Length (nm)',size=20)
                plt.ylabel('Number of Features',size=20)
                plt.title('Cluster lengths',size=20)
                # plt.savefig(save_path +str(eps_threshold) + "_" + str(minimum_locs_threshold) + name_tag +"Lengths.pdf")
                plt.show()
            
                median_length=length.median()
                mean_length=length.mean()
                std_length=length.std()
                
                ratio=measurements['minor_axis_length']/measurements['major_axis_length']
                plt.hist(ratio, bins = 50,range=[0,1], rwidth=0.9,color='#ff0000')
                plt.xlabel('Eccentricity',size=20)
                plt.ylabel('Number of Features',size=20)
                plt.title('Cluster Eccentricity',size=20)
                # plt.savefig(save_path +str(eps_threshold) + "_" + str(minimum_locs_threshold) + name_tag +"Ecc.pdf")
                plt.show()
                
                median_ratio=ratio.median()
                mean_ratio=ratio.mean()
                std_ratio=ratio.std()
                
                measurements['Eccentricity']=ratio
                if len(measurements)==len(cluster_contents):
                    measurements['Number_of_locs']=cluster_contents
                    # measurements.to_csv(save_path + name_tag + 'Metrics.csv', sep = '\t')
                
                Output_overall = pd.DataFrame(columns=['xw','yw','cluster'])
                
                Output_overall['xw']=xcoords
                
                Output_overall['yw']=ycoords
                
                Output_overall['cluster']=clusters
                
                # Output_overall.to_csv(save_path + str(eps_threshold) + "_" + str(minimum_locs_threshold)+ name_tag +'all.csv', sep = '\t')    
            
                Output_all_cases = Output_all_cases.append({'Path':path,'Number_of_clusters':maximum,'Points_per_cluster_mean':mean_locs,'Points_per_cluster_SD':std_locs,'Points_per_cluster_med':median_locs,
                                                    'Area_mean':mean_area,'Area_sd':std_area,'Area_med':median_area,'Length_mean':mean_length,'Length_sd':std_length,'Length_med':median_length,
                                                    'Ratio_mean':mean_ratio,'Ratio_sd':std_ratio,'Ratio_med':median_ratio},ignore_index=True)
            else:
                Output_all_cases = Output_all_cases.append({'Path':path,'Number_of_clusters':'0','Points_per_cluster_mean':'0','Points_per_cluster_SD':'0','Points_per_cluster_med':'0',
                                                    'Area_mean':'0','Area_sd':'0','Area_med':'0','Length_mean':'0','Length_sd':'0','Length_med':'0',
                                                    'Ratio_mean':'0','Ratio_sd':'0','Ratio_med':'0'},ignore_index=True)
           
           
                
    else:
        Output_all_cases = Output_all_cases.append({'Path':path,'Number_of_clusters':'no locs','Points_per_cluster_mean':'0','Points_per_cluster_SD':'0','Points_per_cluster_med':'0',
                                            'Area_mean':'0','Area_sd':'0','Area_med':'0','Length_mean':'0','Length_sd':'0','Length_med':'0',
                                            'Ratio_mean':'0','Ratio_sd':'0','Ratio_med':'0'},ignore_index=True)
        
        
if to_cluster==1:
    
    Output_all_cases.to_csv(save_total + str(eps_threshold) + '_' + str(minimum_locs_threshold) + name_tag + 'clusters_data_GDSC_all_metrics.csv', sep = '\t')
                
            
            