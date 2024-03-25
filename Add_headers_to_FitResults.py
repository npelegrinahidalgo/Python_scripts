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

tag = "638" #Replace with whatever target you are looking at so files contain this label




# Paths to analyse below:


pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/B2+D6G4AB(2nM)+nB(6nM)+E2285(1nM)+NR(5nM)_2024-02-16_15-22-12/Processed images/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/B2+D6G4AB(5nM)+nB(15nM)+D7674(1nM)+NR(5nM)_2024-02-16_19-00-33/Processed images/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/B3+UE3R2AB(2nM)+nB(6nM)+D7674(1nM)+NR(5nM)_2024-02-16_18-02-44/Processed images/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/C2+D6G4AB(2nM)+nB(6nM)+E2285(1nM)+NR(5nM)_2024-02-16_15-47-51/Processed images/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/A3+UE3R2AB(2nM)+nB(6nM)+D7674(1nM)+NR(5nM)_2024-02-16_20-40-14/Processed images/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/C2+D6G4AB(5nM)+nB(15nM)+D7674(1nM)+NR(5nM)_2024-02-16_19-44-36/Processed images/")
pathlist.append(r"/Volumes/Noe PhD 4/Microscopes/TIRF/20240216_EV/C3+UE3R2AB(2nM)+nB(6nM)+D7674(1nM)+NR(5nM)_2024-02-16_18-18-46/Processed images/")


for path in pathlist:
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
    
            
            FOV = "X0Y0R" + str(row) + "W" + str(well) + "_"
        
            Filename = FOV + tag + "_0_FitResults.txt"  # This is the name of the SR file containing the localisations.
        

            path_within = path
            
            
            # Go through each file
            
            print(path_within)    
            os.chdir(path_within)
            input_data = pd.read_table(Filename)      # Load the data
             
            
            df=input_data.copy()
            fit = df.drop('Source',1)
            fit1 = fit.drop('SNR', 1)
            
               
          
            Out_nc=open(path_within+ FOV + tag + '_FitResults_headers.txt','w')   # Open file for writing to.
                # Write the header of the file
            Out_nc.write("""#Localisation Results File #FileVersion Text.D0.E0.V2 #Name 638_super_res.tif (LSE)#Source <gdsc.smlm.ij.IJImageSource><name>638_super_res.tif</name><width>512</width><height>512</height><frames>4000</frames><singleFrame>0</singleFrame><extraFrames>0</extraFrames><path>/Volumes/TOSHIBA EXT/SuperResData/638.tif</path></gdsc.smlm.ij.IJImageSource>#Bounds x0 y0 w512 h512#Calibration <gdsc.smlm.results.Calibration><nmPerPixel>103.0</nmPerPixel><gain>2.17</gain><exposureTime>50.0</exposureTime><readNoise>0.0</readNoise><bias>0.0</bias><emCCD>false</emCCD><amplification>0.0</amplification></gdsc.smlm.results.Calibration>#Configuration <gdsc.smlm.engine.FitEngineConfiguration><fitConfiguration><fitCriteria>LEAST_SQUARED_ERROR</fitCriteria><delta>1.0E-4</delta><initialAngle>0.0</initialAngle><initialSD0>2.0</initialSD0><initialSD1>2.0</initialSD1><computeDeviations>false</computeDeviations><fitSolver>LVM</fitSolver><minIterations>0</minIterations><maxIterations>20</maxIterations><significantDigits>5</significantDigits><fitFunction>CIRCULAR</fitFunction><flags>20</flags><backgroundFitting>true</backgroundFitting><notSignalFitting>false</notSignalFitting><coordinateShift>4.0</coordinateShift><shiftFactor>2.0</shiftFactor><fitRegion>0</fitRegion><coordinateOffset>0.5</coordinateOffset><signalThreshold>0.0</signalThreshold><signalStrength>30.0</signalStrength><minPhotons>0.0</minPhotons><precisionThreshold>10000.0</precisionThreshold><precisionUsingBackground>false</precisionUsingBackground><nmPerPixel>103.0</nmPerPixel><gain>2.17</gain><emCCD>false</emCCD><modelCamera>false</modelCamera><noise>0.0</noise><minWidthFactor>0.5</minWidthFactor><widthFactor>1.01</widthFactor><fitValidation>true</fitValidation><lambda>10.0</lambda><computeResiduals>false</computeResiduals><duplicateDistance>0.5</duplicateDistance><bias>0.0</bias><readNoise>0.0</readNoise><amplification>0.0</amplification><maxFunctionEvaluations>2000</maxFunctionEvaluations><searchMethod>POWELL_BOUNDED</searchMethod><gradientLineMinimisation>false</gradientLineMinimisation><relativeThreshold>1.0E-6</relativeThreshold><absoluteThreshold>1.0E-16</absoluteThreshold></fitConfiguration><search>2.5</search><border>1.0</border><fitting>3.0</fitting><failuresLimit>10</failuresLimit><includeNeighbours>true</includeNeighbours><neighbourHeightThreshold>0.3</neighbourHeightThreshold><residualsThreshold>1.0</residualsThreshold><noiseMethod>QUICK_RESIDUALS_LEAST_MEAN_OF_SQUARES</noiseMethod><dataFilterType>SINGLE</dataFilterType><smooth><double>0.5</double></smooth><dataFilter><gdsc.smlm.engine.DataFilter>MEAN</gdsc.smlm.engine.DataFilter></dataFilter></gdsc.smlm.engine.FitEngineConfiguration>
            #frames	origX	origY	origValue	Error	Noise	Background	Signal	Angle	X	Y	X SD	Y SD	Precision""")
        
            print("Done")
            
            Out_nc.write(fit1.to_csv(sep = '\t',header=False,index=False))    # Write the columns that are required (without the non-clustered localisations)
            
            
            Out_nc.close() # Close the file.
            
            
        
