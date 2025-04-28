TICKET_PRICE = 10  # dollars, constants are always in capital letters
SERVICE_CHARGE = 2  # dollars, only applied once per purchase, not per ticket
tickets_remaining = 100  # variables are always in snake_case


def welcome_customer():  # no parameters needed
    username = input("Enter your username: ").strip()  # strip nice for
    # removing accidental whitespace
    print(f"Hello {username}, we are delighted"  # printing on seperate lines
          # to keep within pep8 guidelines
          "that you are interested in "  # continution lines must
          #  be aligned with parens
          "purchasing tickets for one of our events!\n"
          "Just to let you know, there are"  # no need for f string
          f"{tickets_remaining} ticket(s) remaining.")
    if tickets_remaining <= 0:
        return (f"Sorry {username}, as you can see, "  # again lining up
                # continuation lines with parens
                f"we have sold out all of our tickets for this event!")
    else:
        return username


def validate_purchase(username: str):  # grab username from welcome_customer
    interested_purchasing = (input("Would you like to "
                                   "purchase any tickets?"
                                   "(y/n): ")).lower().strip()
    if interested_purchasing not in ["y", "n"]:
        print("Please enter 'y' or 'n' only!")
        return
    num_tickets = int(input("How many tickets would you like to purchase,"
                            f"{username}?: ")).strip()
    if num_tickets <= 0:
        raise ValueError("You cannot purchase 0 tickets!")
    if num_tickets > tickets_remaining:
        raise ValueError("You cannot purchase more tickets"
                         "than we have available!")
    else:
        return num_tickets


def calc_tickets(num_tickets: int):
    return (num_tickets * TICKET_PRICE) + SERVICE_CHARGE


def confirm_purchase(username: str, num_tickets: int):
    confirmation_ans = input(
            f"{username}, are you sure that you want to purchase"
            f"{total_cost} dollars worth of tickets?\n"
            f"This is {num_tickets} ticket(s). It includes a"
            f"{SERVICE_CHARGE} dollar service charge.\n(y/n): "
        ).lower()

    if confirmation_ans not in ["y", "n"]:
        print("Please enter 'y' or 'n' only!")
    elif confirmation_ans == "n":
        print(f"Have a great day, {username}!")
    else:
        print(f"Congratulations {username}!\n"
              f"You now own {num_tickets} ticket(s).\n"
              "Have a great time at the event(s)!")
        tickets_remaining -= num_tickets


def main():
    total_cost = calc_tickets(num_tickets)


if __name__ == "__main__":
    main()
