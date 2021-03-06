# Programming Exercise 3-5
#
# Program to convert a value in kilograms to Newtons, then check whether it is in range.
# This program will prompt a user for a mass in kilograms,
# convert it to Newtons and use constants to check if the weight is within range,
# then display the weight and a range message.



# Global constants for minimum, maximum and mass multiplier values


# Variables for weight and mass initialized as floats   


# Get mass from user and convert it to a float


# Calculate weight using the mass multiplier constant


# Display the weight

# If weight > maximum or < than minimum display an appropriate message

kg = input("Input amount of kilograms: ")
kg = float(kg)

MaxN = float(1000.0)
MinN = float(0.0)

convN = float(9.1)

New = float(kg * convN)

if MinN <= New <= MaxN:
    print("Weight is in range.")
else:
    print("Weight is not in range")
print(New)







