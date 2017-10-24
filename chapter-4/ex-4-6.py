# Programming Exercise 4-6
#
# Program to display a table of Celsius and Fahrenheit equivalents.
# This program takes no input.
# It calculates a series of Fahrenheit equivalents for a range of Celsius temperatures
# then displays them in a table.


# Declare a float variable to hold the Fahrenheit temperature.


# Declare a constant to hold the max celsius value


# Display a table header with Celsius and Fahrenheit separated by two tabs.
# Display a line separator made of underscores



# Use a for loop to iterate from 0 through the range of Celsius temperatures


# 	Calculate the Fahrenheit temperature for the current Celsius value

#	Display the current Celsius and Fahrenheit values, separated by two tabs
c = 0
c = float(c)

maxC = 100.0
maxC = int(maxC)

print("            F        C")
print("            ____________")
for c in range(0,maxC):
    f = input()
    f = float(f)
    c = (f - 32) * (5 / 9)
    print("           ", format(f,'.2f'), "    ",format(c, '.2f'))      
   



