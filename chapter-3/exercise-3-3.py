# Programming Exercise 3-3
#
# Program to assign an age category to an numerical age.
# This program will prompt the user for an integer age value,
# and use it to choose an age category,
# then display that category on the screen.

# Variables to hold an age and a category.
# initialize age as an int and category as a string.

# Get the person's age.
# remember to convert the input to an int.


# Determine if the person is an infant, child, teenager, or adult and set the category.
# Use a series of if ... elif ... etc. statements.

age = input("Input age of person: ")
age = int(age)

category = "Null"
category = str(category)
if age<3:
    category = "infant"
elif 3<=age<13:
    category = "child"
elif 13<=age<20:
    category = "teenager"
else:
    category = "adult"

print(category)

# display a message with the age category.



