import os

MENU_DIVIDER = "-------------------------------------"
GAME_TITLE = "Python Pirate Trader 0.1A"


def welcome_message():
    print("Welcome to Python Pirate Trader")


def get_firm_name():
    # firm_name = input("Please enter your name: ")
    return "Testing Firm"


def get_starting_options():
    # starting_options = input("How do you wish to start. 1) Cash & Debt 2) Cannons no debt.: ")

    # if starting_options == "1":
    #     cash = 250
    #     debt = cash
    #     cannons = 0
    # else:
    #     cash = 0
    #     debt = 0
    #     cannons = 5
    # return cash, debt, cannons
    starting_options = "1"
    if starting_options == "1":
        opts = (250, 250, 0)
    else:
        opts = (0, 0, 5)
    return opts


def leave_port():
    pass


def buy():
    input("What do you want to buy?")


def sell():
    input("What do you want to sell?")


# Start Game
welcome_message()
firm_name = get_firm_name()
cash, debt, cannons = get_starting_options()

game_running = True
while game_running:
    # Display Main Game Interface
    os.system("cls")  # clear terminal
    print(MENU_DIVIDER)
    print(GAME_TITLE)
    print(MENU_DIVIDER)

    # Python String Format Cookbook

    # print("Firm Name: " + firm_name)
    # print("Cash = " + str(cash))
    # print("Debt = " + str(debt))
    # print("Cannons = " + str(cannons))

    # print("Firm Name: %s" % firm_name)
    # print("Cash: %d " % cash)
    # print("Debt: %d " % debt)
    # print("Cannons: %d " % cannons)

    print("Firm Name: %s" % firm_name)
    print("Cash: {} ".format(cash))
    print(f"Debt: {debt}")
    print("Cannons: %d " % cannons)

    print("City: [current_city]")
    print("Date:")

    print(MENU_DIVIDER)

    print("Menu: L)eave Port, B)uy, S)ell, T)ransfer Bank, V)isit the Money Lender, Q)uit")
    menu_option = input("What is your options?:")
    if menu_option == "L":
        leave_port()
    elif menu_option =="B":
        buy()
    elif menu_option == "S":
        sell()
    elif menu_option == "Q":
        game_running = False