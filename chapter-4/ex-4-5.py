# Programming Exercise 4-5
#
# Program to compute total and average monthly rainfall over a span of years.
# This program gets a number of years from a user,
# then uses nested loops to prompt for rainfall for each month in each year
#	and calculate the total and the average monthly rainfall,
# then displays the number of months, total rainfall and average monthly rainfall

# Create float variables for total rainfall, monthly rainfall, average monthly rainfall

# Create int variables for number of years and number of months.



# Get number of years from the user

# Nested loop logic to loop through the years and their months
#
# Outer for loop for the number of years

	# Print the current year message

	# Inner loop for 12 months 

		# Get monthly rainfall for current month from the user
		
		# add monthly rainfall to total rainfall
		
		# increment number of months
		
			
# Calculate the average rainfall using total rainfall and number of months

# print the results on the screen, including details for total months, total rainfall,
#	and average monthly rainfall, formatting any floats to 2 decimal places.

startYear = input("Input starting year: ")
startYear = int(startYear)

years = input("Input amount of years: ")
years = int(years)

totalRain = 0
totalRain = float(totalRain)

yearRain = 0
yearRain = float(yearRain)

x = 0
x = int(x)

y = 1
y = int(y)

for x in range(0,years):
	currentYear = startYear + x
	print("Input rainfall data for year",currentYear)
	for y in range(1,13):
		print("Input inches of rain in month", y,": ", end="")
		rain = input()
		rain = float(rain)
		yearRain = yearRain + rain
		y = y + 1
	averageRain = yearRain / 12.0
	print("Rain in year ",currentYear,": ",format(yearRain,'.2f')," inches.")
	print("Average rain per month in year ",currentYear,": ",format(averageRain,'.2f')," inches")
	totalRain = totalRain + yearRain
	yearRain = 0
	x = x + 1
	y = 1
averageTotalRain = totalRain / (12.0 * x)
print("Total rain in period: ",format(totalRain,'.2f')," inches")
print("Average rain per month in period:",format(averageTotalRain,'.2f')," inches")