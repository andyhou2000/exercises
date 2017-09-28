mpg = input("Input car's miles per gallon: ")
mpg = float(mpg)
dist = input("Input distance driven :")
dist = float(dist)

gallonsUsed = dist * mpg
gallonsUsed = float(gallonsUsed)

print("Used %.2f"%gallonsUsed, "gallons")