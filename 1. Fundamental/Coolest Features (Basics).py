

# Dynamic Typing

movie = "Interstellar"  # string
rating = 9              # number
watched = False         # boolean

print(type(rating))     # prints int

rating = "poor"         # reassigned a new string data
print(type(rating))     # prints str


# Arbitrary integer size

largeNumber = 100000000000000000000000000000000
smallNumber = 100
negativeNum = -50000
floatNum = 3.142


# Swapping two variables

a = 5
b = 6

a, b = b, a

print(a, b)     # prints 6 and 5


# Reformed ternary operator

movieCollection = 100

status = "flop" if movieCollection < 100 else "hit"

print(status)       # Prints 'hit'


# Return multiple variables from a function

def getExtremes(array):

    minValue = min(array)
    maxValue = max(array)

    return minValue, maxValue

array = [1, 2, 3, 4, 5]

lowest, highest = getExtremes(array)

print(lowest, highest)      # prints 1 5


# Negative index

array = [5, 8, 2, 4]

print(array[-1])        # prints 4
print(array[-2])        # prints 2


# Risk-free String formatting

statement = "Bro, you have to watch {movie}. " \
            "It has IMDB rating of {rating}. " \
            "And it is {director}'s one of the finest."\
                .format(movie="Inception", rating=9.3,
                        director="Nolan")


print(statement)


# Else after loops

marks = [60, 80, 90, 30, 55]

for mark in marks:
    if mark < 40:
        break
else:
    print("You've passed the Sem")


# Array slicing

movies = ["Saw", "Gravity", "Buried", "300", "Gladiator"]

# Sets ["Gravity", "Buried"]
slice1 = movies[1:3]

# Sets ["Saw", "Gravity"]
slice2 = movies[0:2]

# Sets ["Buried", "300", "Gladiator"]
slice3 = movies[2:]

# Sets ["Saw", "Gravity", "Buried", "300"]
slice4 = movies[:4]

# Sets ["Saw", "Gravity", "Buried", "300", "Gladiator"]
slice5 = movies[:]



# Variable hiding

for i in range(5):
    print("Hello World!")

for _ in range(5):
    print("Hello World!")


