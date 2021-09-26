from os import name, system

def clear():
    if name == 'nt':
        _ = system('cls')

answer = "Y"


class grid():
    def __init__(self):
        self.grid = [["O", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"]]
        self.print_grid()
    
    def print_grid(self):
        for row in self.grid:
            print (" ".join(row))

    def change_grid(self, position1, position2):
        self.clear_grid()
        self.grid[position1-1][position2 -1] = "O"
        self.print_grid()
    
    def clear_grid(self):
        self.grid = [["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"]]

grid = grid()


while answer == "Y":
    coords= (input("Where do you want to move to? (Row, column) "))
    while "," not in coords:
        clear()
        grid.print_grid()
        coords= (input("Where do you want to move to? (Row, column) "))


    pos1, pos2 = coords.split(", ")
    pos1, pos2 = int(pos1), int(pos2)
    while (pos1 > 6 or pos1 < 1) or (pos2 > 4 or pos2 < 1):
        clear()
        grid.print_grid()
        coords= (input("Where do you want to move to? (Row, column) "))
        pos1, pos2 = coords.split(", ")
        pos1, pos2 = int(pos1), int(pos2)
    
    print(" ")

    grid.change_grid(int(pos1), int(pos2))
    print(" ")
    answer = str(input("Do you want to move again? 'Y' or 'N'? ")).upper()
    clear()
    grid.print_grid()

clear()


    






