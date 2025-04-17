#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 20:59:54 2025

@author: vena
"""

import math

class Point:

    def __init__(self, x=0, y=0):
        """
        Define the Point class to be initializaed with default values of 0 for x and y

        Parameters
        ----------
        x : TYPE, the x-coordinate. The default is 0.
        y : TYPE, the y-coordinate. The default is 0.

        Returns
        -------
        None.

        """
        self.x = x
        self.y = y

    # In this method we are going to call the Point class inside of the Point class
    # We can do this because it is already defined 
    # And we are just creating a new instance of the Point Class   
    def __add__(self, other): # see we are passing two Point instances anyway - self and other
        '''
        Defining a method to add two Point classes together

        Parameters
        ----------
        x : int or float, the x-coordinate. The default is 0.
        y : int or float, the y-coordinate. The default is 0.

        Returns
        -------
        The Point object that is equivalent to the two objects added together

        
        '''
        return Point(self.x + other.x, self.y + other.y)
    
    # Same thing for the sub overloading method
    def __sub__(self, other):
        """
        
        Defining a method to subtract two Point instances
        
        Parameters
        ----------
        other : Another Point instance like self. We are adding these two together
        These are basically TUPLES of two int/float objects

        Returns
        -------
        Another point instance

        """
        return Point(self.x - other.x, self.y - other.y)
    
    # The iadd and isub methods are overloading the += and -= operators
    # So basically this just adds to (updates) the original value rather than adding them together

    def __iadd__(self, other):
        '''
        A method two add a Point instance to another instance rather than add them together

        Parameters
        ----------
        other : Another Point instance

        Returns
        -------
        A tuple that is another Point class instance

        '''
        self.x += other.x
        self.y += other.y
        return self # See this also will just return the self object as a Point instance
    
    def __isub__(self, other):
        """
       A method two add a Point instance to another instance rather than add them together

       Parameters
       ----------
       other : Another Point instance

       Returns
       -------
       A tuple that is another Point class instance


        """
        self.x -= other.x
        self.y -= other.y
        return self  

    def __repr__(self):
        '''
        Returns user friendly string

        Returns
        -------
        string that is simply user-friendly and easier to understand

        '''
        return 'x: ' + str(round(self.x,4)) + ' y: ' + str(round(self.y,4))

    def __str__(self):
        '''
        Returns user friendly string

        Returns
        -------
        String, exactly same as last method

        '''
        return 'x: ' + str(round(self.x,4)) + ' y: ' + str(round(self.y,4))
        

    pass
    
class Vec2D(Point): # This is a child of the Point class

    def __init__(self, a = None, b = None):
        """
        Essentially just defining a Vec2D instance object in four different ways
        
        A child of Point class, only difference is ways it can be initialized and default values
        
        Parameters
        ----------
        a : Tuple of ints/floats for the object and the default is None. 
        b : Tuple of ints/floats for the object and the default is None
        Raises
        ------
        ValueError
            If there is something such as the wrong type inserted in 

        Returns
        -------
        None.

        """
        if a is None and b is None: # First way of implementing where we pass nothing
            self.x, self.y = 0, 0
        elif isinstance(a, Point) and b is None: # Second way where we pass only one object arguments
            self.x, self.y = a.x, a.y
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)): # Third way where we pass two object arguments
            self.x, self.y = float(a), float(b)
        elif isinstance(a, Point) and isinstance(b, Point): # Fourth way where we pass to Point objects themselves
            self.x = b.x - a.x
            self.y = b.y - a.y
        else:
            raise ValueError("Invalid arguments for Vec2D constructor") # Error way which is anything else forming an error
        
    # Overriding the method to return a Vec2D object instead of a Point obejct
    def __add__(self, other):
        """
        Adding two Vec2D object instances together
        
        Parameters
        ----------
        other : Vec2D instance just like self

        Returns
        -------
        Vec2D instance of the self and other instances added together

        """
        return Vec2D(self.x + other.x, self.y + other.y)

    # Same for the sub overloading
    def __sub__(self, other):
        """
        Subtracting one Vec2D object instances from another
        
        Parameters
        ----------
        other : Vec2D instance just like self

        Returns
        -------
        Vec2D instance of the self and other instances added together

        """
        return Vec2D(self.x - other.x, self.y - other.y)

    # Now we want to write the mul method
    def __mul__(self, other):
        """
        Method to multiply two instances in a multiple amount of ways
        This includes two object instances together as well as normal scalar multiplication
        
        Parameters
        ----------
        other : Another instance of the Vec2D class

        Raises
        ------
        TypeError
            If something of a different type is used

        Returns
        -------
        an int or float value simply based on the calculations

        """
        # This is for if we are calculating the dot product of two Vec2D or Point objects
        if isinstance(other, Vec2D) or isinstance(other, Point):
            return self.x * other.x + self.y * other.y
        # This is for scalar multiplication
        elif isinstance(other, (int, float)):
            return Vec2D(self.x * other, self.y * other)
        # Raising an error if necessary
        else:
            raise TypeError("Unsupported operand type(s) for *")    
            
    def norm(self):
        """
        Returns the simple magnitude of the vector based on the distance formula

        Returns
        -------
        A specific number that is an int/float

        """
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def normal_ccw(self):
        """
        Simply returns an orthogonal vector by rotating 90 degrees counter-clockwise
        For this, based on a formula, the (x,y) becomes (-y,x)

        Returns
        -------
        A new Vec2D object instance

        """
        # Calculated through the basic rotation formula
        return Vec2D(-self.y, self.x)    
    
    def __str__(self):
        """
        Returns a simple string version of the Vec2D object

        Returns
        -------
        str
            String version of Vec2D object

        """
        return f"x: {self.x} y: {self.y}"

if __name__=='__main__':

    # This is some test code from the file
    
    # 1. Create a point object with no arguments
    a = Point()
    
    # 2. Create a point object with two numbers
    b = Point(2, 1)

    print(a.x, a.y)
    print(b.x, b.y)
    
    # More test code
    
    # Create two point objects
    a = Point(3, 1)
    b = Point(4, 2)

    # Add points
    print(a + b)
    print(type(a + b))

    # Subtract points
    print(a - b)
    print(type(a - b))
    
    # Increment a point
    c = Point(2, 2)
    a += c
    print(a)
    print(type(c))
    
    # Decrement a point
    c = Point(2, 2)
    b -= c

    print(b)
    print(type(b))


    print("---------------------------------------------")
    
    # Now some testing for the Vec2d clsas
    
    # 1. Create a vector object with no arguments
    a = Vec2D()

    # 2. Create a vector object by passing two numbers
    b = Vec2D(3,4)

    # 3. Create a vector object with two point objects
    c = Vec2D(Point(4,5), Point(2,1))

    # 4. Create a vector object with one point object
    d = Vec2D(Point(5,6))
    
    print(a)
    print(b)
    print(c)
    print(d)

    print(Vec2D(4,5) + Vec2D(1, 0) )
    print(Vec2D(4,5) - Vec2D(2, 1) )
    
    # 1. Dot product of two vectors
    dot_prod = Vec2D(4,5) * Vec2D(1, 0)
    print(dot_prod, type(dot_prod))

    # 2. Vector and a point
    dot_prod = Vec2D(4,5) * Point(1, 1)
    print(dot_prod,type(dot_prod))

    # 3. Scaling a vector
    scaled_vec = Vec2D(1,1) * 2
    print(scaled_vec)
    print(type(scaled_vec))
    