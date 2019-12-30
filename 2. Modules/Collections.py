
from collections import Counter

from collections import namedtuple

from collections import OrderedDict

from collections import defaultdict

from collections import deque

buildingHeights = [40, 20, 30, 70, 80, 50, 20, 10]

myQueue = deque()
slider = 3

for i in range(slider):
    myQueue.append(buildingHeights[i])

consecutiveHeight = []
# Moving slider example
for i in range(slider, len(buildingHeights)):
    consecutiveHeight.append((sum(myQueue)))
    myQueue.popleft()
    myQueue.append(buildingHeights[i])

print("Maximun combine height of " + str(slider) +
      " consecutive buildings is: " + str(max(consecutiveHeight)))

# -------------------------------- Default Dict

# Default dictionary constructor takes a default type.
# If passed, int, it will return 0 when a key does not exist.

myScoreBoard = defaultdict(int)

myScoreBoard["Rohit"] = 79
myScoreBoard["Dhawan"] = 56
myScoreBoard["Kohli"] = 141

# Prints 141
print(myScoreBoard["Kohli"])

# Prints default value "0"
print(myScoreBoard["Dhoni"])


# -------------------------------- Ordered Dict

myScoreBoard = OrderedDict()

myScoreBoard["Rohit"] = 79
myScoreBoard["Dhawan"] = 56
myScoreBoard["Kohli"] = 141
myScoreBoard["Rahul"] = 33
myScoreBoard["Pant"] = 6
myScoreBoard["Jadeja"] = 52

# Prints in the order in which they were inserted.
# Normal, dictionary will print it randomly.
print(myScoreBoard)


# -------------------------------- Named Tuple example

Rect = namedtuple("Rect", "top, left, bottom, right")
# myPosition is now a namedTuple.
myPosition = Rect(30, 100, 70, 200)

# We can access it's values using names instead of indexes
print("My height : ", myPosition.bottom - myPosition.top)
print("My width : ", myPosition.right - myPosition.left)

# -------------------------------- Counter example

# Poker Game Cards
myCards \
    = ["King", "King", "Seven", "Jack",
       "Two", "Jack", "Jack"]

myColor \
    = ["Club", "Heart", "Spade", "Heart",
       "Diamond", "Club", "Space"]

myCounter = Counter(myCards)

# Prints: {'Jack': 3, 'King': 2, 'Seven': 1, 'Two': 1})
print(myCounter)

topTwo = myCounter.most_common(2)
# Prints: [('Jack', 3), ('King', 2)]
print(topTwo)

if topTwo[0][1] == 4:
    print("Four of a kind.")
elif topTwo[0][1] == 3 and topTwo[1][1] == 2:
    print("Full house.")
elif topTwo[0][1] == 2 and topTwo[1][1] == 2:
    print("Two pairs.")

