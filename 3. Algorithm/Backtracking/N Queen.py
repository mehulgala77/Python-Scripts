
board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

direction = ((1, 1), (-1, -1), (1, -1), (-1, 1))

def start(bo):
    startPos = (0, 0)
    bo[startPos[0]][startPos[1]] = 1
    solve(startPos[0], startPos[1], bo)


def solve(currRow, currCol, bo):

    # Recursion base case
    if isBoardSolved(bo):
        return True

    lastRow = currRow
    lastCol = currCol

    while True:

        pos = getNextPos(lastRow, lastCol, bo)
        if pos == None:
            break

        if isValidMove(pos[0], pos[1], bo):

            bo[pos[0]][pos[1]] = 1

            if solve(pos[0], pos[1], bo):
                return True

            # Backtrack
            bo[pos[0]][pos[1]] = 0

        lastRow = pos[0]
        lastCol = pos[1]

    return False

def isValidPos(currRow, currCol, bo):

    if currRow >= 0 and currRow < len(bo):
        if currCol >= 0 and currCol < len(bo[0]):
            return True

    return False


def isValidMove(currRow, currCol, bo):

    # Checking for another queen in the column
    for i in range(len(bo)):
        if i != currRow and bo[i][currCol] == 1:
            return False

    # Checking for another queen in the row
    for i in range(len(bo[0])):
        if i != currCol and bo[currRow][i] == 1:
            return False

    # Checking for another queen in the diagonal

    for item in direction:

        # Go down the diagonal
        nextRow = currRow + item[0]
        nextCol = currCol + item[1]

        while True:
            if not isValidPos(nextRow, nextCol, bo):
                break

            if bo[nextRow][nextCol] == 1:
                return False

            nextRow += item[0]
            nextCol += item[1]

    return True


def isBoardSolved(bo):

    queenCount = 0
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 1:
                queenCount += 1

    return queenCount == len(bo)


def getNextPos(currRow, currCol, bo):

    if currCol != len(bo[0]) - 1:
        return currRow, currCol + 1

    if currRow != len(bo) - 1:
        return currRow + 1, 0

    return None


def printBoard(bo):

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            print(bo[i][j], end=" ")

        print("")


# Driver Code
# Print the initial board
printBoard(board)

# Start solving the puzzle
start(board)

# Print the solved board
print("")
print("")
printBoard(board)