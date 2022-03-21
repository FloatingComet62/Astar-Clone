import grid

GRID = grid.grid([
    [" ", " ", " ", " ", "X", "D", " ", "X"],
    ["P", "X", "X", " ", "X", "X", " ", "X"],
    [" ", "X", "X", " ", " ", " ", " ", " "],
    [" ", " ", " ", "X", " ", " ", "X", " "],
    ["X", "X", " ", " ", " ", "X", "X", " "]
], False)

GRID.genPath()

print(GRID.path)