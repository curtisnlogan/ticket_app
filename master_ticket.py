TICKET_PRICE = 10
tickets_remaining = 100
SERVICE_CHARGE = 2

while True:
    # Prompt the user for their name and format it properly
    username = input("Enter your username: ").title()
    print(f"Hello {username}, we are delighted that you are interested in one of our events!\n"
          f"Just to let you know, there are {tickets_remaining} ticket(s) remaining.")
    
    # Inform users that tickets are sold out and prevent them from making purchases
    if tickets_remaining <= 0:
        print(f"Sorry {username}, we have sold out of all tickets! We hope to see you next time.")
        continue  # Allow another user to try

    # Check if the user is interested in purchasing tickets
    while True:
        interested = input("Would you like to purchase any tickets? (y/n): ").lower()
        if interested not in ["y", "n"]:
            print("Please enter 'y' or 'n' only!")
            continue
        break  # Valid response received, exit loop

    if interested != "y":
        print(f"Have a great day, {username}!")
        continue  # Restart the process for a new user

    # Define a function to validate the number of tickets the user wants to purchase
    def valid_purchase(number, too_many_tickets):
        if number <= 0:
            raise ValueError("You cannot purchase 0 tickets!")  # Raise an error for invalid input
        if number > too_many_tickets:
            raise ValueError("You cannot purchase more tickets than are available!")

    # Define a function to calculate the total ticket cost, including the service charge
    def calc_tickets(number):
        return (number * TICKET_PRICE) + SERVICE_CHARGE

    while True:
        try:
            # Prompt the user to specify the number of tickets they wish to purchase
            num_tickets = int(input(f"How many tickets would you like to purchase, {username}?: "))
            valid_purchase(num_tickets, tickets_remaining)  # Validate the user's input
        except ValueError as err:
            print(err)  # Display an error message if the input is invalid
            continue
        total_cost = calc_tickets(num_tickets)  # Calculate the total cost of the tickets
        break  # Exit the loop once the input is valid

    while True:
        # Ask the user to confirm their purchase
        confirmation = input(f"{username}, are you sure that you want to purchase {total_cost} dollars worth of tickets?\n"
                            f"This is {num_tickets} ticket(s). It includes a {SERVICE_CHARGE} dollar service charge.\n(y/n): ").lower()

        if confirmation not in ["y", "n"]:
            print("Please enter 'y' or 'n' only!")
            continue
        elif confirmation == "n":
            print(f"Have a great day, {username}!")
            continue  # Restart the process for a new user
        else:
            # Complete the purchase, congratulate the user, and update the ticket count
            print(f"Congratulations {username}!\nYou now own {num_tickets} ticket(s).\nHave a great time at the event(s)!")
            tickets_remaining -= num_tickets  # Deduct the purchased tickets from the available count
