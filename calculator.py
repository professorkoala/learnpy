number_one = int(input("Enter number one: "))
number_two = int(input("Enter number two: "))
operation = input("Choose arithmetic operation (+, -, * or /): ")

if operation == "+":
    print(number_one + number_two)
elif operation == "-":
    print(number_one - number_two)
elif operation == "*":
    print(number_one * number_two)
elif operation == "/":
    print(number_one / number_two)
else:
    print("Unknown arithmetic operation")
