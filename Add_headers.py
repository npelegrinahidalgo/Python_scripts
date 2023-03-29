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


Filename='test_01_Fit Results.txt'   # This is the name of the SR file containing the localisations.

# Paths to analyse below:

pathlist.append(r"/Volumes/Noe PhD 2/Microscopes/ONI/20230323_NPH_PSMa3_StressMarq/PLL_ThT+2/pos_0/")
    

# pathlist.append("/Volumes/Noelia PhD/Microscopes/ONI/20220603_ibd14_dSTORM_Tom20/A1_1in5000AF647_buffer/pos_0/30_20GDSC_reconstruction/")
# pathlist.append("/Volumes/Noelia PhD/Microscopes/ONI/20220603_ibd14_dSTORM_Tom20/A1_1in5000AF647_buffer-1/pos_0/30_20GDSC_reconstruction/")
# pathlist.append("/Volumes/Noelia PhD/Microscopes/ONI/20220603_ibd14_dSTORM_Tom20/A1_1in5000AF647_buffer-2/pos_0/30_20GDSC_reconstruction/")
# pathlist.append("/Volumes/Noelia PhD/Microscopes/ONI/20220603_ibd14_dSTORM_Tom20/A1_1in5000AF647_buffer-3/pos_0/30_20GDSC_reconstruction/")
# pathlist.append("/Volumes/Noelia PhD/Microscopes/ONI/20220603_ibd14_dSTORM_Tom20/A1_1in5000AF647_buffer-4/pos_0/30_20GDSC_reconstruction/")
# pathlist.append("/Volumes/Noelia PhD/Microscopes/ONI/20220603_ibd14_dSTORM_Tom20/A1_1in5000AF647_buffer-4-1/pos_0/30_20GDSC_reconstruction/")
# pathlist.append("/Volumes/Noelia PhD/Microscopes/ONI/20220603_ibd14_dSTORM_Tom20/A1_1in5000AF647_no_buffer/pos_0/30_20GDSC_reconstruction/")
# pathlist.append("/Volumes/Noelia PhD/Microscopes/ONI/20220603_ibd14_dSTORM_Tom20/A2_1in7000AF647_buffer_several_positions/pos_0/30_20GDSC_reconstruction/")
# pathlist.append("/Volumes/Noelia PhD/Microscopes/ONI/20220603_ibd14_dSTORM_Tom20/A2_1in7000AF647_buffer_several_positions/pos_1/30_20GDSC_reconstruction/")
# pathlist.append("/Volumes/Noelia PhD/Microscopes/ONI/20220603_ibd14_dSTORM_Tom20/A2_1in7000AF647_buffer_several_positions/pos_2/30_20GDSC_reconstruction/")
# pathlist.append("/Volumes/Noelia PhD/Microscopes/ONI/20220603_ibd14_dSTORM_Tom20/A2_1in7000AF647_buffer_several_positions/pos_3/30_20GDSC_reconstruction/")
# pathlist.append("/Volumes/Noelia PhD/Microscopes/ONI/20220603_ibd14_dSTORM_Tom20/A2_1in7000AF647_buffer_several_positions/pos_4/30_20GDSC_reconstruction/")
# pathlist.append("/Volumes/Noelia PhD/Microscopes/ONI/20220603_ibd14_dSTORM_Tom20/A3_1in10000AF647_buffer/pos_0/30_20GDSC_reconstruction/")
# pathlist.append("/Volumes/Noelia PhD/Microscopes/ONI/20220603_ibd14_dSTORM_Tom20/A3_1in10000AF647_buffer/pos_1/30_20GDSC_reconstruction/")
# pathlist.append("/Volumes/Noelia PhD/Microscopes/ONI/20220603_ibd14_dSTORM_Tom20/A3_1in10000AF647_buffer/pos_2/30_20GDSC_reconstruction/")
# pathlist.append("/Volumes/Noelia PhD/Microscopes/ONI/20220603_ibd14_dSTORM_Tom20/A3_1in10000AF647_buffer/pos_3/30_20GDSC_reconstruction/")
# pathlist.append("/Volumes/Noelia PhD/Microscopes/ONI/20220603_ibd14_dSTORM_Tom20/A3_1in10000AF647_buffer/pos_4/30_20GDSC_reconstruction/")
# pathlist.append("/Volumes/Noelia PhD/Microscopes/ONI/20220603_ibd14_dSTORM_Tom20/A3_1in10000AF647_no_buffer/pos_0/30_20GDSC_reconstruction/")
# pathlist.append("/Volumes/Noelia PhD/Microscopes/ONI/20220603_ibd14_dSTORM_Tom20/A4__noTom20_1in10000AF647_buffer-1/pos_0/30_20GDSC_reconstruction/")
# pathlist.append("/Volumes/Noelia PhD/Microscopes/ONI/20220603_ibd14_dSTORM_Tom20/A4__noTom20_1in10000AF647_no_buffer-3/pos_0/30_20GDSC_reconstruction/")




