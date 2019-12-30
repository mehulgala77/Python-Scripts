# Universal in operator

myList = ["The Dark Knight", "Godfather", "The matrix"]
myTuple = ("Forrest Gump", "The Lord of the Rings", "Momento")
mySet = {"Edge of Tomorrow", "Source Code", "The Dark Knight"}
myDictionary = {"The Pursuit of Happyness" : "Will Smith",
          "The wolf of wall street": "Leonardo Di Caprio",
          "Captain Phillips": "Tom Hanks"}

myMovie = "The Dark Knight"

if myMovie in myList:               # true
    print("Found in the list")

if myMovie in myTuple:              # false
    print("Found in the tuple")

if myMovie in mySet:                # true
    print("Found in the set")

if myMovie in myDictionary:         # false
    print("Found in the dictionary")


# List comprehensions

# Compute squares of the numbers in the list,
# and create a new list
newList = [x*x for x in range(7)]
# Prints a new list: [0, 1, 4, 9, 16, 25, 36]
print(newList)

# We can filter the values while creating new list
# Only squares of even numbers will be printed.
newList = [x*x for x in range(7) if x % 2 == 0]
# [0, 4, 16, 36]
print(newList)

# We can create a new list from existing lists
listOfWords = ["ThIs", "iS", "a", "LIST", "of", "WorDs"]
newList = [word.lower() for word in listOfWords]
# ['this', 'is', 'a', 'list', 'of', 'words']
print(newList)


# Enumerate function

myList = ["The Prestige", "Now you see me", "The Illusionist"]

print("My favorite magic related movies are:")
for index, item in enumerate(myList):
    print("Rank {0}: {1}".format(index, item))

# Prints following
'''
My favorite magic related movies are:
Rank 0: The Prestige
Rank 1: Now you see me
Rank 2: The Illusionist
'''


# Zip function

# Traverse multiple lists in parallel
movies = ["The road trip", "Mr popper's penguins",
          "We bought a Zoo"]
ratings = [6.5, 7, 7.2]

for movie, rating in zip(movies, ratings):
    print('"{0}", Rating: {1}'.format(movie, rating))

# prints following
'''
"The road trip", Rating: 6.5
"Mr popper's penguins", Rating: 7
"We bought a Zoo", Rating: 7.2
'''

# Sorting using two lists parallelly the Zip function
movies = ["The road trip", "Mr popper's penguins",
          "We bought a Zoo"]
ratings = [6.5, 7, 7.2]

for rating, movie in sorted(zip(ratings, movies),
                            reverse=True):
    print('"{0}", Rating: {1}'.format(movie, rating))

# prints following
'''
"We bought a Zoo", Rating: 7.2
"Mr popper's penguins", Rating: 7
"The road trip", Rating: 6.5
'''


# Keyword arguments

name = "Will"
surname = "Smith"


def printName(firstname, lastname):
    print("The person's name is {0} {1}"
            .format(firstname, lastname))


# prints "The person's name is Will Smith"
printName(firstname=name, lastname=surname)

# Also prints "The person's name is Will Smith"
printName(lastname=surname, firstname=name)


# Packing

first_name = "Jack"
last_name = "Sparrow"
rank = "Captain of the Black Pearl"
place = "Tortuga"


def pirateRecords(*args):

    for item in args:
        print(item)


pirateRecords(first_name, last_name, rank, place)



# Unpacking


coordinates = [3, 5, -1, 6]


def recordLocation(top, left, bottom, right):
    print(top, left, bottom, right)


# This converts the list into four separate variables that
# the function expects.
recordLocation(*coordinates)


def getCurrentTime():
    time = [10, 30, 56]
    return time


hours, mins, secs = getCurrentTime()
print(hours, mins, secs)


# Create a dictionary from two lists
movies = ["The road trip", "Mr popper's penguins",
          "We bought a Zoo"]
ratings = [6.5, 7, 7.2]

myDictionary = {movie: rating
                for movie, rating
                in zip(movies, ratings)}

# {'The road trip': 6.5, "Mr popper's penguins": 7,
# 'We bought a Zoo': 7.2}
print(myDictionary)


# Operator Chaining

a = 10
b = 20
c = 30

if a < b < c:
    print("Order is forward")

# Other languages needs a logical operator
# a < b && b < c


