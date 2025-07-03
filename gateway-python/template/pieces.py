from points import Point as P
import utils
import pygame
import math

class Tetromino:
    '''
    A class representing a Tetromino piece in the Tetris game. The Tetromino is defined by its name, vertices,
    color, and current position on the board.

    Attributes:
        name (str):        The name of the Tetromino piece (e.g., 't', 'o', 'l', etc.).
        verts (list):      A list of Point objects representing the vertices of the Tetromino in the current position.
        color (tuple):     The RGB color of the Tetromino.
        orientation (int): The current orientation of the Tetromino (0, 1, 2, or 3).
        squares (list):    A list of Point objects representing the positions of the top left corners of the
                           squares that form the Tetromino.
    '''
    
    def __init__(self, name, verts, color, orientation = 0, dx = 0, dy = 0):
        '''
        Initializes a new instance of the Tetromino class.

        Args:
            name (str): The name of the Tetromino piece (e.g., 't', 'o', 'l', etc.).
            verts (list): A list of Point objects representing the vertices of the Tetromino.
            color (tuple): The RGB color of the Tetromino.
            orientation (int):  Keep track of orientation of the piece, defaults to 0
            dx (int, optional): The x-offset to apply to the vertices. Default is 0.
            dy (int, optional): The y-offset to apply to the vertices. Default is 0.
        '''

        self.name        = name
        self.verts       = [P(v.x + dx, v.y + dy) for v in verts]
        self.color       = color
        self.orientation = orientation
        self.squares     = utils.get_square_positions(self.name, self.verts, self.orientation)

    def __str__(self):
        '''
        Returns a string representation of the Tetromino, showing its vertices.

        Returns:
            str: A string representation of the Tetromino vertices.
        '''

        return "verts " + str(self.verts) + "\ncolor: " + str(self.color) + " orientation: " + str(self.orientation) 
            
    def move(self, dx, dy):
        '''
        Moves the Tetromino by a specified amount in the x and y directions.

        Args:
            dx (int): The distance to move in the x direction.
            dy (int): The distance to move in the y direction.
        '''
        for vertex in self.verts:
            vertex.x += dx
            vertex.y += dy
    
    def get_pivot(self):
        '''
        Returns the pivot point of the Tetromino, which is the point around which the piece will rotate.

        Returns:
            Point: The pivot point of the Tetromino.
        '''
        x_sum = sum(vertex.x for vertex in self.verts)
        y_sum = sum(vertex.y for vertex in self.verts)
        return P(x_sum/len(self.verts), y_sum/len(self.verts))       
    
    def rotate(self):
        """
        Rotates the Tetromino 90 degrees clockwise around its pivot point.
        """
        pivot = self.get_pivot()
        self.verts = [vertex.rotate(pivot.x, pivot.y) for vertex in self.verts]
        # Update orientation
        self.orientation = (self.orientation + 1) % 4

    def copy(self):
        '''
        Get a new copy of the object
        '''
        
        return Tetromino(self.name, [P(v.x, v.y) for v in self.verts], self.color, self.orientation)
        
        
    def draw(self, screen, pix_size = 30):
        '''
        Draws the Tetromino on the provided Pygame screen surface.

        Args:
            screen (pygame.Surface): The Pygame surface on which to draw the Tetromino.
            pix_size (int, optional): The size of each pixel in the game grid. Default is 30.
        '''
        
        get_points = lambda : [(v.x*pix_size, v.y*pix_size) for v in self.verts]
        pygame.draw.polygon(screen, self.color, get_points())


if __name__=='__main__':
    pass
