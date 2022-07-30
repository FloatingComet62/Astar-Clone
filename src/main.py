import grid

GRID = grid.Grid([
    [" ", " ", " ", " ", "X", "D", " ", "X"],
    ["P", "X", "X", " ", "X", "X", " ", "X"],
    [" ", "X", "X", " ", " ", " ", " ", " "],
    [" ", " ", " ", "X", " ", " ", "X", " "],
    ["X", "X", " ", " ", " ", "X", "X", " "]
], False)
directions = GRID.genPath()
GRID.reset(True, 0.1)
GRID.followDirections(directions)
