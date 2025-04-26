# TODO: Critical Fixes Needed
# 1. Nested while True loops risky - could hang if break missed; consider state variable or functions

import random
import sys

class RandomNumberGame:
    def __init__(self, minrange, maxrange, attempts):
        self.minrange = minrange
        self.maxrange = maxrange
        self.attempts = attempts
    def playrng(self):
        return (random.randint(self.minrange, self.maxrange))

obj_rng = RandomNumberGame(0, 0, 0)
won = 0
loss = 0

while True:
    while True:
        try:
            print(f"Welcome to the Random Number Game!\nYou can choose how many attempts you want to guess the correct number. You have {won} wins and {loss} losses.\nIf you want to quit simply enter 'q' during any guess attempt.")
            player_attempts = int(input(f"How many attempts do you want?: "))
            player_minrange = int(input(f"Minimum number range?: "))
            player_maxrange = int(input(f"Maximum number range?: "))
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
        break
    obj_rng.attempts = player_attempts
    obj_rng.minrange = player_minrange
    obj_rng.maxrange = player_maxrange
    result = obj_rng.playrng()
    for attempt in range(1, player_attempts + 1):
     while True:
          try:
               raw_guess = input(f"You are on attempt {attempt}. Guess the number: ")
               if raw_guess == "q":
                    sys.exit()
               else:
                    guess = int(raw_guess)
          except ValueError:
               print("Invalid input! Please enter a whole number (like 2, not 'abc').")  
               continue  
          break
     if guess == result:
          print(f"Congratulations! You have won the game! The number was {result}!")
          won += 1
          break
     else:
          if attempt < player_attempts:
               print("Try again!")
          if attempt == player_attempts - 1:
               print("This is your last try!")
          if attempt == player_attempts:
               print(f"Your {player_attempts} attempts have been made. YOU HAVE DIED. The number was {result}!")
               loss += 1
               break
    retry = input(f"You have {won} win(s) and {loss} loss(es). Do you want to play again? y/n: ")
    if retry.lower() != "y":
        print(f"Thanks for playing! Your final score is {won} win(s) and {loss} loss(s)")
        break