for path in pathlist:           # Go through each file
    print(path)    
    os.chdir(path)
    input_data = pd.read_table(Filename)       # Load the data
     
    
    df=input_data.copy()
    fit = df.drop('Source',1)
    fit1 = fit.drop('SNR', 1)
    
       
  
    Out_nc=open(path+'/'+'test_FitResults_withheader.txt','w')   # Open file for writing to.
        # Write the header of the file
    Out_nc.write("""#Localisation Results File
#FileVersion Text.D0.E0.V2
#Name DNA-PAINT_super_res.tif (LSE)
#Source <gdsc.smlm.ij.IJImageSource><name>DNA-PAINT_super_res.tif</name><width>428</width><height>684</height><frames>5000</frames><singleFrame>0</singleFrame><extraFrames>0</extraFrames><path>/Volumes/TOSHIBA EXT/SuperResData/DNA-PAINT.tif</path></gdsc.smlm.ij.IJImageSource>
#Bounds x0 y0 w428 h684
#Calibration <gdsc.smlm.results.Calibration><nmPerPixel>117.0</nmPerPixel><gain>2.17</gain><exposureTime>50.0</exposureTime><readNoise>0.0</readNoise><bias>0.0</bias><emCCD>false</emCCD><amplification>0.0</amplification></gdsc.smlm.results.Calibration>
#Configuration <gdsc.smlm.engine.FitEngineConfiguration><fitConfiguration><fitCriteria>LEAST_SQUARED_ERROR</fitCriteria><delta>1.0E-4</delta><initialAngle>0.0</initialAngle><initialSD0>2.0</initialSD0><initialSD1>2.0</initialSD1><computeDeviations>false</computeDeviations><fitSolver>LVM</fitSolver><minIterations>0</minIterations><maxIterations>20</maxIterations><significantDigits>5</significantDigits><fitFunction>CIRCULAR</fitFunction><flags>20</flags><backgroundFitting>true</backgroundFitting><notSignalFitting>false</notSignalFitting><coordinateShift>4.0</coordinateShift><shiftFactor>2.0</shiftFactor><fitRegion>0</fitRegion><coordinateOffset>0.5</coordinateOffset><signalThreshold>0.0</signalThreshold><signalStrength>30.0</signalStrength><minPhotons>0.0</minPhotons><precisionThreshold>10000.0</precisionThreshold><precisionUsingBackground>false</precisionUsingBackground><nmPerPixel>103.0</nmPerPixel><gain>2.17</gain><emCCD>false</emCCD><modelCamera>false</modelCamera><noise>0.0</noise><minWidthFactor>0.5</minWidthFactor><widthFactor>1.01</widthFactor><fitValidation>true</fitValidation><lambda>10.0</lambda><computeResiduals>false</computeResiduals><duplicateDistance>0.5</duplicateDistance><bias>0.0</bias><readNoise>0.0</readNoise><amplification>0.0</amplification><maxFunctionEvaluations>2000</maxFunctionEvaluations><searchMethod>POWELL_BOUNDED</searchMethod><gradientLineMinimisation>false</gradientLineMinimisation><relativeThreshold>1.0E-6</relativeThreshold><absoluteThreshold>1.0E-16</absoluteThreshold></fitConfiguration><search>2.5</search><border>1.0</border><fitting>3.0</fitting><failuresLimit>10</failuresLimit><includeNeighbours>true</includeNeighbours><neighbourHeightThreshold>0.3</neighbourHeightThreshold><residualsThreshold>1.0</residualsThreshold><noiseMethod>QUICK_RESIDUALS_LEAST_MEAN_OF_SQUARES</noiseMethod><dataFilterType>SINGLE</dataFilterType><smooth><double>0.5</double></smooth><dataFilter><gdsc.smlm.engine.DataFilter>MEAN</gdsc.smlm.engine.DataFilter></dataFilter></gdsc.smlm.engine.FitEngineConfiguration>
#frames	origX	origY	origValue	Error	Noise	Background	Signal	Angle	X	Y	X SD	Y SD	Precision
""")

    print("Done")
    Out_nc.write(fit1.to_csv(sep = '\t',header=False,index=False))    # Write the columns that are required (without the non-clustered localisations)
    
    
    Out_nc.close() # Close the file.

