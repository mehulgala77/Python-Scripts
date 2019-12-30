
board = [
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1]
]

directions = [(2, -1), (2, 1), (-2, 1), (-2, -1),
              (-1, 2), (1, 2), (-1, -2), (1, -2)]


def startGame(bo):
    startNode = (0, 0)
    bo[startNode[0]][startNode[1]] = 0
    solve(startNode, 0, bo)


def solve(currPos, moveCount, bo):

    # Recursion Base case
    if isBoardSolved(bo) is True:
        return True

    # Try solution in every direction
    for item in directions:

        nextRow = currPos[0] + item[0]
        nextCol = currPos[1] + item[1]

        if isValidMove((nextRow, nextCol), bo):

            bo[nextRow][nextCol] = moveCount + 1

            if solve((nextRow, nextCol), moveCount + 1, bo) is True:
                return True

            # Backtrack the change
            bo[nextRow][nextCol] = -1

    else:

        return False


def isValidMove(pos, bo):

    if pos[0] >= 0 and pos[0] < len(bo):
        if pos[1] >= 0 and pos[1] < len(bo[0]):
            if bo[pos[0]][pos[1]] == -1:
                return True

    return False


def getNextMove(currPos, bo):

    for item in directions:

        nextRow = currPos[0] + item[0]
        nextCol = currPos[1] + item[1]

        if nextRow >= 0 and nextRow < len(bo):
            if nextCol >= 0 and nextCol < len(bo[0]):
                if bo[nextRow][nextCol] == -1:
                    return (nextRow, nextCol)

    else:

        return None


def isBoardSolved(bo):

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == -1:
                return False

    return True


def printBoard(bo):

    for i in range(len(bo)):

        if i == (len(bo) // 2):
            print("--------------------")

        for j in range(len(bo[0])):

            if j == (len(bo[0]) // 2):
                print("|", end=" ")

            print(bo[i][j], end=" ")

        print("")


# Driver Code
printBoard(board)
startGame(board)
print("")
printBoard(board)