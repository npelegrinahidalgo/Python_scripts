#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 10:21:18 2022

@author: pele
"""

import numpy as np
import pandas as pd
import os
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import scatterplot

pathlist = []


# Output image of clusters? 0 for no, 1 for yes:

cluster_image_output=0

tag = "CD9" #Replace with whatever target you are looking at so files contain this label




# Paths to analyse below:


pathlist.append(r"/Volumes/Noe_PhD_5/Microscopes/ONI/20240917_NPH_SMP-11/DEFAULT_USER/20240917_SMP-11-1/A2+2nM-D7673+1uM-DiR_2000-frames/pos_0/")
pathlist.append(r"/Volumes/Noe_PhD_5/Microscopes/ONI/20240917_NPH_SMP-11/DEFAULT_USER/20240917_SMP-11-1/A2+2nM-D7673+1uM-DiR_20000-frames/pos_0/")
pathlist.append(r"/Volumes/Noe_PhD_5/Microscopes/ONI/20240917_NPH_SMP-11/DEFAULT_USER/20240917_SMP-11-1/A4+2nM-D7673+1uM-DiR_20000-frames/pos_0/")
pathlist.append(r"/Volumes/Noe_PhD_5/Microscopes/ONI/20240917_NPH_SMP-11/DEFAULT_USER/20240917_SMP-11-1/A5+2nM-D7673+1uM-DiR_10000-frames/pos_0/")
pathlist.append(r"/Volumes/Noe_PhD_5/Microscopes/ONI/20240917_NPH_SMP-11/DEFAULT_USER/20240917_SMP-11-1/B5+2nM-D7673+1uM-DiR_10000-frames/pos_0/")
pathlist.append(r"/Volumes/Noe_PhD_5/Microscopes/ONI/20240917_NPH_SMP-11/DEFAULT_USER/20240917_SMP-11-1/B4+2nM-D7673+1uM-DiR_10000-frames/pos_0/")
pathlist.append(r"/Volumes/Noe_PhD_5/Microscopes/ONI/20240917_NPH_SMP-11/DEFAULT_USER/20240917_SMP-11-1/B3+2nM-D7673+1uM-DiR_10000-frames_100ms/pos_0/")
pathlist.append(r"/Volumes/Noe_PhD_5/Microscopes/ONI/20240917_NPH_SMP-11/DEFAULT_USER/20240917_SMP-11-1/A4+10nM-D7673+1uM-DiR_10000-frames/pos_0/")
pathlist.append(r"/Volumes/Noe_PhD_5/Microscopes/ONI/20240917_NPH_SMP-11/DEFAULT_USER/20240917_SMP-11-1/B2+10nM-D7673+1uM-DiR_10000-frames/pos_0/")
pathlist.append(r"/Volumes/Noe_PhD_5/Microscopes/ONI/20240917_NPH_SMP-11/DEFAULT_USER/20240917_SMP-11-1/C2+2nM-D7673+1uM-DiR_10000-frames/pos_0/")
pathlist.append(r"/Volumes/Noe_PhD_5/Microscopes/ONI/20240917_NPH_SMP-11/DEFAULT_USER/20240917_SMP-11-1/C3+2nM-D7673+1uM-DiR_10000-frames/pos_0/")
pathlist.append(r"/Volumes/Noe_PhD_5/Microscopes/ONI/20240917_NPH_SMP-11/DEFAULT_USER/20240917_SMP-11-1/B3+10nM-D7673+1uM-DiR_50000-frames/pos_0/")
pathlist.append(r"/Volumes/Noe_PhD_5/Microscopes/ONI/20240917_NPH_SMP-11/DEFAULT_USER/20240917_SMP-11-1/B3+10nM-D7673+1uM-DiR_50000-frames/pos_1/")
pathlist.append(r"/Volumes/Noe_PhD_5/Microscopes/ONI/20240917_NPH_SMP-11/DEFAULT_USER/20240917_SMP-11-1/B3+10nM-D7673+1uM-DiR_50000-frames/pos_2/")


for path in pathlist:
    print(path)

    # rows = range(1,4)
    # wells = range(1,4)

    # for row in rows:
        
    #     for well in wells:
    
    
    # FOV = "X0Y0R" + str(row) + "W" + str(well) + "_"
    
    # # Skip R2W1 file because it doesn't exits (issues during acquisition)
    
    # if "B2" in path:
        
    #     if row == 2 and well == 1:
    #         continue
    
    Filename = "CD9_FitResults.txt"#FOV + tag + "_mapped_FitResults.txt"  # This is the name of the SR file containing the localisations.


    path_within = path
    
    
    # Go through each file
    
    print(path_within)    
    os.chdir(path_within)
    input_data = pd.read_table(Filename)      # Load the data
     
    
    df=input_data.copy()
    fit = df.drop('Source', axis = 1)
    fit1 = fit.drop('SNR', axis = 1)
    
       
  
    Out_nc=open(path_within + tag + '_FitResults_headers.txt','w')   # Open file for writing to.
        # Write the header of the file
    Out_nc.write("""#Localisation Results File
