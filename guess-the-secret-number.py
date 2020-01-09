import random

secret = random.randint(1, 30)

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("Congratulations, you guessed the number! It was " + str(secret))
        break
    elif guess < secret:
        print(str(guess) + " is smaller than the secret number.")
    elif guess > secret:
        print(str(guess) + " is bigger than the secret number.")
