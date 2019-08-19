import os
import datetime

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


def leave_port(city_list, current_date):
    i = 1
    for city in city_list:
        print("{0} {1}".format(i, city['name']))
        i = i + 1
    select_city = input("Which city do you wish to go to?: ")
    current_date += datetime.timedelta(days=1)
    return city_list[int(select_city)-1], current_date


def buy():
    input("What do you want to buy?")


def sell():
    input("What do you want to sell?")


def visit_bank():
    input("How much to transfer to the bank?: ")

# Start Game
welcome_message()
firm_name = get_firm_name()
cash, debt, cannons = get_starting_options()

cities = ({'name': 'Hong Kong', 'has_warehouse': True, 'has_bank': True},
          {'name': 'Shangai', 'has_warehouse': False, 'has_bank': False},
          {'name': 'London', 'has_warehouse': False, 'has_bank': False})

current_city = cities[0]
game_running = True
current_date = datetime.datetime(1820, 1, 1)

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

    print("City: %s" % current_city['name'])
    # print("Date: {}".format(current_date))
    # http://strtime.org
    print("Date: {:%B %d, %Y}".format(current_date))

    print(MENU_DIVIDER)

    has_bank_string = ""
    if current_city['has_bank'] == True:
        has_bank_string = "V)isit Bank"

    print("Menu: L)eave Port, B)uy, S)ell, T)ransfer Warehouse, %s Q)uit" % has_bank_string)
    menu_option = input("What is your options?:")
    if menu_option == "L":
        current_city, current_date = leave_port(cities, current_date)
    elif menu_option =="B":
        buy()
    elif menu_option == "S":
        sell()
    elif menu_option == "V" and current_city['has_bank'] == True:
        visit_bank()
    elif menu_option == "Q":
        game_running = False

