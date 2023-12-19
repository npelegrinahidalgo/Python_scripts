#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 19:45:03 2022

@author: pele
"""
# ~~~This is a script to generate a pathlist to open the desired list of pahts

import os
import numpy as np
import pandas as pd
import re


def init():
    fp = (r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_1/")
    print_dirs(2, fp)

def print_dirs(step, fp):
    print('\n\n')
    count = 150
    done = []
    pathlist = []
    for root, dirs, files in os.walk(fp):
        
        
        for name in files:
            if step == 1:
                if 'posZ0.tif' in name:
                
                    for_ij = r'path[{0}]="{1}\";'.format(count, root)
                    if root not in done:
                        done.append(root)
                        print(for_ij.replace('\\', '/'))
                        count += 1
                        
            if step == 2:
                
                if 'posZ0.tif' in name:
                    for_py = 'pathlist.append(r"{0}/")'.format(root)
                
                            
                
                    if for_py not in pathlist:
                        pathlist.append(root)
                    
                        print(for_py)
    print(len(pathlist))
    
    
init()

                
    # # pathlist_fiji = done
    # # pathlist_fiji
    # # to_save = pd.DataFrame(done,index=False)
    
    # # print(len(to_save.columns),
    # #       to_save[3:])
    # # to_save_paths = to_save
    
    
    # to_save_paths.to_csv(fp + "path.txt",sep='\n')
    # print(to_save_paths)
    
    

    



        
# ~~~ For now I am only running the folders path to open with Fiji and python


            # elif step == 3:

            #     if '.png' in name:
            #         for_latex = r'.newpage \r .begin\{figure\}\[hbtp\] \r.centering \r.includegraphics[width=1\textwidth]\{{0}.png\}\r.end\{figure\}\r.newpage\{0\}'.format(count)
            
            #         print(for_latex)
                    
            #         count += 1
            # elif step == 4:
            #     if 'Bottom_For_SR_X0Y0R1W1_Split_1.tif' in name:
            #         for_py = 'pathList.append(r"{0}")'.format(root)
            #         print(for_py)
            #         #print name
            # elif step == 5:

            #     if 'X0Y0R1W2_Apt_1.2_0' in name:
            #         for_igor = r'filelist[{0}]="{1}\"'.format(count, root)
            #         for_igor = for_igor.replace('/',':')
            #         #for_igor = for_igor.replace(':Users','Macintosh HD:Users')
            #         print(for_igor.replace('\\', ':'))
            #         count+=1