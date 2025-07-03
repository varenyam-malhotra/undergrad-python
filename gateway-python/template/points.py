class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotate(self, px, py):
        """
        Rotate the point 90 degrees clockwise around pivot point (px, py).
        """
        new_x = py - (self.y - py)
        new_y = px + (self.x - px)
        return Point(new_x, new_y)
      
    
    def __add__(self, other):
        # Called when using + between two Points
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented
        # NotImplemented as error message
    
    def __sub__(self, other):
        # Called when using - between two Points
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        return NotImplemented
        # NotImplemented as error message
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        '''
        Returns user friendly string

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        return 'x: ' + str(round(self.x,4)) + ' y: ' + str(round(self.y,4))

    def __str__(self):
        '''
        Returns user friendly string

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        return 'x: ' + str(round(self.x,4)) + ' y: ' + str(round(self.y,4))

    
 
 
