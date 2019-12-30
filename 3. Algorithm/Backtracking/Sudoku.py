
board = [
    [0, 0, 0, 0, 9, 7, 0, 0, 8],
    [0, 3, 0, 6, 0, 8, 4, 9, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 7, 0],
    [8, 9, 0, 0, 7, 0, 0, 6, 3],
    [0, 0, 2, 3, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 3, 0],
    [2, 0, 0, 0, 1, 0, 8, 0, 0],
    [0, 8, 0, 0, 6, 0, 0, 0, 0]
]


def solve(bo):

    # Grab an empty spot
    spot = getEmptySpot(bo)

    # Recursion base case
    if spot is None:
        return True

    # Try putting numbers 1 to 9 in the empty slot
    for num in range(1, 10):

        bo[spot[0]][spot[1]] = num

        # After every attempt, see if the board is valid
        if isValid(bo, num, spot):

            # If valid, call solve recursively to
            if solve(bo):
                return True

        # If the solve returns false, meaning there is no solution,
        # backtrack, revert the change we made, and try with a new number.
        bo[spot[0]][spot[1]] = 0

    return False


# Check Validity of the Board
def isValid(bo, num, pos):

    # Check Row
    for i in range(len(bo[0])):
        if num == bo[pos[0]][i] and i != pos[1]:
            return False

    # Check Col
    for i in range(len(bo)):
        if num == bo[i][pos[1]] and i != pos[0]:
            return False

    # Check 3*3 grid
    grid_row_index = pos[0] // 3
    grid_col_index = pos[1] // 3

    for i in range(3):
        for j in range(3):

            currRow = grid_row_index * 3 + i
            currCol = grid_col_index * 3 + j
            currVal = bo[currRow][currCol]

            if num == currVal and pos != (currRow, currCol):
                return False

    return True


# Find Empty Spot
def getEmptySpot(bo):

    for i in range(len(bo)):
        for j in range(len(bo[0])):

            if bo[i][j] == 0:
                return (i, j)   # (row, col)

    return None


# For visual presentation of the board
def printBoard(bo):

    print()
    for i in range(len(bo)):

        if i % 3 == 0 and i != 0:
            print("-------------------------")

        for j in range(len(bo[i])):

            if j % 3 == 0 and j != 0:
                print(" | ", end=" ")

            print(bo[i][j], end=" ")

        print("")


# Driver code
solve(board)
printBoard(board)