#FileVersion Text.D0.E0.V2
#Name """ + tag +""" (LSE)
#Source <gdsc.smlm.ij.IJImageSource><name>""" + tag + """</name><width>428</width><height>684</height><frames>200</frames><singleFrame>0</singleFrame><extraFrames>0</extraFrames><path></path></gdsc.smlm.ij.IJImageSource>
#Bounds x0 y0 w428 h684
#Calibration <gdsc.smlm.results.Calibration><nmPerPixel>103.0</nmPerPixel><gain>55.5</gain><exposureTime>50.0</exposureTime><readNoise>0.0</readNoise><bias>0.0</bias><emCCD>false</emCCD><amplification>0.0</amplification></gdsc.smlm.results.Calibration>
#Configuration <gdsc.smlm.engine.FitEngineConfiguration><fitConfiguration><fitCriteria>LEAST_SQUARED_ERROR</fitCriteria><delta>1.0E-4</delta><initialAngle>0.0</initialAngle><initialSD0>2.0</initialSD0><initialSD1>2.0</initialSD1><computeDeviations>false</computeDeviations><fitSolver>LVM</fitSolver><minIterations>0</minIterations><maxIterations>20</maxIterations><significantDigits>5</significantDigits><fitFunction>CIRCULAR</fitFunction><flags>20</flags><backgroundFitting>true</backgroundFitting><notSignalFitting>false</notSignalFitting><coordinateShift>4.0</coordinateShift><shiftFactor>2.0</shiftFactor><fitRegion>0</fitRegion><coordinateOffset>0.5</coordinateOffset><signalThreshold>0.0</signalThreshold><signalStrength>30.0</signalStrength><minPhotons>0.0</minPhotons><precisionThreshold>400.0</precisionThreshold><precisionUsingBackground>true</precisionUsingBackground><nmPerPixel>117.0</nmPerPixel><gain>55.5</gain><emCCD>false</emCCD><modelCamera>false</modelCamera><noise>0.0</noise><minWidthFactor>0.5</minWidthFactor><widthFactor>1.01</widthFactor><fitValidation>true</fitValidation><lambda>10.0</lambda><computeResiduals>false</computeResiduals><duplicateDistance>0.5</duplicateDistance><bias>0.0</bias><readNoise>0.0</readNoise><amplification>0.0</amplification><maxFunctionEvaluations>2000</maxFunctionEvaluations><searchMethod>POWELL_BOUNDED</searchMethod><gradientLineMinimisation>false</gradientLineMinimisation><relativeThreshold>1.0E-6</relativeThreshold><absoluteThreshold>1.0E-16</absoluteThreshold></fitConfiguration><search>2.5</search><border>1.0</border><fitting>3.0</fitting><failuresLimit>10</failuresLimit><includeNeighbours>true</includeNeighbours><neighbourHeightThreshold>0.3</neighbourHeightThreshold><residualsThreshold>1.0</residualsThreshold><noiseMethod>QUICK_RESIDUALS_LEAST_MEAN_OF_SQUARES</noiseMethod><dataFilterType>SINGLE</dataFilterType><smooth><double>0.5</double></smooth><dataFilter><gdsc.smlm.engine.DataFilter>MEAN</gdsc.smlm.engine.DataFilter></dataFilter></gdsc.smlm.engine.FitEngineConfiguration>
#Frame	origX	origY	origValue	Error	Noise	Background	Signal	Angle	X	Y	X SD	Y SD	Precision

    """)


    print("Done")
    
    Out_nc.write(fit1.to_csv(sep = '\t',header=False,index=False))    # Write the columns that are required (without the non-clustered localisations)
    
    
    Out_nc.close() # Close the file.
    
    
    # "#Localisation Results File #FileVersion Text.D0.E0.V2"
