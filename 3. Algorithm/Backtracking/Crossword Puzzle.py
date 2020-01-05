
grid = [
    ["+", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
    ["+", "-", "-", "-", "-", "-", "-", "+", "+", "+"],
    ["+", "+", "+", "-", "+", "+", "+", "+", "+", "+"],
    ["+", "+", "+", "-", "+", "+", "+", "+", "+", "+"],
    ["+", "+", "+", "-", "-", "-", "-", "-", "+", "+"],
    ["+", "+", "+", "-", "+", "+", "-", "+", "+", "+"],
    ["+", "+", "+", "+", "+", "+", "-", "+", "+", "+"],
    ["+", "+", "+", "+", "+", "+", "-", "+", "+", "+"],
    ["+", "+", "+", "+", "+", "+", "-", "+", "+", "+"],
    ["+", "+", "+", "+", "+", "+", "+", "+", "+", "+"]
]

words = ("POLAND", "LHASA", "SPAIN", "INDIA")

# Will be used to check if the word is already used
cache = set()

# Only going to check for right and bottom direction,
# The top and left directions should not have empty cells
# Because we must have filled them while coming at this square.
directions = {}
directions['r'] = (0, 1)
directions['b'] = (1, 0)


def solve(bo):

    if isPuzzleSolved():
        return True

    nextVacantPos = getNextPos(bo)
    if nextVacantPos is None:
        return True

    for word in words:

        if word not in cache:

            ret, dir = fitWord(bo, nextVacantPos, word)

            if ret:

                cache.add(word)

                if solve(bo):
                    return True

                # Backtrack
                cache.remove(word)
                eraseWord(bo, nextVacantPos, dir, word)


def shouldEraseChar(bo, pos, dir):

    opposites = []

    if dir == "r":

        opposites.append((pos[0] + 1, pos[1]))
        opposites.append((pos[0] - 1, pos[1]))

    else:

        opposites.append((pos[0], pos[1] + 1))
        opposites.append((pos[0], pos[1] - 1))

    for item in opposites:

        if isValidPos(bo, (item[0], item[1])):

            if bo[item[0]][item[1]] not in ["+", "-"]:
                return False

    return True


def eraseWord(bo, pos, dir, word):

    val = directions[dir]

    currRow = pos[0]
    currCol = pos[1]

    for i in range(len(word)):

        if shouldEraseChar(bo, (currRow, currCol), dir):
            bo[currRow][currCol] = "-"

        currRow += val[0]
        currCol += val[1]


# Try to fit the word at the empty location
# Must make sure of existing alphabets in the path
# Must make sure of the same number of blanks as the length of the word
def fitWord(bo, pos, word):

    for key, val in directions.items():

        matched = False
        currPosRow = pos[0]
        currPosCol = pos[1]

        for i in range(len(word)):

            if not isValidPos(bo, (currPosRow, currPosCol)):
                break

            if bo[currPosRow][currPosCol] != "-":
                if bo[currPosRow][currPosCol] != word[i]:
                    break

            currPosRow += val[0]
            currPosCol += val[1]

        else:

            matched = True

            if isValidPos(bo, (currPosRow, currPosCol)):
                if bo[currPosRow][currPosCol] == "-":
                    matched = False

        if matched:

            currPosRow = pos[0]
            currPosCol = pos[1]

            for i in range(len(word)):

                bo[currPosRow][currPosCol] = word[i]

                currPosRow += val[0]
                currPosCol += val[1]

            return True, key

    return False, None


# Return empty or alphabet location
def getNextPos(bo):

    for i in range(len(bo)):
        for j in range(len(bo[0])):

            if bo[i][j] == "+":
                continue

            if bo[i][j] == "-":
                return (i, j)

            for key, val in directions.items():
                if bo[i + val[0]][j + val[1]] == "-":
                    return (i, j)

    return None


def isPuzzleSolved():

    if len(words) == len(cache):
        return True

    return False


def isValidPos(bo, pos):

    if pos[0] > 0 and pos[0] < len(bo):
        if pos[1] > 0 and pos[1] < len(bo[0]):
            return True

    return False


def printBoard(bo):

    for i in range(len(bo)):
        for j in range(len(bo[0])):

            print(bo[i][j], end=" ")

        print("")


# Driver Code
printBoard(grid)

# Solve the puzzle
solve(grid)

print("")
printBoard(grid)