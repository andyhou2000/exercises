# Programming Exercise 5-4
#
# Program to compute monthly and annual auto expenses.
# This program prompts a user for several auto monthly expense amounts,
# then passes them to a function to total the values, annualize them,
# and display the details and totals on the screen.



# define the main function

    # Define local float variables for loan, insurance, gas, oil, tires and maintenance


    # Get the amount of the monthly loan payment from the user.


    # Get the amount of the monthly insurance from the user.


    # Get the amount of the monthly gas from the user.


    # Get the amount of the monthly oil from the user.


    # Get the amount for monthly tire wear from the users.


    # Get the amount for monthly maintenance from the user.

        
    # Call the function to summarize car expenses,
    # passing the loan, insurance, gas, oil, tires and maintenance as arguments.



# Define a function to summarize car expenses,
# it accepts loan, insurance, gas, oil, tires, and maintenance as arguments,
# calculates a monthly total and an annual total,
# and displays these totals.

    # Define local float variables for monthly total and annual total

    # calculate the monthly total
    
    # calculate the annual total


    # Print monthly and annual information, formatting float value to 2 decimal places.



# Call the main function to start the program

def main():
    loan = input("Input monthly loan payment: $")
    loan = float(loan)
    
    insurance = input("Input monthly insurance payment: $")
    insurance = float(insurance)
    
    gas = input("Input monthly gas spending: $")
    gas = float(gas)
    
    oil = input("Input monthly oil change payment: $")
    oil = float(oil)
    
    tire = input("Input price of monthly tire maintenence: $")
    tire = float(tire)
    
    maint = input("Input price of monthly maintenence on car: $")
    maint = float(maint)
    
    total(loan, insurance, gas, oil, tire, maint)

def total(loan, insurance, gas, oil, tire, maint):
    monthlytotal = loan + insurance + gas + oil + tire + maint
    monthlytotal = float(monthlytotal)
    yearlytotal = monthlytotal * 12
    yearlytotal = float(yearlytotal)
    print("Monthly cost of the car: $", format(monthlytotal, '.2f'))
    print("Yearly cost of the car: $", format(yearlytotal, '.2f'))
    
main()
