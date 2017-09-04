from sudoku.utils import *


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


def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """

    # I would like to put boxes here, in place of values.keys()
    # but the different order in which they are checked change the result
    for b in boxes:
        if len(values[b]) == 1:
            for p in peers[b]:
                values[p] = values[p].replace(values[b], '')
    return values


def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    for unit in unitlist:
        for d in '123456789':
            # array of boxes for the digit d
            destinations = [b for b in unit if d in values[b]]
            if len(destinations) == 1:
                values[destinations[0]] = d
    return values


def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        values = only_choice(eliminate(values))

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def naked_twins(values):

    return values


def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values == False:
        return False

    if len([box for box in values.keys() if len(values[box]) == 1]) == 81:
        return values
    # Choose one of the unfilled squares with the fewest possibilities
    min = 10
    minKey = None
    for v in values:
        if 1 < len(values[v]) < min:
            min = len(values[v])
            minKey = v

    for digit in values[minKey]:
        new_values = dict(values)
        new_values[minKey] = digit
        new_values = search(new_values)
        if new_values != False:
            return new_values
    return False


# Easy Sudoku
# grid1 = grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
# grid1 = (reduce_puzzle(grid1))
# print grid1

# Harder Sudoku
grid2 = grid_values('4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......')
grid2 = (search(grid2))
print(grid2)