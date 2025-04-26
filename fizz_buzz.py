#  TODO: Critical Fixes
# 1. No error handling for int(input()) - crashes on non-integer input
# 2. is_fizz/is_buzz use numbers, not Booleans - risky logic, fix to True/False
# 3. needs docstrings
# 4. refactoring into OOP

import logging # useful for recording events that happen
# when the program runs and that you dont want the user to see. use logging
# instead of print for debugging

logging.basicConfig(filename='fizz_buzz.log', level=logging.DEBUG)
# 'level'refers to the severity of the log messages that will be captured

name = input("Enter your name: ")
number = int(input("Enter a number: ")) # can add a breakpoint here and this line will not run
# then can use the debugger to step through the code
# if the user enters a non-integer, the program will crash as there is no error handling
IS_FIZZ = ""
IS_BUZZ = ""
logging.debug("User %s has entered number %d", name, number)
# use lazy string formatting instead of f-strings to avoid overhead if logging is disabled

if number % 3 == 0:
    IS_FIZZ = number
if number % 5 == 0:
    IS_BUZZ = number
elif number % 5 == 0:
    is_buzz = number

print(f"Hello {name}!")
print(f"You picked the number {number}!")

if IS_FIZZ and IS_BUZZ:
    print(f"{number} is a FizzBuzz number!")
elif IS_FIZZ:
    print(f"{number} is a Fizz number!")
elif IS_BUZZ:
    print(f"{number} is a Buzz number!")
else:
    print(f"{number} is neither a fizzy or a buzzy number!")
# blank line at end of file pep8
