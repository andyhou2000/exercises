# Programming Exercise 5-12
#
# Program to find the greater of two integers.
# This program accepts two integers,
# passes them to a function that compares them,
# and displays which one is greater.



# define the main function

    # Define local variables to hold two integers


    # prompt the user for the first integer
    
    
    # prompt the user for the second integer


    # print the return value from calling a function to find the greater of two integers
    # the two integers are passed as arguments

 
# Define a function to compare integer values.
# This function accepts two integer parameters,
# compares them,
# and returns the value of the greater.

	# if the first integer is greater, return the first integer

	# else, return the second integer



# Call the main function to start the program

def main():
    x = input("Input first number x: ")
    x = int(x)
    y = input("Input second number y: ")
    y = int(y)
    compare(x,y)

def compare(x,y):
    if x > y:
        print("x is greater than y. x =", x)
    elif y > x:
        print("y is greater than x. y =", y)
    else:
        print("Both numbers are the same. x and y =", x)

main()