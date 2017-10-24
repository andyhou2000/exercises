# Programming Exercise 4-2
#
# Program to output table of calories burned for different times.
# This program takes no input.
# It uses a constant for calories burned per minute to calculate the calories burned for a range of different times,
# then displays a table with the results for each time. 

# Declare a constant for the calories burned per minute.

# Declare variables for calories burned and number of minutes.
# initialize calories burned as a float and minutes as an integer


# print the table header using two tabs between Minutes and Calories Burned
# print a line under the header using underscores


# Use a for loop to calculate and display a display a line for each value of minutes
# set up the loop using a range of comma-separated minutes values 

    # calculate calories burned using the constant for calories burned per minute

    # display the minutes and calories burned using two tabs between the values

calMin = 20
calMin = float(calMin)
time = 0
time = int(time)
calBurn = 0
calBurn = float(calBurn)
x = 10
x = int(x)
print("            Time     Cal")
print("            ____________")
for x in range(0,100):
    time = input(end='')
    time = int(time)
    calBurn = time * calMin
    print("           ", time, "    ",format(calBurn, '.2f'))      
   