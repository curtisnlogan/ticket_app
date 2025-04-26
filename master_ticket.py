TICKET_PRICE = 10
tickets_remaining = 100
SERVICE_CHARGE = 2

while True:
    # Get user input and format their name properly
    username = input("Enter a username: ").title()
    print(f"Hello {username}, we are delighted that you are interested in one of our events!\n"
          f"Just to let you know, there are {tickets_remaining} ticket(s) remaining.")
    
    # Prevent users from trying to buy tickets if they are sold out
    if tickets_remaining <= 0:
        print(f"Sorry {username}, we have sold out of all tickets! We hope to see you next time.")
        continue  # Instead of exiting, we let another user try

    # Ask if the user wants to buy tickets
    while True:
        interested = input("Would you like to purchase any tickets?\ny/n: ").lower()
        if interested not in ["y", "n"]:
            print("'y' or 'n' only!")
            continue
        break  # Valid response received, exit loop

    if interested != "y":
        print(f"Have a great day, {username}!")
        continue  # Start over for another user

    # Function to validate the number of tickets the user wants to purchase
    def valid_purchase(number, too_many_tickets):
        if number <= 0:
            raise ValueError("You cannot purchase 0 tickets!")  # Prevents invalid input
        if number > too_many_tickets:
            raise ValueError("You cannot purchase more tickets than there are available!")
    
    # Function to calculate total ticket cost including service charge
    def calc_tickets(number):
        return (number * TICKET_PRICE) + SERVICE_CHARGE

    while True:
        try:
            # Get number of tickets from the user
            num_tickets = int(input(f"How many tickets would you like to purchase, {username}?: "))
            valid_purchase(num_tickets, tickets_remaining)  # Ensure valid input
        except ValueError as err:
            print(err)  # Print error message if input is invalid
            continue
        total_cost = calc_tickets(num_tickets)  # Calculate the total price
        break  # Exit loop if input is valid

    while True:
        # Confirm purchase
        confirmation = input(f"{username}, are you sure that you want to purchase {total_cost} dollars worth of tickets?\n"
                            f"This is {num_tickets} ticket(s). It includes a {SERVICE_CHARGE} dollars service charge.\ny/n: ").lower()

        if confirmation not in ["y", "n"]:
            print("'y' or 'n' only please!")
            continue
        elif confirmation == "n":
            print(f"Have a great day, {username}!")
            continue  # Start over for another user
        else:
            # Final confirmation: complete purchase and update remaining tickets
            print(f"Congratulations {username}!\nYou now own {num_tickets} ticket(s).\nHave a great time at the event(s)!")
            tickets_remaining -= num_tickets  # Deduct tickets from available count
