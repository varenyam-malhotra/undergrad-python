import pygame

class Block:
    
    '''
        A class to represent an individual block in the Tetris game grid.

        Attributes:
            x (int): The x-coordinate of the block.
            y (int): The y-coordinate of the block.
            color (tuple): The RGB color of the block.
    '''
        
    def __init__(self, p, color):
        '''
        Initializes a new block.

        Args:
            p (Point): A Point object representing the block's position.
            color (tuple): The RGB color of the block.
        '''
        
        self.x     = p.x
        self.y     = p.y
        self.color = color

    def draw(self, screen, p_size):
        '''
        Draws the block on the game screen.

        Args:
            screen (pygame.Surface): The Pygame surface where the block will be drawn.
            p_size (int): The size of the block in pixels.
        '''
        
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x * p_size, self.y * p_size, p_size, p_size))



class Board:
    '''
    A class to represent the Tetris game board.
    
    Attributes:
        width (int): The width of the game board (in blocks).
        height (int): The height of the game board (in blocks).
        pix_size (int): The pixel size of each block. (Used for visualization purposes)
        grid (list): A 2D list representing the grid of blocks (None for empty cells, Block for filled).
    '''

    def __init__(self, w, h, pixel_size = 30):
        '''
        Initializes the Tetris game board.

        Args:
            w (int): The width of the board in number of blocks.
            h (int): The height of the board in number of blocks.
            pixel_size (int, optional): The size of each block in pixels. Default is 30.
        '''

        self.width    = w
        self.height   = h
        self.pix_size = pixel_size
        self.grid     = [[None for _ in range(self.width)] for _ in range(self.height)]

        
    def check_collision(self, tet):
        '''
        Checks if the active Tetromino has collided with the edges of the board or other placed blocks.

        Args:
            tet (Tetromino): The Tetromino object currently falling.
        
        Returns:
            bool: True if there is a collision, False otherwise.
        '''
        # For every block
        for block in tet.squares:
        # Check for collision with the left and right edges
            if block.x < 0 or block.x >= self.width:
                return True
        # Check for collision with the bottom edge
            if block.y >= self.height:
                return True
        # Check for collision with another block 
            if self.grid[block.y][block.x] is not None:
                return True
        return False
    
    def place_tetromino(self, tet):
        '''
        Places a Tetromino on the game board by adding its blocks to the grid.

        Args:
            tetromino (Tetromino): The Tetromino object to be placed on the board.
        '''

        for s in tet.squares:
            self.grid[s.y][s.x] = Block(s, tet.color)
                                
            
    def clear_rows(self):
        '''
        Clears any rows that are completely filled with blocks and shifts blocks above down by one row.
        '''

        # Find rows that are filled
        new_grid = [row for row in self.grid if any(cell is None for cell in row)]
    
        # Calculate number of rows cleared
        rows_cleared = self.height - len(new_grid)
    
        # Add empty rows at the top
        new_grid = [[None for _ in range(self.width)] for _ in range(rows_cleared)] + new_grid
    
        # Update the game grid
        self.grid = new_grid
        
    def draw(self, screen):
        '''
        Draws the game board and all placed blocks on the screen.

        Args:
            screen (pygame.Surface): The Pygame surface where the game board will be drawn.
        '''

        for row in self.grid:
            for block in row:
                if block:
                    block.draw(screen, self.pix_size)
        

if __name__ == "__main__":
    pass
