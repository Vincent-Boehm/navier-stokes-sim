import grid

class cell:

    def __init__(self,starting_temp:float) -> None:
        self.temprature = starting_temp
        self.deltatemp = 0
        self.alpha = 1
    def calc_deltatemp(self,delta_time:float,grid:grid.grid,i:int,j:int) -> None:
        try:
            delta_x_1 = grid[i+1,j]
        except:
            delta_x_1 = 0
        
        try:
            delta_x_2 = grid[i-1,j]
        except:
            delta_x_2 = 0

        try:
            delta_y_1 = grid[i,j+1]
        except:
            delta_y_1 = 0

        try:
            delta_y_2 = grid[i,j-1]
        except:
            delta_y_2 = 0

        self.deltatemp = (self.alpha * ( delta_x_1 - delta_x_2 + delta_y_1 - delta_y_2)) * delta_time
    def apply_deltatemp(self) -> None:
        self.temprature += self.deltatemp