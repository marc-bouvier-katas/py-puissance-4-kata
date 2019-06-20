class game:
    grid=None

    def __init__(self):
        self.grid = "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
        
    def ascii(self):
        return "\n".join(self.__grid_to_list())

    def play(self,player,column):
        # try to place it at the deepest position into the column
        # If there is already a token, place it the row above
        # If there is a token in the tallest row this is a wrong move
        #index = self.__get_available_index(column)
        grid_list = self.__grid_to_list()
        row = grid_list[5]
        row = row[:(column-1)] + player + row[(column):]
        print('row : '+row)
        grid_list[5] = row
        self.grid = "".join(grid_list)
        return self

    def __get_available_index(self,column):
        grid_list = self.__grid_to_list()
        #grid_list[6][column-1] = 
        
    def __grid_to_list(self):
        n = 7
        return [self.grid[i:i+n] for i in range(0, len(self.grid), n)]
