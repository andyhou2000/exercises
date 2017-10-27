# Programming Exercise 6-6
#
# Program to find the average value of numbers stored in a text file.
# This program takes no user input but requires a file with one number per line,
# which it opens, loops through totaling the values, then averages them,
# and displays the average value on the screen.

# Define the main function

    # Declare local float variables for number and total, and an integer counter

    
    # Open numbers.txt file for reading

    # Iterate over the lines in the file

        # increment the counter

        # get a number from the current line

        # add the number to the total

        
    # Close file


    # Calculate average

    
    # Display the average of the numbers in the file



# Call the main function to start the program

def main():
    number = str("dummy")
    total = float(0)
    counter = int(0)
    file = open("numbers.txt","r")
    while number != "":
        number = file.readline()
        if number == "":
            pass
        else:
            number = float(number)
            total = total + number
            counter = counter + 1
    file.close()
    average = float(total / counter)
    print("Average : ",average)

main()