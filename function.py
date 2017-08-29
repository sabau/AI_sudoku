from utils import *


def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    alldigits = '123456789'
    sudoku = dict(zip(boxes, grid))
    for k in sudoku:
        if sudoku[k] == '.':
            sudoku[k] = alldigits
    return sudoku


def eliminatee(values):
    for b in values.keys():
        if len(values[b]) == 1:
            for p in peers[b]:
                values[p] = values[p].replace(values[b], '')
    return values


def eliminate(values):
    # I would like to put boxes here, in place of values.keys()
    # but the different order in which they are checked change the result
    for b in boxes:
        if len(values[b]) == 1:
            for p in peers[b]:
                values[p] = values[p].replace(values[b], '')
    return values

gf = grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
gf2 = grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
gf2 = eliminatee(eliminatee(eliminatee(gf2)))
gf = eliminate(eliminate(eliminate(gf)))
print (gf)
print (gf2)

print gf2 == gf