print("Welcome to the program that converts kilometers to miles.")

loop = "y"

while loop == "y":
    km = float(input("Please enter your distance in kilometers: "))

    print("The distance in miles is: " + str(km * 0.621371))
    loop = input("Would you like to convert another distance? (y/n): ")

print("Thank you for using this converter, goodbye!")