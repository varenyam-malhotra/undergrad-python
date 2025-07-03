#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 11:35:00 2024

@author: vena
"""

"""
Project A Template


"""

import math

#from simVis1 import visualize

'''simVis1'''
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
    
'''End Simvis1'''   

    

def main():
    
    # initialize parameters
    
    radius =0.15
    dt =.2
    
    # simulation steps
    simSteps = 800
    

    # Default is Ax1xmin= 0,Ax1xmax = 1, Ax1ymin = 0, Ax1ymax = 1
    vis = visualize() 
    

    x1 = 0.2
    y1 = 0.25
    
    v1x = -0.05
    v1y = -0.05
    
    x2 = 0.7
    y2 = 0.7
    
    
    v2x = 0.05
    v2y = 0.05
    
    
    # run simulation
    simulate(simSteps,vis,x1,y1,x2,y2,v1x,v1y,v2x,v2y,dt,radius)
    


# DO NOT CHANGE THIS FUNCTION
def boundary_locations(vis,radius):
    
    """
    Calculate the boundary locations within the visualization window.
    This function calculates the boundary coordinates for a containing box 
    within the visualization window to ensure that particles 
    do not exceed these boundaries.

    Parameters
    ----------
    vis : visualization object
        The visualization object used for determining window boundaries.
    radius : float
        The radius of the particles.

    Returns
    -------
    xLow : float
        The lower bound of the containing box's threshold to hit the vertical left wall.
    yLow : float
        The lower bound of the containing box's threshold to hit the horizontal bottom wall.
    xHigh : float
        The upper bound of the containing box's threshold to hit the vertical right wall.
    yHigh : float
        The upper bound of the containing box's threshold to hit the horizontal top wall.

    """
    
    # Adjust the boundary according to the 
    # circle radius and display window size
    # Assume circles have the same radius.
    xLow = vis.Ax1xmin + radius 
    xHigh = vis.Ax1xmax - radius 
    
    yLow = vis.Ax1ymin + radius 
    yHigh = vis.Ax1ymax - radius 
    
    return xLow, yLow, xHigh, yHigh
    
    


def updateX(x,vx,dt): 
    
    xnew = x + (vx * dt)
    return xnew

def updateY(y,vy,dt):
    
    ynew = y + (vy * dt)
    return ynew

def boxCollision(x,y,vx,vy,xLow,xHigh,yLow,yHigh):
    
    if x < xLow:
        x = xLow
        vx = -vx
    elif x > xHigh:
        x = xHigh
        vx = -vx
    
    if y < yLow:
        y = yLow
        vy = -vy
    elif y > yHigh:
        y = yHigh
        vy = -vy
        
    return x, y, vx, vy

        
def get_distance(x1,y1,x2,y2):
      
      distance = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1,2))
      return distance  

def Overlap(x1,y1,radius1,x2,y2,radius2):
    
    centers_dist = get_distance(x1,y1,x2,y2)
    radii_sum = radius1 + radius2
    if centers_dist >= radii_sum:
        return False
    elif centers_dist < radii_sum:
        return True

def get_unit_direction(x1,y1,x2,y2):
    
    xunit = (x1 - x2) / math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2))
    yunit = (y1 - y2) / math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2))
        
    return round(xunit, 3), round(yunit,3)
    
def dot_product(x1,y1,x2,y2):
    
    return x1 * x2 + y1 * y2

def update_collision_velocity(x1, y1, v1x, v1y, x2, y2, v2x, v2y):
        
    denominator = (x1 - x2)**2 + (y1 - y2)**2
        
    if denominator == 0:
            
        V1x = -v1x
        V2y = -v1y
        V1x = -v2x
        V2y = -v2y
            
    else:
            
        V1x = v1x - ((v1x - v2x) * (x1 - x2) + (v1y - v2y) * (y1 - y2)) * (x1 - x2) / denominator
        V1y = v1y - ((v1x - v2x) * (x1 - x2) + (v1y - v2y) * (y1 - y2)) * (y1 - y2) / denominator
            
        V2x = v2x - ((v2x - v1x) * (x2 - x1) + (v2y - v1y) * (y2 - y1)) * (x2 - x1) / denominator
        V2y = v2y - ((v2x - v1x) * (x2 - x1) + (v2y - v1y) * (y2 - y1)) * (y2 - y1) / denominator

    V1x = round(V1x, 3)
    V1y = round(V1y, 3)
    V2x = round(V2x, 3)
    V2y = round(V2y, 3)

    return V1x, V1y, V2x, V2y

def circleCollision(x1,y1,radius1,v1x, v1y, x2,y2,radius2,v2x,v2y):
    
    overlap_variable = Overlap(x1, y1, radius1, x2, y2, radius2)
    x1_new, y1_new, v1x_new, v1y_new = x1, y1, v1x, v1y
    x2_new, y2_new, v2x_new, v2y_new = x2, y2, v2x, v2y
    
    if overlap_variable == True:
        v1x_new, v1y_new, v2x_new, v2y_new = update_collision_velocity(x1, y1, v1x, v1y, x2, y2, v2x, v2y)
        unit_dir_x, unit_dir_y = get_unit_direction(x1, y1, x2, y2)
        
        if math.isnan(unit_dir_x) or math.isnan(unit_dir_y):
            unit_dir_x, unit_dir_y = 0.707, 0.707

        overlap = (radius1 + radius2) - get_distance(x1, y1, x2, y2)
            
        displacement_x = unit_dir_x * overlap
        displacement_y = unit_dir_y * overlap
    
        x1_new = x1 + displacement_x
        y1_new = y1 + displacement_y
        
    return round(x1_new, 3), round(y1_new, 3), round(v1x_new, 3), round(v1y_new, 3), round(x2, 3), round(y2, 3), round(v2x_new, 3), round(v2y_new, 3)

# DON NOT CHANGE THIS FUNCTION
def simulate(simSteps,vis,x1,y1,x2,y2,v1x,v1y,v2x,v2y,dt,radius):
    
    """
    Run a particle simulation for a specified number of time steps.

    Parameters
    ----------
    simSteps : int
        Number of time steps to run the simulation.
    vis : visualize
        An instance of the 'visualize' class for visualization.
    x1 : float
        Initial x-coordinate of the center of circle 1.
    y1 : float
        Initial y-coordinate of the center of circle 1.
    x2 : float
        Initial x-coordinate of the center of circle 2.
    y2 : float
        Initial y-coordinate of the center of circle 2.
    v1x : float
        Initial x-component of the velocity of circle 1.
    v1y : float
        Initial y-component of the velocity of circle 1.
    v2x : float
        Initial x-component of the velocity of circle 2.
    v2y : float
        Initial y-component of the velocity of circle 2.
    dt : float
        Time step size for the simulation.
    radius : float
        Radius of both particles.

    Returns
    -------
    None

    """
    
    # This function runs a two-particle simulation for a specified number of 
    # time steps. It updates the positions of two circles and checks for 
    # their collisions with both the container boundary and each other. 
    # The simulation is visualized using the'visualize' class instance 
    # provided as 'vis'.
    
    
    # Identify the boundary location for the containing window
    # Assumption: both particles have the same radius.
    xLow,yLow,xHigh, yHigh = boundary_locations(vis,radius) 
    
    for i in range(simSteps):
        
            
    
    
        # update x, y position of particles
        x1 = updateX(x1,v1x,dt)
        y1 = updateY(y1,v1y,dt)
        
        x2 = updateX(x2,v2x,dt)
        y2 = updateY(y2,v2y,dt)
            
        
                    
        # Check for box and circle collisions
        
        x1,y1,v1x,v1y = boxCollision(x1,y1,v1x,v1y,xLow,xHigh,yLow,yHigh)
        
        
        
        x2,y2,v2x,v2y = boxCollision(x2,y2,v2x,v2y,xLow,xHigh,yLow,yHigh)
        
        
        x1,y1,v1x,v1y, x2,y2,v2x,v2y = circleCollision\
                                      (x1,y1,radius,v1x, \
                                        v1y, x2,y2,radius,v2x,v2y)
                    
        
                    
        # draw circles
        vis.circle(x1, y1, radius, 0)
        vis.circle(x2, y2, radius, 1)
        
                    
        # pause plots and clear window axis 1
        vis.plotPause()
        
        
        vis.axis1Clear()
    
    # redraw circles after last iteration
    vis.circle(x1, y1, radius, 0)
    vis.circle(x2, y2, radius, 1)
        
if __name__ == '__main__': 
    
    # Call the main function to excute the simulation
    # For testing purpose comment main() and call another 
    # function.
    main()
    
    
    