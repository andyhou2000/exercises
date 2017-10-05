# Programming Exercise 3-6
#
# Program to check if a date is 'magic' (day * month = year).
# This program takes a month, day and year from the user as integers,
# Checks to see if each is in range, then checks whether month * day = year,
# then displays an appropriate message depending on the result

# Variables for month, day, year and message
# initialize month, day and year as integers, message as a string


# Get month and cast it to int


# Get day and cast it to int


# Get year and cast it to int


# This problem can be solved with if-else logic by the reducing the problem domain
# if month input is out of range

	# set message to hold "invalid month" message


# else if day input is out of range

    # set message to hold "invalid day" message

# else if  year input is out of range (greater than 99 or less than 0)

    # set message to hold "invalid year" message

# else 

    # set message to hold the date in 00/00/00 form
    
    # if day * month equals year, add " is a magic date" to message
    
    # else add " is not a magic date" to message


# print message for the user

month = int(input("Input month: "))
day = int(input("Input day: "))
year = int(input("Input year:"))

if month < 1:
    print("Invalid month.")
elif month > 12:
    print("Invalid month.")
else:
    if day < 1:
        print("Invalid day.")
    elif month == 1 and day > 31:
        print("Invalid day.")
    elif month == 3 and day > 31:
        print("Invalid day.")
    elif month == 5 and day > 31:
        print("Invalid day.")
    elif month == 7 and day > 31:
        print("Invalid day.")
    elif month == 8 and day > 31:
        print("Invalid day.")
    elif month == 10 and day > 31:
        print("Invalid day.")
    elif month == 12 and day > 31:
        print("Invalid day.")
    elif month == 4 and day > 30:
        print("Invalid day.")
    elif month == 6 and day > 30:
        print("Invalid day.")
    elif month == 9 and day > 30:
        print("Invalid day.")
    elif month == 11 and day > 30:
        print("Invalid day.")
    elif month == 2 and year % 4 ==0 and day > 29:
        print("Invalid day.")
    elif month == 2 and year % 4 != 0 and day > 28:
        print("Invalid day.")
    else:
        if year > 99:
            print("Invalid year.")
        elif year <1:
            print("Invalid year.")
        else:
            if month * day == year:
                print("Date is ", format(month,'02d'), "/", format(day,'02d'), "/", format(year,'02d'), ", and today is a magic date")
            else:
                print("Date is ", format(month,'02d'), "/", format(day,'02d'), "/", format(year,'02d'), ", and today is not a magic date")
