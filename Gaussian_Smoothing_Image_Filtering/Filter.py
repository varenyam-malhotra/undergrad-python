#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 12:42:33 2025

author: @varenyam malhotra

"""
import numpy as np
from Image2D import Image2D

class Filter:
    def __init__(self, size):
        '''
        This method initializes the filter with a certain given kernel size

        Parameters
        ----------
        size : list or tuple of two odd integers. This represents the size of
            the filter kernel (height and width). Both values must be odd. 

        Raises
        ------
        ValueError
            If size isn't a two element tuple or list of odd integers.

        '''
        if not (isinstance(size, (list, tuple)) and len(size) == 2):
            raise ValueError("size must be a list or tuple with two elements.")
        if size[0] % 2 == 0 or size[1] % 2 == 0:
            raise ValueError("both elements of size must be odd integers.")
        self.size = size
        self.center_index = ((size[0] - 1) // 2, (size[1] - 1) // 2)

    def computeSpatialWeights(self, sigma=1, normalize=True):
        '''
        Computes, for the given filter size, a Gaussian spatial weight matrix.

        Parameters
        ----------
        sigma : float which is the standard deviation for the Gaussian function.
                The default is 1.
        normalize : boolean that is whether to normalize the matrix so its sum is 1.
                The default is True.

        Returns
        -------
        H : of numpy.ndarray that is a 2D array of spatial Gaussian weights. 

        '''
        S1, S2 = self.size
        R1, R2 = self.center_index
        H = np.zeros((S1, S2), dtype=float)
        for i in range(S1):
            for j in range(S2):
                dist_sq = (i - R1) ** 2 + (j - R2) ** 2
                H[i, j] = np.exp(-dist_sq / (2 * sigma ** 2))
        if normalize:
            H /= np.sum(H)
        return H

    def computeRangeWeights(self, center_val, patch_vals, sigma_r):
        '''
        Computes range weight matrix based on intensity differences

        Parameters
        ----------
        center_val : float that is intensity of center pixel
        patch_vals : numpy.ndarray that is a 2D array representing the local 
                    patch of pixel intensities. 
        sigma_r : float that is standard deviation for range Gaussian function. 

        Returns
        -------
        weights : numpy.ndarray that is 2D array or range weights for the patch. 

        '''
        diff = patch_vals - center_val
        weights = np.exp(-(diff ** 2) / (2 * sigma_r ** 2))
        return weights

    def computeBilateralResponse(self, spatialWeights, rangeWeights, patch):
        '''
        Combines spatial and range weights to compute filtered pixel value.

        Parameters
        ----------
        spatialWeights : numpy.ndarray that is a 2D array of precomputed spatial weights.
        rangeWeights : numpy.ndarray that is 2D array of range weights based 
                    on the intensity patch.
        patch : numpy.ndarray that is a 2dD array of pixel intensities

        Returns
        -------
        float that is the bilaterally filtered intensity value for the center pixel

        '''
        H = spatialWeights * rangeWeights
        norm = np.sum(H)
        if not np.isclose(norm, 0):
            H /= norm
            return np.sum(H * patch)
        else:
            return patch[self.center_index[0], self.center_index[1]]

    def gaussFilt(self, img_obj, sigma_d=1):
        '''
        This method a pplies Gaussian smoothing to given Image2D object.

        Parameters
        ----------
        img_obj : Image2D type. Is the input image to be filtered.
        sigma_d : float that is the standard deviation of the spatial Gaussian 
                kernel. Default is 1.

        Returns
        -------
        Image2D
            New Image2D object containing the smoothed image.
        '''
        kernel = self.computeSpatialWeights(sigma=sigma_d, normalize=True)
        R1, R2 = self.center_index
        padded = img_obj.padImage(self.size, padValue=0).astype(float)
        h, w = img_obj.getHeight(), img_obj.getWidth()
        result = np.zeros((h, w), dtype=float)
        for i in range(h):
            for j in range(w):
                patch = padded[i:i+self.size[0], j:j+self.size[1]]
                result[i, j] = np.sum(patch * kernel)
        # result = np.clip(result, 0, np.iinfo(img_obj.pixels.dtype).max)
        dtype = img_obj.pixels.dtype
        info = np.iinfo(dtype) if np.issubdtype(dtype, np.integer) else np.finfo(dtype)
        result = np.clip(result, 0, info.max)
        return Image2D(w, h, img_obj.dType, dataArray=result.astype(img_obj.pixels.dtype))

    def bilateralFilt(self, img_obj, sigma_d=1, sigma_r=100):
        '''
        
        This applies bilateral filtering to the given Image2D object to smooth the image
        while preserving its edges.

        Parameters
        ----------
        img_obj : Image2D type; the input image to be filtered.
        sigma_d : float, the standard deviation of the spatial Gaussian kernel. 
                Default is 1.
        sigma_r : float that is the standard deviation of the range Gaussian 
                kernel. Default is 100.

        Returns
        -------
        Image2D that is the new Image2D object containing the bilaterally filtered image.

        '''
        spatial_weights = self.computeSpatialWeights(sigma=sigma_d, normalize=False)
        R1, R2 = self.center_index
        padded = img_obj.padImage(self.size, padValue=0).astype(float)
        h, w = img_obj.getHeight(), img_obj.getWidth()
        result = np.zeros((h, w), dtype=float)
        for i in range(h):
            for j in range(w):
                patch = padded[i:i+self.size[0], j:j+self.size[1]]
                center_val = padded[i + R1, j + R2]
                range_weights = self.computeRangeWeights(center_val, patch, sigma_r)
                result[i, j] = self.computeBilateralResponse(spatial_weights, range_weights, patch)
        # result = np.clip(result, 0, np.iinfo(img_obj.pixels.dtype).max)
        dtype = img_obj.pixels.dtype
        info = np.iinfo(dtype) if np.issubdtype(dtype, np.integer) else np.finfo(dtype)
        result = np.clip(result, 0, info.max)
        return Image2D(w, h, img_obj.dType, dataArray=result.astype(img_obj.pixels.dtype))
