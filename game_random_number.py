import random

class GameRandomNumber:
    """
    Defines a random number game class. The jist of the game is simple; the player must merely guess the number which has been chosen at random. Some complexity is added through three user selectable difficulty modes, which will modify the number of guesses that are allowed and win/loss tracking.
    """
    def __init__(self):
        """
        win: int (tracks the number of wins a player has)
        loss: int (tracks the number of losses a player has)
        min_num: int (tracks the minimum number which can be chosen at random)
        max_num: int (tracks the maximum number which can be chosen at random)
        attempts: int (tracks the number of attempts the player has had to guess the correct number)
        """
        self.wins = 0
        self.losses = 0
        self.min_num = 0
        self.max_num = 0
        self.attempts = 0

    def intro(self):
        """
        Function introduces the player to the basics of the game and shows them their current number of wins and losses.
        """
        print(f"Welcome to the Random Number Game!\nYou will have a certain number of attempts to guess the correct number.\nYou can choose between easy, normal and hard difficulty modes!\nYou currently have {self.wins} wins and {self.losses} losses.")

    def difficulty(self):
        """
        Function controls everything to do with difficulty selection and what those specific difficulties modify.
        """
        while True:
            try:
                user_difficulty = input(f"Would you like to play on 'easy', 'normal' or 'hard' difficulty!\nType in your chosen difficulty here: ").lower().strip()
                if user_difficulty != "easy":
                    raise ValueError
            except ValueError as err_1:
                print(f"'easy', 'normal' or 'hard' only please!")
                continue
            if user_difficulty == "easy":
                self.min_num = 1
                self.max_num = 10
                self.attempts = 5
                break
            elif user_difficulty == "normal":
              self.min_num = 1
              self.max_num = 50
              self.attempts = 10
              break
            elif user_difficulty == "hard":
                self.min_num = 1
                self.max_num = 100
                self.attempts = 3
                break
    def play():
        return random.randint(self.min_num, self.max_num)
    def guess(self):
        valid_input = False
        while valid_input == False:
            try:
                user_guess = int(input(f"Guess the number!: "))
                valid_input = True
            except ValueError:
                print("Numbers only!")
            if user_guess == result:
                print(f"Congratulations! You have won the game! The number was {result}!")
                win_count += 1
                valid_result = True
            else:
                if current_attempt < total_attempts:
                    print("Try again!")
                    current_attempt += 1
                    valid_input = False
                elif current_attempt == total_attempts:
                    print("This is your last try!")
                    current_attempt += 1
                    valid_input = False
                elif current_attempt > total_attempts:
                    print(f"Your {total_attempts} attempts have been made. YOU HAVE DIED. The number was {result}!")
                    loss_count += 1
                    current_attempt = 1
                    valid_result = True
            continue

new_vegas_casino = GameRandomNumber(0, 0, 0, 0, 0)

while True:
    new_vegas_casino.intro()
    outputs = new_vegas_casino.play()
    total_attempts = outputs[1]
    result = outputs[0]
    win = outputs[2]
    loss = outputs[3]
    current_attempt = 1