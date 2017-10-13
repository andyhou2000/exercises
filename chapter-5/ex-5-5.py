# Programming Exercise 5-5
#
# Program to compute assessed value and property tax.
# This program accepts a property value from a user,
# uses global constants to calculate an assessed value and property tax,
# then passes them to a function to display the results for the user.



# Global constants for assessment percentage and property tax rate



# define the main function

    # Define local float variables for property value, assessed value and property tax


    # Get the property value from the user.


    # Calculate the assessed value using the global constant


    # Calculate the property tax using the global constant


    # Call the function to display property tax information, 
    # passing assessed value and property tax as arguments


    
# Define a function to display property tax information.
# This function accepts the assessed value and property tax as parameters,
# performs no calculations,
# but displays the information with float variables formatted to 2 decimal places.

	# display the assessed value
	
	# display the property tax



# Call the main function to begin the program.
prop_tax_rate = float(.0144)
assess_rate = float(.8)
    
def main():
    prop_val = input("Input property value: ")
    prop_val = float(prop_val)
    
    assess_val = prop_val * assess_rate
    prop_tax = assess_val * prop_tax_rate
    
    prop_info(assess_val,prop_tax)

def prop_info(assess_val,prop_tax):
    print("Assessed value of house: $",format(assess_val,'.2f'))
    print("Property tax on house: $",format(prop_tax,'.2f'))
    
main()