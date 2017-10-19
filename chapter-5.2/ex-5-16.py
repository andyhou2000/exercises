# Programming Exercise 5-16
#
# Program to compare the proportion of odd and even random integers.
# This program accepts no input.
# It uses a loop and the random library to generate 100 random integers,
# counts the number of odd and even results,
# and displays the total of each.



# To use the random integer function, import the random library



# define the main function

    # define local int variable for number, odd and even totals


    # define a constant to hold how many numbers to compare (100)


    # loop through the range of numbers to compare

        # get a random integer from the random library function

        # if the check for even function returns true, increment even counter

        # else increment odd counter.

    # display the results on the screen



# Define a function to check for even numbers
# This function accepts one integer parameter,
# uses the mod operater to see if can be evenly divided by two,
# and return true if it can, false it cannot

    # if dividing the number by two yields no remainder, return true

    # else return false



# Call the main function to begin the program

from random import *

def main():
    total = int(0)
    odd = int(0)
    even = int(0)
    count = int(100)
    
    for x in range(0,count):
        y = randint(0,100)
        yesno = even_function(y)
        if yesno == "True":
            total = total + y
            even = even + 1
        else:
            total = total + y
            odd = odd + 1
    
    print("Total:",total)
    print("Number of odds:",odd)
    print("Number of evens:",even)

def even_function(y):
    if y % 2 == 0:
        return "True"
    else:
        return "False"

main()