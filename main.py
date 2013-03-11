from graphics import *

class Application:
    """The Application"""
    application_name = "Hog Wild!"
    window_size = 300

    def __init__(self):
        self.win = GraphWin(self.application_name,self.window_size,self.window_size) 
    def run(self):
        self.the_grid = TheGrid(2,self.win)
        self.the_grid.draw()

        while not self.win.closed:
            self.the_grid.update()
            self.win.update()

class LifeCell:
    """The Fundamental Unit"""
    state = 'red'
    def __init__(self,location,size,window):
        self.size = size
        self.location = location
        self.window = window

    def draw(self):        
        rectangle_end_x = self.location.x + self.size
        rectangle_end_y = self.location.y + self.size
        rectangle_end = Point(rectangle_end_x,rectangle_end_y) 

        self.r = Rectangle(self.location,rectangle_end)
        self.r.setFill(self.state) 
        self.r.draw(self.window)

    def update(self):
        self.r.setFill(self.state)

class TheGrid:
    """The Game Grid"""

    def __init__(self,grid_size,window):
        self.grid_size = grid_size
        self.the_grid = [[None]*grid_size]*grid_size
        self.window = window

    def draw(self):
        offset_x = 0
        offset_y = 0

        for x in range(len(self.the_grid)):
            for y in range(len(self.the_grid[x])): 
                self.the_grid[y][x] = LifeCell(Point(offset_x, offset_y),20,self.window)
                self.the_grid[y][x].draw()
                offset_x += 21
            offset_y +=21
            offset_x = 0
        
    def update(self):
        for x in range(len(self.the_grid)):
            for y in range(len(self.the_grid[x])): 
                self.the_grid[y][x].state = 'blue'
                self.the_grid[y][x].update()

a = Application()
a.run()


