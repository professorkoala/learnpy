import random

secret = random.randint(1, 30)
attempts = 0

with open("score.txt", "r") as score_file:
    best_score = int(score_file.read())
    print("Top score: " + str(best_score))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("Congratulations, you guessed the number! It was " + str(secret))
        print("Your attempts: " + str(attempts))
        if attempts < best_score:
            with open ("score.txt", "w") as score_file:
                score_file.write(str(attempts))
        break
    elif guess < secret:
        print(str(guess) + " is smaller than the secret number.")
    elif guess > secret:
        print(str(guess) + " is bigger than the secret number.")
