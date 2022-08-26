#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 16:41:37 2022

@author: pele
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from sklearn.cluster import DBSCAN
from skimage import filters,measure
import seaborn as sns


path = r"/Volumes/Noe PhD 2/Analysis/20220810ibd5/DBSCAN/A4-1/10_10Tom20_DBSCAN/"


file = "10_10all.csv"

os.chdir(path)
locs = pd.read_table(file)
locs_1 = locs.reindex(columns=['Unnamed: 0', 'yw', 'xw', 'cluster'])
     
                 
sns.scatterplot(data=locs_1, x="yw", y="xw", s=10, edgecolor="none", hue="cluster")
plt.show()

