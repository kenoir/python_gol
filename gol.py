from graphics import *
from random import randint

class Application:
    """The Application"""
    application_name = "Hog Wild!"
    window_size = 300
    cell_size = 30

    def __init__(self):
        self.win = GraphWin(self.application_name,self.window_size,self.window_size) 
    def run(self):
        cells_in_row = self.window_size / self.cell_size
        self.the_grid = TheGrid(self.cell_size,cells_in_row,self.win)
        self.the_grid.draw()

        while not self.win.closed:
            self.the_grid.update()

class LifeCell:
    """The Fundamental Unit"""
    alive = True
    alive_color = 'green'
    dead_color = 'black'
    updating_color = 'red'

    def __init__(self,location,size,window):
        self.size = size
        self.location = location
        self.window = window
        self.alive = bool(randint(0,1))

    def draw(self):        
        rectangle_end_x = self.location.x + self.size
        rectangle_end_y = self.location.y + self.size
        rectangle_end = Point(rectangle_end_x,rectangle_end_y) 

        self.r = Rectangle(self.location,rectangle_end)
        self.update()
        self.r.draw(self.window)

    def update(self):
        self.r.setFill(self.updating_color)
        if self.alive:
            state_color = self.alive_color
        else:
            state_color = self.dead_color
        self.r.setFill(state_color)     
 
class TheGrid:
    """The Game Grid"""

    def __init__(self,cell_size,grid_size,window):
        self.cell_size = cell_size
        self.grid_size = grid_size
        self.the_grid = [[0 for x in xrange(grid_size)] for x in xrange(grid_size)] 
        self.grid_buffer = [[0 for x in xrange(grid_size)] for x in xrange(grid_size)]
        self.window = window

    def draw(self):
        offset_x = 0
        offset_y = 0

        for x in range(len(self.the_grid)):
            for y in range(len(self.the_grid[x])): 
                cell = LifeCell(Point(offset_x, offset_y),self.cell_size,self.window)
                cell.draw()
                self.the_grid[y][x] = cell 

                offset_x += self.cell_size 
            offset_y += self.cell_size
            offset_x = 0
        
    def update(self):
        for x in range(len(self.the_grid)):
            for y in range(len(self.the_grid[x])): 
                left_cell_state = self.the_grid[(y-1)%self.grid_size][x].alive
                right_cell_state = self.the_grid[(y+1)%self.grid_size][x].alive
                self.grid_buffer[y][x] = left_cell_state and right_cell_state

        for x in range(len(self.the_grid)):
            for y in range(len(self.the_grid[x])): 
                self.the_grid[y][x].alive = bool(self.grid_buffer[y][x])

        for x in range(len(self.the_grid)):
            for y in range(len(self.the_grid[x])): 
                self.the_grid[y][x].update()    
