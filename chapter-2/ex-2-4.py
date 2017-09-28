# Programming Exercise 2-4
#
# Program to compute a final price for five items with tax.
# This program will prompt a user for a set of five prices,
# sum them to a subtotal and calculate sales tax with tax rate stored in a constant,
# then display the results on the screen.

# Variables to hold the prices of five items, the subtotal, and the total.
# All should be initialized as floats.


# Constant for the sales tax rate.


# Get the price of each item by prompting the user.
# You will need to convert each input to a float.


# Calculate the subtotal by adding up the item prices.


# Calculate the sales tax by multiplying the subtotal by the tax rate.


# Calculate the total by adding the subtotal and tax.


# Print the values for the subtotal, tax and total.
# Label each value, and format them to display with two decimal places. 

a = input("First item price: ")
a = float(a)

b = input("Second item price: ")
b = float(b)

c = input("Third item price: ")
c = float(c)

d = input("Fourth item price: ")
d = float(d)

e = input ("Fifth item price: ")
e = float(e)

salesTax = 1.0625
salesTax = float(salesTax)

price = salesTax * a + salesTax * b + salesTax * c + salesTax * d + salesTax * e

print("Total price is: $%.2f"%price)