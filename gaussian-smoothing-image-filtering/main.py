#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 15:42:34 2025

author: @varenyam malhotra

"""

# -*- coding: utf-8 -*-

# The following commented out code is just a first attempt at trying to avert 
# an error that kept coming up regarding NoneType and padding

'''
from Image2D import Image2D
from Filter import Filter
import matplotlib.pyplot as plt
import os
import numpy as np

def create_dummy_mri():
    print("Creating a valid dummy mri.raw file (176 x 256)...")
    dummy = np.random.randint(0, 65536, size=(176, 256), dtype='uint16')
    dummy = np.asfortranarray(dummy)  # this forces Fortran-style layout in memory
    dummy.flatten(order='F').tofile("mri.raw")
    print("Dummy created. Bytes:", dummy.nbytes)


def main():
    
    I = Image2D(256,176,'uint16', fileName='mri.raw')
    I1 = I.transpose()
    
    GaussianF=Filter([7,7])
    
    smoothed_img = GaussianF.gaussFilt(I1)
    smoothed_img.write("mri_smooth_gauss_771.raw")
    I1.showSub(smoothed_img,titleSelf="Original Image",titleOther= "Gaussian smoothed 771")
    
    smoothed_bil=GaussianF.bilateralFilt(I1,sigma_d=1,sigma_r=60)
    smoothed_bil.write("mri_smooth_bilateral_771_60.raw")
    I1.showSub(smoothed_bil,titleSelf="Original Image",titleOther="Bilateral smoothed 881_60")
    
    expected_size = 256 * 176 * 2  # uint16 = 2 bytes
    if not os.path.exists("mri.raw") or os.path.getsize("mri.raw") != expected_size:
        create_dummy_mri()

    try:
        I = Image2D(256, 176, 'uint16', fileName='mri.raw', order='F') # Correct dimensions for order='F'
        print("Image loaded. Shape:", I.pixels.shape)
    except Exception as e:
        print("Failed to load image:", e)
        return

    I1 = I.transpose()
    if I1 is None:
        print("Transpose failed. Exiting.")
        return

    print("Transpose successful. Shape:", I1.pixels.shape)

    # Gaussian filtering
    try:
        G_filter = Filter([7, 7])
        I_gauss = G_filter.gaussFilt(I1, sigma_d=1)
        I_gauss.write("mri_smooth_gauss_771.raw")
        print("Gaussian smoothing complete.")
    except Exception as e:
        print("Gaussian filter failed:", e)
        return

    # Bilateral filtering
    try:
        B_filter = Filter([7, 7])
        I_bilateral = B_filter.bilateralFilt(I1, sigma_d=1, sigma_r=60)
        I_bilateral.write("mri_smooth_bilateral_771_60.raw")
        print("Bilateral smoothing complete.")
    except Exception as e:
        print("Bilateral filter failed:", e)
        return

    # Plot results
    try:
        I1.showSub(I_gauss, titleSelf="Original image", titleOther="Gaussian smoothed")
        plt.savefig("Original_Gauss771.png")

        I1.showSub(I_bilateral, titleSelf="Original image", titleOther="Bilateral smoothed")
        plt.savefig("Original_Bilateral771_60.png")

        print("Images saved successfully.")
    except Exception as e:
        print("Plotting failed:", e)
'''

# The following is the actual, correct version of the main methods and files.

import numpy as np
import os
import matplotlib.pyplot as plt
from Image2D import Image2D
from Filter import Filter

def create_dummy_mri():
    '''
    

    Returns
    -------
    None.

    '''
    print("Creating a valid dummy mri.raw file (176 x 256)...")
    dummy = np.random.randint(0, 65536, size=(176, 256), dtype='uint16')
    dummy = np.asfortranarray(dummy)
    dummy.flatten(order='F').tofile("mri.raw")
    print("Dummy created. Bytes:", dummy.nbytes)

def main():
    
    # Checking for the mri.raw file
    expected_size = 256 * 176 * 2
    if not os.path.exists("mri.raw") or os.path.getsize("mri.raw") != expected_size:
        create_dummy_mri()

    # Loading the image from the file
    try:
        I = Image2D(256, 176, 'uint16', fileName='mri.raw', order='F')
        print("Image loaded. Shape:", I.pixels.shape)
    except Exception as e:
        print("Failed to load image:", e)
        return

    # Transposing the image
    I1 = I.transpose()
    if I1 is None:
        print("Transpose failed. Exiting.")
        return
    print("Transpose successful. Shape:", I1.pixels.shape)

    # Applying a Gaussian filter
    try:
        G_filter = Filter([7, 7])
        I_gauss = G_filter.gaussFilt(I1, sigma_d=1)
        I_gauss.write("mri_smooth_gauss_771.raw")
        print("Gaussian smoothing complete.")
    except Exception as e:
        print("Gaussian filter failed:", e)
        return

    # Applying a Bilateral Filter
    try:
        B_filter = Filter([7, 7])
        I_bilateral = B_filter.bilateralFilt(I1, sigma_d=1, sigma_r=60)
        I_bilateral.write("mri_smooth_bilateral_771_60.raw")
        print("Bilateral smoothing complete.")
    except Exception as e:
        print("Bilateral filter failed:", e)
        return

    # Displaying and Saving the Output Images
    try:
        I1.showSub(I_gauss, titleSelf="Original image", titleOther="Gaussian smoothed")
        plt.savefig("Original_Gauss771.png")

        I1.showSub(I_bilateral, titleSelf="Original image", titleOther="Bilateral smoothed")
        plt.savefig("Original_Bilateral771_60.png")

        print("Images saved successfully.")
    except Exception as e:
        print("Plotting failed:", e)

# Just the final line to get the main method good to go and up and running! 
# Runs when the script is executed! 
if __name__ == "__main__":
    main()
