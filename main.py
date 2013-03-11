from graphics import *

class Application:
    """The Application"""
    application_name = "Hog Wild!"
    window_size = 300

    def __init__(self):
        self.win = GraphWin(self.application_name,self.window_size,self.window_size) 
    def run(self):
        self.the_grid = TheGrid(5,self.win)
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
        self.window = window
        self.the_grid = [[LifeCell(Point(0, 0),20,self.window)]*grid_size]*grid_size

    def draw(self):
        print self.the_grid 
        print self.the_grid[3][3]
        
        for cell_row in self.the_grid:
            for cell in cell_row:
                print cell

        self.the_grid[0][0] = LifeCell(Point(0, 0),20,self.window)
        self.the_grid[0][0].draw()
        
    def update(self):
        self.the_grid[0][0].state = 'blue' 
        self.the_grid[0][0].update()

a = Application()
a.run()


