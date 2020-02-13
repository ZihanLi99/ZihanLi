# Author: Zihan Li
# Date: 2020/2/12
# Description: a puzzle consisting of a row of squares that contain non-negative integers,
#              with a zero in the rightmost square

def row_puzzle(row):
    # call recursive function
    return row_puzzle_rec(row, 0, set())

def row_puzzle_rec(row, i, visited):
    if i < 0:
        # out of range
        return False
    if i >= len(row):
        # out of range
        return False
    if i == len(row) - 1:
        # reach last column
        return True

    steps = row[i]
    visited.add(i)
    # mark as visited

    if (i - steps) not in visited:
        if row_puzzle_rec(row, i - steps, visited):
            # try an unvisited column (left)
            return True

    if (i + steps) not in visited:
        if row_puzzle_rec(row, i + steps, visited):
            # try an unvisited column (right)
            return True
    return False
    # neither direction has solution, return False
