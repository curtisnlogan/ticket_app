# TODO: Critical Fixes Needed
# 1. Nested while True loops are risky - could hang if 'break' is missed; consider using state variables or breaking this into smaller functions for better readability and maintainability.

import random
import sys

class RandomNumberGame:
    def __init__(self, minrange, maxrange, attempts):
        self.minrange = minrange
        self.maxrange = maxrange
        self.attempts = attempts

    def playrng(self):
        return random.randint(self.minrange, self.maxrange)

# Initialize game variables
obj_rng = RandomNumberGame(0, 0, 0)
won = 0
loss = 0

# Main game loop
while True:
    # Setup loop for game configuration
    while True:
        try:
            print(f"Welcome to the Random Number Game!\n"
                  f"You can choose how many attempts you want to guess the correct number. "
                  f"You have {won} wins and {loss} losses.\n"
                  f"If you want to quit, simply enter 'q' at any prompt.")
            player_attempts = int(input("How many attempts do you want?: "))
            player_minrange = int(input("Minimum number range?: "))
            player_maxrange = int(input("Maximum number range?: "))

            if player_minrange > player_maxrange:
                print("Minimum range must be less than or equal to maximum range!")
                continue
            if player_attempts <= 0:
                print("Number of attempts must be at least 1!")
                continue
            if player_maxrange - player_minrange < 1:
                print("Range between two numbers must be at least 1!")
                continue
        except ValueError:
            print("Invalid input! Please enter a whole number (like 2, not 'abc').")
            continue
        break  # Exit configuration loop once inputs are valid

    # Update game object with user inputs
    obj_rng.attempts = player_attempts
    obj_rng.minrange = player_minrange
    obj_rng.maxrange = player_maxrange
    result = obj_rng.playrng()

    # Game loop for guesses
    for attempt in range(1, player_attempts + 1):
        while True:  # Ensure valid input for each guess
            try:
                raw_guess = input(f"You are on attempt {attempt}. Guess the number: ")
                if raw_guess == "q":  # Allow user to quit mid-game
                    sys.exit()
                else:
                    guess = int(raw_guess)
            except ValueError:
                print("Invalid input! Please enter a whole number (like 2, not 'abc').")
                continue
            break  # Exit input validation loop once guess is valid

        if guess == result:
            print(f"Congratulations! You have won the game! The number was {result}!")
            won += 1
            break  # Exit guessing loop on win
        else:
            if attempt < player_attempts:
                print("Try again!")
            if attempt == player_attempts - 1:
                print("This is your last try!")
            if attempt == player_attempts:
                print(f"Your {player_attempts} attempts have been made. YOU HAVE DIED. The number was {result}!")
                loss += 1
                break  # Exit guessing loop on loss

    # Retry prompt after game ends
    retry = input(f"You have {won} win(s) and {loss} loss(es). Do you want to play again? y/n: ")
    if retry.lower() != "y":
        print(f"Thanks for playing! Your final score is {won} win(s) and {loss} loss(es).")
        break  # Exit main game loop
