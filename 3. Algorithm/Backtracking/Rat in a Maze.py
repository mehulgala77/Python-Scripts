
# Rat can move in any 4 direction (left, right, up and down)
# Solved using Backtracking algorithm

board = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1]
]

output = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def startGame(bo, output):

    startPos = (0, 0)
    endPos = (len(bo) - 1, len(bo[0]) - 1)

    output[startPos[0]][startPos[1]] = 1

    solve(startPos, endPos, bo, output)


def solve(pos, endPos, bo, output):

    # TakeAway: Recursion base case
    if pos == endPos:
        return True

    for item in directions:

        nextRow = pos[0] + item[0]
        nextCol = pos[1] + item[1]

        # TakeAway: Avoid visiting valid path cells
        if isValidMove((nextRow, nextCol), bo) \
                and output[nextRow][nextCol] != 1:

            output[nextRow][nextCol] = 1

            if solve((nextRow, nextCol), endPos, bo, output):
                return True

            # TakeAway: Backtrack the move, and try with a new one
            output[nextRow][nextCol] = 0

    return False


def isValidMove(pos, bo):

    row = pos[0]
    col = pos[1]

    if row >= 0 and row < len(bo):
        if col >= 0 and col < len(bo[0]):
            if bo[row][col] != 0:
                return True

    return False


def printBoard(bo):

    for i in range(len(bo)):
        for j in range(len(bo[0])):

            print(bo[i][j], end=" ")

        print("")


# Driver Code

# Board before the game
printBoard(board)

# Starting the game
startGame(board, output)

# The path
print("")
printBoard(output)