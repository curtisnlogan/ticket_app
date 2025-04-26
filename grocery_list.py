# TODO: Critical Fixes
# 1. 'else: break' exits on any invalid input, not just 'q' or 'd' - clarify exit logic
# 2. No feedback for empty list on 'v' or 'd' - could confuse users

# original unrefactored code

import time

grocery_list_user = []

while True:
  user_input = input(f"If you want to add an item to your list type in: 'a'.\nIf you want to view your list type in: 'v'.\nIf you want to do neither type in: 'q'.\nIf you have finished making your grocery list, type in: 'd'.\nIf you require help at any point, simply type in: 'help'.").lower().strip()
  time.sleep(1)
  if user_input == "a":
    add_item = input(f"Type in the item that you would like to add to your list: ").strip()
    grocery_list_user.append(add_item)
    print(f"There are {len(grocery_list_user)} items in your grocery list!")
    time.sleep(1)
    continue
  elif user_input == "v":
    print(f"Grocery List: {', '.join(grocery_list_user)}")
    time.sleep(1)
    continue
  elif user_input == "d":
    print(f"Here is your final grocery list: {', '.join(grocery_list_user)}")
    time.sleep(1)
  elif user_input == "help":
    continue
  else:
    break

# TODO: Critical Fixes
# 1. 'else: continue' risks infinite loop on invalid input - add feedback and exit option
# 2. 'grocery_help()' every loop overwhelms user - call only on 'help' or start

# refactored code

import time

master_grocery_list = [] # in real use, master_grocery_list could contain default items. no need for a master list for copying purposes as its blank but i am pretending it is for educational purposes
grocery_list_copy = master_grocery_list.copy()

def grocery_help():
  print(f"Welcome to your grocery list!\nIf you want to add an item to your list type in: 'a'.\nIf you want to view your list type in: 'v'.\nIf you want to exit the app type in: 'q'.\nIf you have finished making your grocery list type in: 'd'.\nIf you require help at any point, type in 'help' to see this message again.\nIf your problem requires further assistance, see the contact information at the bottom of this page.")
  time.sleep(1)

def add_item(list, item):
  list.append(item)
  print(f"There are {len(list)} items in your grocery list!")
  time.sleep(1)
  return list

def view_list(list):
  print(f"Your Grocery List: {', '.join(list)}")
  time.sleep(1)

def done_list(list):
  print(f"Your Final Grocery List is: {', '.join(list)}")
  time.sleep(1)

while True:
  grocery_help()
  user_input = input("Enter Your Response: ").lower().strip()
  if user_input == "a":
    item = input(f"Type in the item that you would like to add to your list: ").strip()
    grocery_list_copy = add_item(grocery_list_copy, item)
    continue
  elif user_input == "v":
    view_list(grocery_list_copy)
    continue
  elif user_input == "q":
    break
  elif user_input == "d":
    done_list(grocery_list_copy)
    break
  elif user_input == "help":
    continue
  else:
    continue
