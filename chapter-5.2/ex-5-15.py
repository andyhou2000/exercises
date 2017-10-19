# Programming Exercise 5-15
#
# Program to find the average of five scores and output the scores and average with letter grade equivalents.
# This program prompts a user for five numerical scores,
# calculates their average, and assigns letter grades to each,
# and outputs the list and average as a table on the screen.

# define the main function

    # define local variables for average and five scores


    # Get five scores from the user


    # find the average by passing the scores to a function that returns the average


    # display grade and average information in tabular form
    # as score, numeric grade, letter grade, separated by tabs
    
    # display a line of underscores under this header
    
    # print data for all five scores, using the score,
    # with the result of a function to determine letter grade

    # display a line of underscores under this table of data

    # display the average and the letter grade for the average



# Define a function to return the average of 5 grades.
# This function accepts five values as parameters,
# computes the average,
# and returns the average.

    # define a local float variable to hold the average
    
    # calculate the average
    
    # return the average



# Define a function to return a numeric grade from a number.
# This function accepts a grade as a parameter,
# Uses logical tests to assign it a letter grade,
# and returns the letter grade.

    # if score is 90 or more, return A
    
    # 80 or more, return B
    
    # 70 or more, return C
    
    # 60 or more, return D
    
    # anything else, return F


# Call the main function to start the program

def main():
    a = input("Input first score: ")
    a = float(a)
    b = input("Input second score: ")
    b = float(b)
    c = input("Input third score: ")
    c = float(c)
    d = input("Input fourth score: ")
    d = float(d)
    e = input("Input fifth score: ")
    e = float(e)
    average(a,b,c,d,e)
    
def average(a,b,c,d,e):
    avg = (a + b + c + d + e) / 5
    print("Average Store = ",avg,"%")
    letter(avg)

def letter(avg):
    if avg >= 90:
        letter = "A"
    elif avg >= 80 and avg <90:
        letter = "B"
    elif avg >= 70 and avg < 80:
        letter = "C"
    elif avg >= 60 and avg < 70:
        letter = "D"
    else:
        letter = "F"
    
    print("Letter Grade = ",letter)
    
main()
