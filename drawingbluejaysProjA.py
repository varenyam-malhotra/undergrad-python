# -*- coding: utf-8 -*-

# Varenyam Malhotra
# Feb 17 2025
# Gateway Computing Python Project A
# Professor Oses
# Johns Hopkins University

from graphics import *
import random
import math

def drawCircle(p, r, color, win):
    """
    Draws a circle of specified color and radius r centered at point p 
    in window win

    Parameters
    ----------
    p : Point
        Center point.
    r : float
        radius.
    color : string
        Color of circle.
    win : GraphWin
        Graphics Window.

    Returns
    -------
    None.

    """
    
    C = Circle(p, r)
    C.setFill(color)
    C.setOutline(color)
    C.draw(win)
    
def drawTriangle(p0, p1, p2, color, win):
    """
    Draws a triangle of specified color with corners points p0, p1 and p2
    in window win

    Parameters
    ----------
    p0 : Point
        First point.
    p1 : Point
        Second point.
    p2 : Point
        Thrid point.
    color : string
        Color of triangle.
    win : GraphWin
        Graphics Window.

    Returns
    -------
    None.

    """
    T = Polygon([p0,p1,p2])
    T.setFill(color)
    T.setOutline(color)
    T.draw(win)


def bluejay(x, y, s, win):
    """
    Draws a bluejay inside box of size s at (x,y)

    Parameters
    ----------
    x : float
        x-coordinate of upper left corner.
    y : float
        y-coordinate of upper left corner.
    s : float
        size of box.
    win : GraphWin
        Graphics Sindow.

    Returns
    -------
    None.

    """
    # Draw Box 
    p0 = Point(x, y)
    p1 = Point(x+s, y+s)
    box = Rectangle(p0, p1)
    box.setOutline("black")
    box.draw(win) # Comment this line to hide box
    
    # 4.1: Drawing the Body
    # Use drawCircle to draw the body circle with given dimensions
    # The center of the body
    body_center = Point(x + 0.65 * s, y + 0.65 * s)
    # The radius of the body
    body_radius = 0.35 * s
    # Now drawing the blue circle for the body in win 
    drawCircle(body_center, body_radius, "blue", win)
    
    # 4.2: Drawing the Head
    # Use the drawCircle to draw head circle with given dimensions
    head_center = Point(x + 0.65 * s, y + 0.2 * s)
    head_radius = 0.2 * s
    drawCircle(head_center, head_radius, "blue", win)
    
    # 4.3: Drawing the Eye
    # Use drawCircle with given dimensions
    eye_center = Point(x + 0.65 * s, y + 0.2 * s)
    eye_radius = 0.05 * s
    drawCircle(eye_center, eye_radius, "black", win)
    
    # 4.4: Drawing the Beak
    # Using drawTriangle using corner points based on given dimensions
    beak_tip = Point(x + s, y + 0.2 * s)
    # We can call getX and getY from the Point class instead of repeating x and y coordinate calculations
    beak_top_point = Point(head_center.getX() + head_radius, head_center.getY() - eye_radius)
    beak_bottom_point = Point(head_center.getX() + head_radius, head_center.getY() + eye_radius)
    # Now drawing the orange triangle for the beak of the blue jay
    drawTriangle(beak_tip, beak_top_point, beak_bottom_point, "orange", win)
    
    # 4.5: Drawing the Tail
    tail_point1 = Point(head_center.getX() - head_radius/(math.sqrt(2)), head_center.getY() + head_radius/(math.sqrt(2)))
    tail_point2 = Point(x, y + s)
    tail_point3 = Point(x + 0.65 * s, y + s)
    drawTriangle(tail_point1, tail_point2, tail_point3, "blue", win)
    
    # 4.6: Drawing the Hair of the bluejay
    hair_point1 = tail_point1
    hair_point2 = Point(head_center.getX(), head_center.getY() - head_radius)
    hair_point3 = Point(x + 0.25 * s, y)
    drawTriangle(hair_point1, hair_point2, hair_point3, "blue", win)
    
  
def overlap(x0, y0, s0, x1, y1, s1):
    """
    Function to determine if two bluejays (their squares) overlap with each other

    Parameters
    ----------
    x0 : float, x-coordinate of center of first bluejay
    y0 : float, y-coordinate of center of first bluejay
    s0 : float, side size of first bluejay
    x1 : float, x-coordinate of center of second bluejay
    y1 : Tfloat, y-coordinate of center of second bluejay
    s1 : float, side size of second bluejay

    Returns
    -------
    bool
        True or false depending on whether the bluejays (their squares) overlap or not

    """
    if (x0 >= x1 - s0) and (x0 <= x1 + s1) and (y0 >= y1 - s0) and (y0 <= y1 + s1):
        return True
    else:
        return False
    

def newXY(XY, s, win):
    """
    Finds a new random coordinate (x,y) of box of size s in window which
    does not overlap with boxes listed in XY

    Parameters
    ----------
    XY : list
        Current boxes in format [(x0,y0), (x1,y1), ...] .
    s : float
        size of box.
    win : GraphWin
        Graphics Window.

    Returns
    -------
    x0 : float
        New x-coordinate.
    y0 : float
        New y-coordinate.
    """
    length = win.getHeight()
    (x0, y0) = (random.randint(0,length-s), random.randint(0,length-s))
    
    while any([overlap(x0, y0, s, x1, y1, s) for (x1,y1) in XY]):
        (x0, y0) = (random.randint(0,length-s), random.randint(0,length-s))
    
    XY.append((x0,y0))
    return (x0, y0)  
    
def flock(n, s, win):
    """
    This function actually draws the bluejays of n number and s size in the window
    It uses random coordinates obtained from the newXY method

    Parameters
    ----------
    n : int, number of bluejays
    s : float, size of each bluejay (the size of the side of the bluejay square)
    win : the graphics window

    Returns
    -------
    None.

    """
    # Draw grass
    length = win.getHeight()
    
    p0 = Point(0,0)
    p1 = Point(length,length)
    sky = Rectangle(p0, p1)
    sky.setFill("lightgreen")
    sky.setOutline("lightgreen")
    sky.draw(win)
    
    # Create empty list to store box coordinates
    XY = []
    
    # Use for loop to create n bluejays
    for i in range(0, n):   
        (x,y) = newXY(XY, s, win)
        bluejay(x, y, s, win)
        

def main():
    """
    Main function

    Returns
    -------
    None.

    """
    # Create graphics window
    length = 500
    win = GraphWin("Flock", length, length)
    
    # Two lines of code below to test the code output
    bluejay(200,200,100, win)
    flock(5, 100, win)
    
    # Close after mouse click
    try:
        win.getMouse()    
        win.close()
    except:
        pass
    

if __name__ == "__main__":
    main()


