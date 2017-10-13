# Programming Exercise 5-3
#
# Program to compute recommended insurance to carry on an item.
# This program accepts a replacement cost from a user,
# calculates a minimum recommended insurance to carry from a global constant,
# then passes these values to a function to be displayed



# Global constant for the percent of replacement cost to insure



# Define the main function

    # Define local float variables for replacement cost and minimum insurance


    # Get the replacement cost from the user

    # Calculate the minimum insurance amount using the global constant

    # Call the function to display the insurance details, 
    # passing the replacement cost and minimum insurance to the function


      
# Define a function to display the insurance details
# This function accepts the replacement cost and minimum insurance as parameters,
# uses the global constant to calculate percent insured,
# and displays the insurance details.

	# display the replacement cost, formatting the value to 2 decimal places

    # display the percent insured, formatting the value to 2 decimal places

	# display the minimum insurance, formatting the value to 2 decimal places



# Call the main function to start the program

min_ins_percent = .8
min_ins_percent = float(min_ins_percent)

def main():
    rep_cost = input("Input replacement cost of item: $")
    rep_cost = float(rep_cost)

    minimum = min_ins_percent * rep_cost
    
    display_details(rep_cost,minimum)

def display_details(rep_cost,minimum):
    print("Replacement cost is $", format(rep_cost,'.2f'))
    percent_ins = minimum / rep_cost
    print("Your item is ", format(percent_ins * 100,'.2f'),"% insured")
    print("Minimum insurance is $",format(minimum,'.2f'))

main()