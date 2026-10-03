import random

# Generate a random 4 Digit number
secret_num = random.randrange(1000, 10000)

# It start attempt by 0
attempt = 0

# Welcome in Mastermind game
print("Welcome in Mastermind game")
print("Try to Guess 4 Digit number. \n")

# Makes a loop for the game
while True:
    # Protect code from crashes
    try:
        # Asks user to guess the number of 4 digits
        guess = int(input("Guess the 4 digit number: "))

        # The basic logic of game to prevent game from low or high entered value
        if guess < 1000 or guess > 9999:
            print("Please Enter a 4 digit number: ")
            continue
    # Save the code from crashing and prints the custom string
    except ValueError:
        print("Invalid input, please enter the answer in int..")
        continue

    # Add on every attempt
    attempt += 1

    # This line check that the value user entered is correct or not
    if secret_num == guess:
        print("\n you've became a mastermind")
        print(f"it tooks {attempt} attempts")
        # breaks the code if complete the conditions of this line
        break

    # Converts the int into str 
    guess_str = str(guess)
    secret_str = str(secret_num)

    # This line starts the counts from 0
    count = 0
    correct = ['x'] *4

    # Makes a loop 
    for i in range(4):
        if guess_str[i] == secret_str[i]:
            count += 1
            correct[i] = guess_str[i]

    # Prints that in how count we guessed
    print(f"\nNot quite the number. You did get {count} digit(s) correct.")


    if count > 0:
        print("Correctly Placed Digits:")
        print(" ".join(correct))

    print()
