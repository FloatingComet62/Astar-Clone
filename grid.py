import os
import time

class grid:
    def __init__(self, grid, Ui, timeDelay=0.1):
        self.grid = grid
        self.ui = Ui
        self.backUpGrid = grid
        self.row = len(self.grid)
        self.col = len(self.grid[0])
        self.numGrid = [[0 for x in range(self.col)] for y in range(self.row)]
        self.path = []
        self.finding = True
        self.timeDelay = timeDelay

        for x in range(self.row):
            row = self.grid[x]
            for y in range(self.col):
                if row[y] == "X":
                    self.numGrid[x][y] = 9999999
                if row[y] == "D":
                    self.numGrid[x][y] = -1
    
    def printGrid(self):
        output = ""
        for row in self.grid:
            for item in row:
                output += " "+item+" "
            output += "\n"
        print(output)

        return self
    
    def getPlayer(self):
        for x in range(len(self.grid)):
            row = self.grid[x]
            for y in range(len(row)):
                if row[y] == "P":
                    return (x, y)
    
    def getEnd(self):
        for i in range(len(self.grid)):
            row = self.grid[i]
            for j in range(len(row)):
                if row[j] == "D":
                    return (i, j)
    
    def setCell(self, coords, identifier):
        (x, y) = coords
        self.grid[x][y] = identifier   
    
    def callback(self, end=False):
        if self.ui:
            os.system('cls')
            self.printGrid()
            time.sleep(self.timeDelay)
        
        if end:
            self.finding = False
        pass
    
    def poop(self, coords):
        (x, y) = coords
        self.numGrid[x][y] += 1

        return self.numGrid[x][y]





    def up(self):
        (y, x) = self.getPlayer()

        if y == 0:
            self.callback()
            return self
        if self.grid[y-1][x] == "X":
            self.callback()
            return self
        if self.grid[y-1][x] == "D":
            self.setCell((y-1, x), "P")
            self.poop((y, x))
            self.setCell((y, x), " ")
            self.callback(True)
        
        self.setCell((y-1, x), "P")
        self.poop((y, x))
        self.setCell((y, x), " ")
        self.callback()

        return self
    
    def down(self):
        (y, x) = self.getPlayer()

        if y == self.row:
            self.callback()
            return self
        if self.grid[y+1][x] == "X":
            self.callback()
            return self
        if self.grid[y+1][x] == "D":
            self.setCell((y+1, x), "P")
            self.poop((y, x))
            self.setCell((y, x), " ")
            self.callback(True)
        
        self.setCell((y+1, x), "P")
        self.poop((y, x))
        self.setCell((y, x), " ")
        self.callback()

        return self

    def right(self):
        (y, x) = self.getPlayer()

        if x == self.col:
            self.callback()
            return self
        if self.grid[y][x+1] == "X":
            self.callback()
            return self
        if self.grid[y][x+1] == "D":
            self.setCell((y, x+1), "P")
            self.poop((y, x))
            self.setCell((y, x), " ")
            self.callback(True)
        
        self.setCell((y, x+1), "P")
        self.poop((y, x))
        self.setCell((y, x), " ")
        self.callback()

        return self

    def left(self):
        (y, x) = self.getPlayer()

        if x == 0:
            self.callback()
            return self
        if self.grid[y][x-1] == "X":
            self.callback()
            return self
        if self.grid[y][x-1] == "D":
            self.setCell((y, x-1), "P")
            self.poop((y, x))
            self.setCell((y, x), " ")
            self.callback(True)
        
        self.setCell((y, x-1), "P")
        self.poop((y, x))
        self.setCell((y, x), " ")
        self.callback()

        return self





    def changetoInt(self, num):
        output = 0
        try:
            output = int(num)
        except:
            output = 9999999
        
        return output

    def genPath(self):
        while self.finding:
            (y, x) = self.getPlayer()
            up = 9999999
            down = 9999999
            right = 999999
            left = 9999999
            if not y == 0:
                up = self.numGrid[y-1][x]
            if not y == self.row-1:
                down = self.numGrid[y+1][x]
            if not x == self.col-1:
                right = self.numGrid[y][x+1]
            if not x == 0:
                left = self.numGrid[y][x-1]

            up = self.changetoInt(up)
            down = self.changetoInt(down)
            right = self.changetoInt(right)
            left = self.changetoInt(left)

            sortedList = [up, down, right, left]
            sortedList.sort()
            if sortedList[0] == up:
                self.up()
                self.path.append("up")
            elif sortedList[0] == down:
                self.down()
                self.path.append("down")
            elif sortedList[0] == right:
                self.right()
                self.path.append("right")
            elif sortedList[0] == left:
                self.left()
                self.path.append("left")
    
    def reset(self):
        self.grid = self.backUpGrid
        self.row = len(self.grid)
        self.col = len(self.grid[0])
        self.numGrid = [[0 for x in range(self.col)] for y in range(self.row)]
        self.path = []