#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 21:05:08 2025

@author: vena
"""

from vec2d import Point
from vec2d import Vec2D

import math


def orient2d(a, b, c):

    '''

    Note that you will need this function only if you plan
    to code up the optional question listed in section 2.4.2
    
    Parameters
    ----------
        a : Point object
        b : Point object
        c : Point object
        
    Returns
    --------
        Integer 1/1/0
        Returns 1 if points are oriented in the 
        counter clockwise direction -1 if clockwise
        and 0 if collinear
        
    '''

    # Signed area of triangle formed by a,b,c
    s_a = (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)
    
    # Orientation
    result = 1 if s_a > 0 else -1 if s_a < 0 else 0
    
    return result



class ConvexPolygon:

    ''' Convex Polygon class definition'''
    
    """
    Represents a convex polygon in 2D space using ordered vertices.

    Attributes:
        nverts (int): Number of vertices
        verts (list of Point): Vertices of the polygon (counter-clockwise)
        edges (list of Vec2D): Edge vectors between consecutive vertices
    """
    
    def __init__(self, points):
        """
        Initialize the polygon by using a list of point objects. 

        Parameters
        ----------
        points : This is the parameter and it it's basically a list of points (the verticies)
        This list is in counter-clockwise order

        Returns
        -------
        None.

        """
        self.nverts = len(points)
        self.verts = points[:]  # shallow copy of points; this basically is a reflection of points list
        # the difference is that if you address it it is the same

        self.edges = []
        for i in range(self.nverts):
            # Edge from vertex i to (i+1)%n as the range
            start = self.verts[i]
            end = self.verts[(i + 1) % self.nverts]
            self.edges.append(Vec2D(start, end))


    def get_centroid(self):
        """
        This basically calculates the weighted center using an area-weighted formula
        Essentially this is equivalent to like the center of mass in physics

        Returns
        -------
        Point object because this is essentially a point that is the center

        """
        A = 0
        Cx = 0
        Cy = 0

        # Remember we can automatically use nverts, verts, and edges because that was defined in the init method
        
        for i in range(self.nverts):
            x0, y0 = self.verts[i].x, self.verts[i].y
            x1, y1 = self.verts[(i + 1) % self.nverts].x, self.verts[(i + 1) % self.nverts].y

            cross = x0 * y1 - x1 * y0
            A += cross
            Cx += (x0 + x1) * cross
            Cy += (y0 + y1) * cross

        A *= 0.5
        Cx /= (6 * A)
        Cy /= (6 * A)

        return Point(Cx, Cy)
    
    def get_perimeter(self):
        """
        This method calculates the perimeter of the polygon
        Done by summing all the norms of all the edge vectors

        Returns
        -------
        perimeter : A float that essentially represents the perimeter of the polygon

        """
        
        perimeter = 0
        for edge in self.edges:
            perimeter += edge.norm() # Add the magnitude of each edge and use the norm method
            # Remember we have imported the vec2d pile originally so we can use the methods from vec2d
        return perimeter
    
    
    def __str__(self):
        
        """
        Basically just returns as a string the number of vertices, edges, and the vertices' coordinates.

        Returns
        -------
        str: this is basically just some coordinate data from the polygon

        """
        
        # These lines allow for the colons to work 
        nv = 'No. of Vertices: '+str(self.nverts)+'\n'
        vs = "Vertices "+" ".join([v.__str__() + ', ' for v in self.verts]) + '\n'
        es = "Edges "+ " ".join([e.__str__() + ', ' for e in self.edges]) 
        return nv + vs + es

    def translate(self, direction):
        """
        This basically translates/moves the entire polygon in the direction of a vector

        Parameters
        ----------
        direction : Vec2D type which gives the direction and distance to move

        Returns
        -------
        None. It just changes it doesn't return anything new.

        """
        
        # Move each vertex by the vector
        for i in range(self.nverts):
            self.verts[i] += direction  # Add the vector to each vertex

        # Find edges again because  vertex positions changed
        self.edges = []
        for i in range(self.nverts):
            start = self.verts[i]
            end = self.verts[(i + 1) % self.nverts]
            self.edges.append(Vec2D(start, end))


    def rotate(self, angle, pivot=None):
        """
        Rotates polygon counter-clockwise by given angle in radians

        Parameters
        ----------
        angle : float is the angle to rotate in radians
        pivot : Tthe point to rotate around as a Point class and it is the centroid as default if it is None

        Returns
        -------
        None. It just updates the vertices and edges in place.

        """
        
        # Use the centroid as the pivot if None
        if pivot is None:
            pivot = self.get_centroid()

        cos_theta = math.cos(angle)
        sin_theta = math.sin(angle)

        new_verts = []

        for pt in self.verts:
            # Translate point so pivot is origin
            dx = pt.x - pivot.x
            dy = pt.y - pivot.y

            # Rotate
            x_new = cos_theta * dx - sin_theta * dy + pivot.x
            y_new = sin_theta * dx + cos_theta * dy + pivot.y

            new_verts.append(Point(x_new, y_new))

        # Update vertices and edges
        self.verts = new_verts
        self.edges = []
        for i in range(self.nverts):
            start = self.verts[i]
            end = self.verts[(i + 1) % self.nverts]
            self.edges.append(Vec2D(start, end))

    def scale(self, sx, sy):
        """
        Scales the polygon

        Parameters
        ----------
        sx : float is the scale factor in the x-direction
        sy : float is the scale factor in the y-direction
        Returns
        -------
        None. It only updates the polygon in place

        """
        
        # Find the centroid; just call the method
        centroid = self.get_centroid()
                
        new_verts = []
                
        for pt in self.verts:
            # Shift point based on centroid
            dx = pt.x - centroid.x
            dy = pt.y - centroid.y
                
            x_new = sx * dx + centroid.x
            y_new = sy * dy + centroid.y
                    
            new_verts.append(Point(x_new, y_new))
                    
            # Update and find edges again
            self.verts = new_verts
            self.nverts = len(self.verts)
    
            self.edges = []
            for i in range(self.nverts):
                start = self.verts[i]
                end = self.verts[(i + 1) % self.nverts] # We have to do this (i+1)%nverts to make sure the range is correct
                self.edges.append(Vec2D(start, end))


    def is_point_inside(self, pt):
        """
        Determines if a point is inside/on edges of polygon or not

        Parameters
        ----------
        pt : Point class instnace and this is basically just a point to check

        Returns
        -------
        Boolean type and it is basically true if it is on inside or on the edge and false otherwise

        """
        
        """
        Determines if a point is inside or on the boundary of the polygon.

        Args:
            pt (Point): The point to check.

        Returns:
            bool: True if inside or on the edge, False otherwise.
        """
        for i in range(self.nverts):
            a = self.verts[i]
            b = self.verts[(i + 1) % self.nverts]
            side = orient2d(a, b, pt)
            if side == -1:
                return False  # If on right then outside and False
        return True  # Here it basically is inside or on edges so True

    def contains_polygon(self, other):
        """
        This method basically checks if this polygon fully contains another polygon

        Parameters
        ----------
        other : This is of type Polygon and is essentially the other Polygon

        Returns
        -------
        bool
            True if all vertices of the other Polygon are inside the self Polygon

        """
        
        for pt in other.verts:
            if not self.is_point_inside(pt):
                return False
        return True

    def is_polygon_convex(self):
        """
        This basically just validates if the polygon is convex.
        Uses orientation tests. 

        Returns
        -------
        True if convex and false otherwise
        
        """
        
        if self.nverts < 3:
            return False

        sign = None
        for i in range(self.nverts):
            A = self.verts[i]
            B = self.verts[(i + 1) % self.nverts]
            C = self.verts[(i + 2) % self.nverts]

            turn = orient2d(A, B, C)

            if turn == 0:
                continue  # Collinear points are okay
            if sign is None:
                sign = turn  # First non-zero orientation
            elif sign != turn:
                return False  # Inconsistent orientation → not convex

        return True


    '''

    # Uncomment these lines if you'd like to run game.py
    
    @staticmethod
    def get_projections_minmax (ortho, obj_1, obj_2):

        # Edit from this line
        projections_obj_1 = [ortho * vert for vert in obj_1.verts]
        projections_obj_2 = [ortho * vert for vert in obj_2.verts]
        
        min_obj_1, max_obj_1 = min(projections_obj_1), max(projections_obj_1)
        min_obj_2, max_obj_2 = min(projections_obj_2), max(projections_obj_2)
        
        return min_obj_1, max_obj_1, min_obj_2, max_obj_2 
        
    

    def __and__(self, other):
        
        #Uses separating axes theorem to check for overlaps

        all_edges = self.edges + other.edges
        
        for edge in all_edges:

            ortho = edge.normal_ccw()
            
            min_self, max_self, min_other, max_other = self.get_projections_minmax(ortho, self, other) 
            
            # Check for overlaps in projection
            if min_self > max_other or max_self < min_other:
                
                # Gap found in projections and therefore Overlap cannot occur
                return False
            
        return True
    

    
    '''
    
    
   
if __name__=='__main__':
    
    # Tester Code

    # Creating the polygon object shown in figure 1
    a = ConvexPolygon([Point(1,0), Point(0,1), Point(-1,0), Point(0,-1)])

    print(a)
    
    a = ConvexPolygon([Point(1,0), Point(0,1), Point(-1,0), Point(0,-1)])

    print("Centroid: ", a.get_centroid())
    
    
    a = ConvexPolygon([Point(1,0), Point(1,1), Point(0,1), Point(0,0)])

    print("Perimeter: ", a.get_perimeter())
    
    a = ConvexPolygon([Point(1,0), Point(0,1), Point(-1,0), Point(0,-1)])

    print("Before translation\n")
    print(a)

    a.translate(Vec2D(3,0))

    print("\nAfter translation\n")
    print(a)
    
    a = ConvexPolygon([Point(1,0), Point(0,1), Point(-1,0), Point(0,-1)])

    print("Before rotation\n")
    print(a)

    print("\nAfter rotation\n")
    a.rotate(math.pi/4.0)
    print(a)
    
    a = ConvexPolygon([Point(1,0), Point(0,1), Point(-1,0), Point(0,-1)])
    
    print("Before scaling\n")
    print(a)

    print("\nAfter scaling\n")
    a.scale(2,2)
    print(a)
    
    a = ConvexPolygon([Point(1,0), Point(0,1), Point(-1,0), Point(0,-1)])

    # See figure 7
    print(a.is_point_inside(Point(0,0)))
    print(a.is_point_inside(Point(1,1)))
    
    a = ConvexPolygon([Point(1,0), Point(0,1), Point(-1,0), Point(0,-1)])
    b = ConvexPolygon([Point(0,0), Point(1/2,1/2), Point(0,1/2)])

    #See figure 8
    print(a.contains_polygon(b))

    #See figure 8
    c = ConvexPolygon([Point(-1,0.5), Point(-1/2,-1/2), Point(-1,-1)])
    print(a.contains_polygon(c))

    d = ConvexPolygon([Point(0,0), Point(1/2,1/2), Point(0,1/2)])
    d.scale(10,10)
    print(a.contains_polygon(d))

    # Creating the polygon object shown in figure 6
    a = ConvexPolygon([Point(1,0), Point(0,1), Point(1,1), Point(0,0)])
    print("Is it convex ", a.is_polygon_convex())

    # Creating the polygon object shown in figure 6
    a = ConvexPolygon([Point(1,0), Point(1/2,1/2), Point(1,1), Point(0,1), Point(0,0)])
    print("Is it convex ", a.is_polygon_convex())

    # Only two points provided
    a = ConvexPolygon([Point(1,0), Point(0,1)])
    print("Is it convex ", a.is_polygon_convex())

    # A square convex polygon
    a = ConvexPolygon([Point(1,0), Point(1,1), Point(0,1), Point(0,0)])
    print("Is it convex ", a.is_polygon_convex())
    
    # Ran game.py, it works fine