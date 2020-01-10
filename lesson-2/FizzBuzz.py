end = int(input("Enter a number between 1 and 100: "))

for n in range(1, end+1):
    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)
