class Connect4():
    
    def __init__(self):
        self.player = 1
        self.grid = list(list([0 for y in range(6)]) for x in range(7))
        self.finished = False

    def play(self, col):
        if self.finished:
            return "Game has finished!"
        if all(x != 0 for x in self.grid[col]):
            return "Column full!"
        self.grid[col][self.grid[col].index(0)] = self.player
        if all(self.grid[col][x] == self.player for x in range(self.grid[col].index(0) - 1 \
                if 0 in self.grid[col] else 5, self.grid[col].index(0) - 5 \
                if 0 in self.grid[col] else 1, -1)):
            self.finished = True
            return "Player {} wins!".format(self.player)
        for i in range(0, 4):
            for j in range(0, 6):
                if all(self.grid[i + y][j] == self.player for y in range(0, 4)):
                    self.finished = True
                    return "Player {} wins!".format(self.player)
        for i in range(0, 4):
            for j in range(0, 3):
                if all(self.grid[i + x][j + x] == self.player for x in range(0, 4)) or \
                    all(self.grid[6 - i - x][j + x] == self.player for x in range(0, 4)):
                    self.finished = True
                    return "Player {} wins!".format(self.player)
        temp = self.player
        self.player = 1 if self.player == 2 else 2
        return "Player {} has a turn".format(temp)