import math

def area(width, length):
    return width * length

def perimeter(width, length):
    return 2 * (width + length)

def areaC(radius):
    return math.pi * radius**2

def circumference(radius):
    return 2 * math.pi * radius

AREA_OF_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

def main():

    choice = 0

    while choice != QUIT_CHOICE:
        display_menu()
        choice = int(input("Enter your choice: "))
        a = handle_choice(choice)
        print(a)

def display_menu():
    print(" MENU")
    print("1) Area of a circle")
    print("2) Circumference of a circle")
    print("3) Area of a rectangle")
    print("4) Perimeter of a rectangle")
    print("5) Quit")

def handle_choice(choice):
    if choice == AREA_OF_CIRCLE_CHOICE:
        radius = float(input("Enter the circle's radius: "))
        return "The area is " + str(areaC(radius))
    elif choice == CIRCUMFERENCE_CHOICE:
        radius = float(input("Enter the circle's radius: "))
        return "The area is " + str(circumference(radius))
    elif choice == AREA_RECTANGLE_CHOICE:
        width = float(input("Enter the rectangle's width: "))
        length = float(input("Enter the rectangle's length: "))
        return "The area is " + str(area(width,length))
    elif choice == PERIMETER_RECTANGLE_CHOICE:
        width = float(input("Enter the rectangle's width: "))
        length = float(input("Enter the rectangle's length: "))
        return "The perimeter is " + str(perimeter(width,length))
    elif choice == QUIT_CHOICE:
        return "Exiting the program..."
    else:
        return "Error: Invalid selection."

main()


