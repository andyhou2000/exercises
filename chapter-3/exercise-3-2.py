# Programming Exercise 3-2
#
# Program to find which of two rectangles has the greater area.
# This program will get two sets of lengths and widths from a user,
# use them to calculate and compare two area values,
# and display a message comparing those areas

# Local variables
# you need length, width and area for A and for B
# initialize these as floats


# Get length A from the user and convert it to a float


# Get width A from the user and convert it to a float


# Get length B from the user and convert it to a float


# Get width B from the user and convert it to a float


# Calculate area A


# Calculate area B


# Print each area, formatting the values to 2 decimal places

# if area A is greater, print "A is greater" message.

# else if area B is greater, print "B is greater" message.

# else print "A and B are equal" message.

aL = input("Insert length of rectangle A: ")
aL = float(aL)
aW = input("Insert width of rectangle A: ")
aW = float(aW)
bL = input("Insert length of rectangle B: ")
bL = float(bL)
bW = input("Insert width of rectangle B: ")
bW = float(bW)

A = aL * aW
B = bL * bW

if A>B:
    print("A is greater")
elif A<B:
    print("B is greater")
else:
    print("A and B are equal")