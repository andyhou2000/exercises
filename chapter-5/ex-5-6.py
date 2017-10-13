# Programming Exercise 5-6
#
# Program to compute calories from fat and carbohydrate.
# This program accepts fat grams and carbohydrate grams consumed from a user,
# uses global constants to calculate the fat calories and carb calories,
# then passes them to a function for formatted display on the screen.


# Global constants for fat calories per gram and carb calories per gram



# define the main function

    # Define local float variables for grams of fat, grams of carbs, calories from fat,
    # and calories from carbs
    

    # Get grams of fat from the user.


    # Get grams of carbs from the user.


    # Calculate calories from fat.


    # Calculate calories from carbs.


    # Call the display calorie detail function, passing grams of fat, grams of carbs,
    # calories from fat and calories from carbs as arguments



# Define a function to display calorie detail.
# This function accepts grams of fat, grams of carbs, calories from fat,
# and calories from carbs as parameters,
# performs no calculations,
# but displays this information formatted for the user.

	# print each piece of information with floats formatted to 2 decimal places.



# Call the main function to start the program

def main():
    cal_per_g_fat = float(9.0)
    cal_per_g_carb = float(4.0)
    
    g_fat = input("Input grams of fat consumed: ")
    g_fat = float(g_fat)
    
    g_carb = input("Input grams of carbs consumed: ")
    g_carb = float(g_carb)
    
    cal_fat = float(cal_per_g_fat * g_fat)
    cal_carb = float(cal_per_g_carb * g_carb)
    
    caldetail(g_fat,g_carb,cal_fat,cal_carb)
    
def caldetail(g_fat,g_carb,cal_fat,cal_carb):
    print("Grams of fat consumed: ", format(g_fat,'.2f'))
    print("Grams of carbs consumed: ", format(g_carb,'.2f'))
    print("Cal from fat: ", format(cal_fat,'.2f'))
    print("Cal from carbs: ", format(cal_carb,'.2f'))
    
main()