#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 12:40:39 2025

author: @varenyam malhotra

"""
import numpy as np
import matplotlib.pyplot as plt

class Image2D:
    def __init__(self, width, height, dType, dataArray=None, fileName=None, order='F'):
        """
        Initializes an Image2D object using a data array or a binary file.

        Parameters
        ----------
        width : int type that is the width of the image in pixels.
        height : int type that is the height of the image in pixels.
        dType : str or numpy dtype that is the data type for the pixel values 
        dataArray : numpy.ndarray type that is the 2D array of pixel values to 
                initialize the image.
        fileName : str type that is the binary file from which to read pixel values.
        order : str type that is the memory layout for reshaping the 
                binary file data ('F' or 'C'). Default is 'F'.

        Raises
        ------
        Exception if both dataArray and fileName are provided.
        AssertionError if the dimensions of dataArray don't match the provided
                width and height.
        """
        self.dType = dType
        self.height = height
        self.width = width

        if fileName is None and dataArray is None:
            self.pixels = np.zeros((height, width), dtype=self.dType)

        elif dataArray is not None and fileName is None:
            assert self.width == dataArray.shape[1] and self.height == dataArray.shape[0], \
                "width or height are not matching the provided data array dimensions!"
            self.pixels = dataArray.astype(self.dType)

        elif dataArray is None and fileName is not None:
            try:
                self.read(fileName, order)
            except Exception as e:
                print(e, f"Issue with processing {fileName} file. Initializing image 2D array to all zeros.")
                self.pixels = np.zeros((height, width), dtype=self.dType)

        else:
            raise Exception('Cannot provide a file name and data array at the same time!')

    def read(self, fileName, order='F'):
        '''
        Reads image data from a binary file and reshapes it to the specified dimensions.

        Parameters
        ----------
        fileName : str tyoe that is the path to the binary image file.
        order : str type that is the memory layout to use when reshaping ('F' or 'C'). 
                Default is 'F'.

        Raises
        ------
        IOError if the file cannot be read.
        ValueError if reshaping fails due to a size mismatch.

        '''
        try:
            data = np.fromfile(fileName, dtype=self.dType, sep="")
        except:
            raise IOError("\nError: cannot find file or read data\n")
        else:
            try:
                dataArray = np.reshape(data, (self.height, self.width), order)
                self.pixels = dataArray
            except:
                raise ValueError('\nWas not able to reshape data following reading' \
                                 ' it from a file. Check if data dimensions are' \
                                 ' consistent with prescribed image width and height.\n')

    def write(self, fileName):
        '''
        Writes the pixel data to a binary file.

       Parameters
       ----------
       fileName : str type that is the destination file name for storing the image.

       Raises
       ------
       IOError if an error occurs during file writing.

        '''
        try:
            with open(fileName, 'wb') as binwrite:
                self.pixels.astype(self.dType).tofile(binwrite)
        except IOError:
            raise IOError('\nAn error occurred trying to write the file.')

    def show(self, title=""):
        '''
        Displays the image in grayscale using matplotlib.

        Parameters
        ----------
        title : str type that is the title of the image window. Default is an empty string.
        '''
        plt.figure()
        plt.imshow(self.pixels, cmap=plt.cm.gray)
        plt.axis('off')
        plt.title(title)
        plt.show()

    def showSub(self, other, titleSelf="", titleOther=""):
        '''
        Displays this image and another image side-by-side.

        Parameters
        ----------
        other : Image2D that is another Image2D object to compare with.
        titleSelf : str type that is the title of the current image. Default is "".
        titleOther : str type that is the title of the other image. Default is "".

        '''
        plt.figure()
        plt.subplot(121)
        plt.imshow(self.pixels, cmap=plt.cm.gray)
        plt.axis('off')
        plt.title(titleSelf)

        plt.subplot(122)
        plt.imshow(other.pixels, cmap=plt.cm.gray)
        plt.axis('off')
        plt.title(titleOther)

        plt.show()

    def getWidth(self):
        '''
        Returns the width of the image.

        Returns
        -------
        int that is the width of the image (number of columns).

        '''
        return self.pixels.shape[1]

    def getHeight(self):
        '''
        Returns the height of the image.

        Returns
        -------
        int that is the height of the image (number of rows).

        '''
        return self.pixels.shape[0]

    def getDataType(self):
        '''
        Returns the data type of the image.

        Returns
        -------
        dtype that is the data type of the pixel values.

        '''
        return self.dType

    def transpose(self):
        '''
        Returns a transposed version of the image.

        Returns
        -------
        Image2D that is a new Image2D object with rows and columns swapped.
        '''
        transposed_array = self.pixels.T
        return Image2D(
            width=transposed_array.shape[1],
            height=transposed_array.shape[0],
            dType=self.dType,
            dataArray=transposed_array
        )

    def padImage(self, filterSize, padValue=0):
        '''
        Pads the image with a border for filtering operations.

        Parameters
        ----------
        filterSize : list or tuple of two ints that is the size of the filter (height, width)
        padValue : float or int that is the value used for padding. The default is 0.

        Returns
        -------
        numpy.ndarray that is the padded version of the image.

        '''
        S1, S2 = filterSize
        R1 = (S1 - 1) // 2
        R2 = (S2 - 1) // 2
        return np.pad(self.pixels, ((R1, R1), (R2, R2)), mode='constant', constant_values=padValue)

    def __str__(self):
        '''
        Returns a string summary of the image including dimensions and a preview.

        Returns
        -------
        str that is a summary of the image content and metadata.
        '''
        rows = self.pixels.shape[0]
        result = f"Image2D Object:\nWidth: {self.getWidth()}, Height: {self.getHeight()}, DataType: {self.dType}\nPixels:\n"

        if rows <= 10:
            result += str(self.pixels)
        elif 10 < rows <= 20:
            top = self.pixels[:10]
            bottom = self.pixels[10:]
            result += f"{top}\n...\n{bottom}"
        else:
            top = self.pixels[:10]
            bottom = self.pixels[-10:]
            result += f"{top}\n...\n{bottom}"

        return result