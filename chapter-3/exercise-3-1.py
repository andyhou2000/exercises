# Programming Exercise 3-1
#
# Program to display the name of a week day from its number.
# This program prompts a user for the number (1 to 7)
# and uses it to choose the name of a weekday
# to display on the screen.

# Variables to hold the day of the week and the name of the day.
# Be sure to initialize the day of the week to an int and the name as a string.


# Get the number for the day of the week.
# be sure to format the input as an int


# Determine the value to assign to the day of the week.
# use a set of if ... elif ... etc. statements to test the day of the week value.







# use the final else to display an error message if the number is out of range.


# display the name of the day on the screen.


    
day = input("Input the day of the week as an interger: ")
day = int(day)

dayStr = str
    
if day == 1:
    dayStr = "Monday"
    print(dayStr)
elif day == 2:
    dayStr = "Tuesday"
    print(dayStr)
elif day == 3:
    dayStr = "Wednesday"
    print(dayStr)
elif day == 4:
    dayStr = "Thursday"
    print(dayStr)
elif day == 5:
    dayStr = "Friday"
    print(dayStr)
elif day == 6:
    dayStr = "Saturday"
    print(dayStr)
elif day == 7:
    dayStr = "Friday"
    print(dayStr)
else:
    print("Stop being a dumdum.")
