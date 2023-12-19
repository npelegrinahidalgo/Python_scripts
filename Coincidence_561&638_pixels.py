#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 13:28:34 2023

@author: pele

Script to analyse EV data on diffraction-limited data --> Use 638 as mask (EVs labelled with AF647) and compare to 561 (AB signal)
Here the coincidence is calculated per pixel only, instead of per individual EV (i.e. particle)

"""

import os
from skimage.io import imread
from PIL import Image
import matplotlib.pyplot as plt
from skimage import color, io
from skimage.filters import try_all_threshold, threshold_otsu
import numpy as np
from tabulate import tabulate
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt



root_path = r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/"
# inpaths to analyse
pathlist=[]



pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_10/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_11/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_12/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_13/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_14/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_15/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_16/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_17/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_18/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_19/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_20/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_21/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_22/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_23/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_24/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A2/pos_9/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_10/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_11/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_12/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_13/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_14/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_15/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_16/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_17/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_18/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_19/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_20/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_21/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_22/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_23/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_24/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B2/pos_9/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/Beads/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C2/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_10/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_11/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_12/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_13/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_14/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_15/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_16/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_17/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_18/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_19/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_20/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_21/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_22/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_23/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_24/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/A4/pos_9/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_10/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_11/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_12/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_13/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_14/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_15/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_16/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_17/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_18/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_19/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_20/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_21/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_22/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_23/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_24/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/B4/pos_9/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_0/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_1/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_10/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_11/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_12/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_13/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_14/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_15/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_16/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_17/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_18/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_19/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_2/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_20/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_21/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_22/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_23/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_24/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_3/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_4/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_5/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_6/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_7/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_8/")
pathlist.append(r"/Volumes/Noe PhD 3/Microscopes/ONI/20231208_NPH_EVs_PLL_protocol_plate_2/C4/pos_9/")


image_561 = "561_mapped.tif"
image_638 = "638_cropped.tif"


Coincidence_table = pd.DataFrame(columns=["File", "Coincidence", "ID"])


def load_image(toload):
    image=imread(toload).astype("float32")
    return image
    

for path in pathlist:
    
    print(path)
    
    # Define paths for both images:

    path_561 = path + image_561
    
    path_638 = path + image_638
    
    # Load 638 image and mask it (average + 2* std formulae):
        
    im_638 = load_image(path_638)
    plt.imshow(im_638)
    plt.title("638")
    plt.axis('off')
    plt.show()
    
    
    ave_638 = im_638.mean()
    std_638 = im_638.std()
    
    masked_638 = im_638 > ave_638 +  2 * std_638
    plt.imshow(masked_638)
    plt.colorbar()
    plt.show()
    
    # Load 561 image:
        
    im_561 = load_image(path_561)
    plt.imshow(im_561)
    plt.title("561")
    plt.axis('off')
    plt.show()    
    
    
    # Calculate coincidence:
        
    Coincidence = im_561 * masked_638
    plt.imshow(Coincidence)
    plt.title("Coincidence")
    plt.axis('off')
    plt.show()
    
    total_coincidence = sum(sum(Coincidence))
    
    # Save coincidence image (so it can be opened in Fiji)
        
    coincidence_saved = Image.fromarray(Coincidence)
    coincidence_saved.save(path + str("Coincidence_561&638.tif"))
    
    # Add coincidence value to table
    if str("A2") in path:
        
        Coincidence_table = Coincidence_table.append({"File":path, "Coincidence": int(total_coincidence), "ID": str("A2")},ignore_index=True)
    
    if str("B2") in path:
        
        Coincidence_table = Coincidence_table.append({"File":path, "Coincidence": int(total_coincidence), "ID": str("B2")},ignore_index=True)
    
    if str("C2") in path:
        
        Coincidence_table = Coincidence_table.append({"File":path, "Coincidence": int(total_coincidence), "ID": str("C2")},ignore_index=True)
    
    if str("A4") in path:
        
        Coincidence_table = Coincidence_table.append({"File":path, "Coincidence": int(total_coincidence), "ID": str("A4")},ignore_index=True)
    
    if str("B4") in path:
        
        Coincidence_table = Coincidence_table.append({"File":path, "Coincidence": int(total_coincidence), "ID": str("B4")},ignore_index=True)
    
    if str("C4") in path:
        
        Coincidence_table = Coincidence_table.append({"File":path, "Coincidence": int(total_coincidence), "ID": str("C4")},ignore_index=True)
    
Coincidence_table.to_csv(root_path + "Coincidence_561&638.csv", sep = "\t")

Coincidence_table = pd.read_csv(root_path + "Coincidence_561&638.csv", sep = "\t")


# Plot graph for coincidence values

data = Coincidence_table

df = pd.DataFrame(data)

# Calculate mean values per condition
mean_values = df.groupby('ID')['Coincidence'].mean().reset_index()

# Plot individual data points
plt.figure(figsize=(10, 7))

for key, group in df.groupby('ID'):
    plt.plot(group["ID"], group['Coincidence'], marker='p', linestyle='', label=f'ID {key}')

# Plot means
# for index, row in mean_values.iterrows():
#     plt.axhline(row['ID'], color='r', linestyle='--', label=f'Mean for Condition {row["ID"]}')
plt.plot(mean_values["Coincidence"])

plt.bar(mean_values["ID"], height = mean_values["Coincidence"])
plt.show()
# Set labels and title
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Plot of Data Points with Mean per Condition')

x_labels = np.array["EVs only", "0.01% triton", "No EVs", "0.05% triton", "0.005% triton", "0.1% triton"]



plt.xticks(mean_values["ID"], x_labels, rotation='vertical')
plt.axis("on")

# Show legend
plt.legend()

# Show the plot
plt.show()





