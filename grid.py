import cell

import random

class grid:
    def __init__(self,size_x:int,size_y:int) -> None:
        self.size_x = size_x
        self.size_y = size_y

        self.grid = [self.size_x][self.size_y]

        for i,j in self.grid: 
            self.grid[i][j] = cell.cell(random.randrange(0,100))

    def tick_temp(self,delta_time:float) -> None:
        for i,j in self.grid:
            self.grid[i,j].calc_deltatemp(delta_time,self.grid,i,j)
        
        for i,j in self.grid:
            self.grid[i,j].apply_deltatemp()