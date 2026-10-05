import random

print("Welcome to Number Guessing Game")
print("Imagine a number from 1 to 20")
print("Your total attempts are 10")


def game():
    guess = random.randint(1, 20)
    score = 0
    total_attempts = 10
    attempts = 0

    while attempts < total_attempts:

        try:
            g = int(input("Make a guess: "))
        except ValueError:
            print("Enter a valid integer")
            continue

        attempts += 1

        if guess == g:
            print("Congrats!! Your guess is correct")
            score += 1
            break

        elif g < guess:
            print("Your guess is low")

        else:
            print("Your guess is high")

        print("Attempts used:", attempts)
        print("Attempts remaining:", total_attempts - attempts)

    if attempts == total_attempts and g != guess:
        print("Sorry, you ran out of attempts")
        print("The correct number was:", guess)

    print("Your Current Score is:", score)


game()
