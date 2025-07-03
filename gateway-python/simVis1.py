#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class objects for Visualization

@author: siamak
"""



import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
#import time



class visualize:
    
    np.random.seed(123456789)
    
    colorDict = {0: 'green', 1:'red', 2:'gray', 3:'black'}
    faceColorDict = {0: (0, 1, 0, .3) , 1: (1, 0, 0, .3), \
                     2: (0.5, 0.5, 0.5, .3),3: (0, 0, 0, .8)}
    
    
    def __init__(self,figwWidth=5,figHeight=5,pauseTime=0.001, 
                 Ax1xmin=0,Ax1xmax = 1, Ax1ymin = 0, Ax1ymax = 1):
        
        
        self.figwWidth = figwWidth
        self.figHeight = figHeight
        
        self.Ax1xmin = Ax1xmin
        self.Ax1xmax = Ax1xmax
        self.Ax1ymin = Ax1ymin
        self.Ax1ymax = Ax1ymax
        
        self.pauseTime = pauseTime
        
        self.f, self.ax1 = plt.subplots(1, 1,figsize=(self.figwWidth,self.figHeight ))
        self.setAx1Limits()
        
        
        
    def circle(self,x, y, radius,colorCode):
        """
        Draw one circle with center placed at x and y and radius value of radius. Sets 
        edge and facecollors based on the colorCode.

        Parameters
        ----------
        x : float
            x-coordinate of the center
        y : float
            y-coordinate of the center
        radius : float
            radius of the circle
        colorCode : integer
           defines the face and edge colors  using class dictionary  attributes.

        Returns
        -------
        None.

        """
        
    
        circle = Circle((x, y), radius , edgecolor=self.colorDict[colorCode] ,facecolor=self.faceColorDict[colorCode])
        self.ax1.add_artist(circle)
        self.setAx1Limits()
        

            
            
    def getXminMax(self):
        """
        gets axis 1 x-min and x-max values

        Returns
        -------
        None.

        """
        
        self.Ax1xmin, self.Ax1xmax = self.ax1.axes.get_xlim() 


    def getYminMax(self):
        """
        gets axis 1 y-min and y-max values

        Returns
        -------
        None.

        """
        
        self.Ax1ymin, self.Ax1ymax = self.ax1.axes.get_xlim() 
        
    def setAx1Limits(self):
        """
        sets axis 1 x and y limits

        Returns
        -------
        None.

        """
        
        self.ax1.set_xlim([self.Ax1xmin, self.Ax1xmax])
        self.ax1.set_ylim([self.Ax1ymin, self.Ax1ymax])
        
    
 
    
    
    def plotPause(self):
        """
        Pauses the plot for the duration of pauseTime

        Returns
        -------
        None.

        """
        
        plt.pause(self.pauseTime)
        
    def axis1Clear(self):
        """
        Clears axis 1 in subplot (left panel)

        Returns
        -------
        None.

        """
        
        self.ax1.cla()
        
    # For debugging
    def addText(self,circlesX,circlesY):
        
        font = {'family': 'serif',
        'color':  'black',
        'weight': 'bold',
        'size': 8
        }

        # #add text with custom font
        # for i, j, k in zip(Agents.x,Agents.y,np.arange(0,Agents.getNumberOfCircles()+1)):
        #     self.ax1.text(i, j, k, fontdict=font)
            
        #add text with custom font
        for i, j, k in zip(circlesX,circlesY,np.arange(0,2+1)):
            self.ax1.text(i , j - 0.03, k+1, fontdict=font)
            
    def addLine(self,circlesX,circlesY,line_style = '--',marker='.'):
        
        self.ax1.plot(circlesX,circlesY,linestyle = line_style, marker = marker)
        self.setAx1Limits()
        
    def drawVector(self,initial_point,vector):
        
        self.ax1.arrow(initial_point[0],initial_point[1], 
                        vector[0],vector[1],
                        head_width=0.01,head_length=0.01, color='r')
        #angles='xy', scale_units='xy', 
        self.setAx1Limits()
            
            
if __name__ == '__main__':
    
    pass
    
    

    