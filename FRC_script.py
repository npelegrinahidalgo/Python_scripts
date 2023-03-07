#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 12:24:00 2022

@author: pele
"""
import os
import numpy as np
import pandas
from skimage import color, io
import matplotlib.pyplot as plt


import miplib.ui.plots.image as showim
from miplib.psf import psfgen
from miplib.processing.deconvolution import deconvolve
from miplib.data.messages import image_writer_wrappers as imwrap
import miplib.data.io.read as imread
import miplib.processing.image as imops
from miplib.data.containers.image import Image

import miplib.analysis.resolution.fourier_ring_correlation as frc
from miplib.data.containers.fourier_correlation_data import FourierCorrelationDataCollection

import miplib.ui.plots.frc as frcplots

import miplib.ui.cli.miplib_entry_point_options as options
import urllib.request as dl


path="/Volumes/Noe PhD 1/Microscopes/TIRFM/20220609_ibd12_PFF_seeded/A1+ buffer_2022_06_09_17_22_06/"


filename = "pS129_aSyn.tif"


full_path = os.path.join(path, filename)

# Automatically dowload the file from figshare, if necessary.

image = io.imread(full_path)

# plt.axis('off')
# plt.imshow(image)

n_iterations = 10000
args_list = ("image psf"  
             " --max-nof-iterations={}  --first-estimate=image " 
             " --blocks=1 --pad=0 --resolution-threshold-criterion=fixed "
             " --tv-lambda=0 --bin-delta=1  --frc-curve-fit-type=smooth-spline").format(n_iterations).split()
            
args = options.get_deconvolve_script_options(args_list)

print (args)


frc_results = FourierCorrelationDataCollection()

frc_results[0] = frc.calculate_single_image_frc(image,args)

plotter = frcplots.FourierDataPlotter(frc_results)
plotter.plot_one(0)

