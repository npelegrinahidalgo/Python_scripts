#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 10:21:18 2022

@author: pele

This is a script to add headers to FitResults.txt from GDSC SMLM Peak Fit function

"""

import numpy as np
import pandas as pd
import os
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import scatterplot

pathlist = []

precision_GDSC = 20
signal_GDSC = 30


tag = "561" #+ "_" + str(precision_GDSC) + "_" + str(signal_GDSC) #This is the specific name to each file (i.e. marker name or whatever channel you are looking at)

Filename='_FitResults.txt'   #This remains constant in all files as long as you use the right macro on Fiji (make sure all files are saved with this ending)


# Paths to analyse below:

  
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A4_only/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A4_only/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A4_only/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A4_only/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A5_only/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A5_only/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A5_only/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A5_only/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/Beads/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/Beads/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/Beads/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/Beads/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/Beads/pos_4/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/Beads/pos_5/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/Beads/pos_6/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/Beads/pos_7/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/Beads/pos_8/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A2_1nM_D7675/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A2_1nM_D7675/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A2_1nM_D7675/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A2_1nM_D7675/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A2_only/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A2_only/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A2_only/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A2_only/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A3_1nM_D7675/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A3_1nM_D7675/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A3_1nM_D7675/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A3_1nM_D7675/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A3_only/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A3_only/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A3_only/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A3_only/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A5_1nM_D7675/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A5_1nM_D7675/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A5_1nM_D7675/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A5_1nM_D7675/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A4_1nM_D7675/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A4_1nM_D7675/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A4_1nM_D7675/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/A4_1nM_D7675/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B3_1nM_D7675/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B3_1nM_D7675/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B3_1nM_D7675/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B3_1nM_D7675/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B3_only/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B3_only/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B3_only/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B3_only/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B2_1nM_D7675/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B2_1nM_D7675/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B2_1nM_D7675/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B2_1nM_D7675/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B2_only/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B2_only/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B2_only/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B2_only/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B4_only/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B4_only/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B4_only/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B4_only/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B5_D7675/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B5_D7675/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B5_D7675/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B5_D7675/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B5_only/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B5_only/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B5_only/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B5_only/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B4_1nM_D7675/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B4_1nM_D7675/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B4_1nM_D7675/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/B4_1nM_D7675/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C3_only/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C3_only/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C3_only/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C3_only/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C4_1nM_D7675/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C4_1nM_D7675/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C4_1nM_D7675/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C4_1nM_D7675/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C4_only/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C4_only/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C4_only/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C4_only/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C5_only/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C5_only/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C5_only/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C5_only/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C2_1nM_D7675/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C2_1nM_D7675/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C2_1nM_D7675/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C2_1nM_D7675/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C2_only/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C2_only/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C2_only/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C2_only/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C3_1nM_D7675/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C3_1nM_D7675/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C3_1nM_D7675/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C3_1nM_D7675/pos_3/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C5_1nM_D7675-1/pos_0/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C5_1nM_D7675-1/pos_1/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C5_1nM_D7675-1/pos_2/")
# pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20230607_NPH_Control_simpull_EVs/C5_1nM_D7675-1/pos_3/")



for path in pathlist:           # Go through each file
    print(path)    
    os.chdir(path)
    input_data = pd.read_table(tag + Filename)       # Load the data
     
    
    df=input_data.copy()
    fit = df.drop('Source',1)
    fit1 = fit.drop('SNR', 1)
    
       
  
    Out_nc=open(path+'/'+ tag + '_FitResults_withheader.txt','w')   # Open file for writing to.
        # Write the header of the file
    Out_nc.write("""#Localisation Results File
#FileVersion Text.D0.E0.V2
#Name """ + tag + """_super_res.tif (LSE)
#Source <gdsc.smlm.ij.IJImageSource><name>""" + tag + """.tif</name><width>428</width><height>684</height><frames>5000</frames><singleFrame>0</singleFrame><extraFrames>0</extraFrames><path>/Volumes/TOSHIBA EXT/SuperResData/""" + tag + """.tif</path></gdsc.smlm.ij.IJImageSource>
#Bounds x0 y0 w428 h684
#Calibration <gdsc.smlm.results.Calibration><nmPerPixel>117.0</nmPerPixel><gain>2.17</gain><exposureTime>50.0</exposureTime><readNoise>0.0</readNoise><bias>0.0</bias><emCCD>false</emCCD><amplification>0.0</amplification></gdsc.smlm.results.Calibration>
#Configuration <gdsc.smlm.engine.FitEngineConfiguration><fitConfiguration><fitCriteria>LEAST_SQUARED_ERROR</fitCriteria><delta>1.0E-4</delta><initialAngle>0.0</initialAngle><initialSD0>2.0</initialSD0><initialSD1>2.0</initialSD1><computeDeviations>false</computeDeviations><fitSolver>LVM</fitSolver><minIterations>0</minIterations><maxIterations>20</maxIterations><significantDigits>5</significantDigits><fitFunction>CIRCULAR</fitFunction><flags>20</flags><backgroundFitting>true</backgroundFitting><notSignalFitting>false</notSignalFitting><coordinateShift>4.0</coordinateShift><shiftFactor>2.0</shiftFactor><fitRegion>0</fitRegion><coordinateOffset>0.5</coordinateOffset><signalThreshold>0.0</signalThreshold><signalStrength>30.0</signalStrength><minPhotons>0.0</minPhotons><precisionThreshold>10000.0</precisionThreshold><precisionUsingBackground>false</precisionUsingBackground><nmPerPixel>103.0</nmPerPixel><gain>2.17</gain><emCCD>false</emCCD><modelCamera>false</modelCamera><noise>0.0</noise><minWidthFactor>0.5</minWidthFactor><widthFactor>1.01</widthFactor><fitValidation>true</fitValidation><lambda>10.0</lambda><computeResiduals>false</computeResiduals><duplicateDistance>0.5</duplicateDistance><bias>0.0</bias><readNoise>0.0</readNoise><amplification>0.0</amplification><maxFunctionEvaluations>2000</maxFunctionEvaluations><searchMethod>POWELL_BOUNDED</searchMethod><gradientLineMinimisation>false</gradientLineMinimisation><relativeThreshold>1.0E-6</relativeThreshold><absoluteThreshold>1.0E-16</absoluteThreshold></fitConfiguration><search>2.5</search><border>1.0</border><fitting>3.0</fitting><failuresLimit>10</failuresLimit><includeNeighbours>true</includeNeighbours><neighbourHeightThreshold>0.3</neighbourHeightThreshold><residualsThreshold>1.0</residualsThreshold><noiseMethod>QUICK_RESIDUALS_LEAST_MEAN_OF_SQUARES</noiseMethod><dataFilterType>SINGLE</dataFilterType><smooth><double>0.5</double></smooth><dataFilter><gdsc.smlm.engine.DataFilter>MEAN</gdsc.smlm.engine.DataFilter></dataFilter></gdsc.smlm.engine.FitEngineConfiguration>
#frames	origX	origY	origValue	Error	Noise	Background	Signal	Angle	X	Y	X SD	Y SD	Precision
""")

    print("Done")
    Out_nc.write(fit1.to_csv(sep = '\t',header=False,index=False))    # Write the columns that are required (without the non-clustered localisations)
    
    
    Out_nc.close() # Close the file.
