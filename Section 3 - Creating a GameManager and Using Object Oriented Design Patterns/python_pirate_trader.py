import os
import datetime
from product import Product
from city import City
from gamemanager import GameManager


def welcome_message():
    print("Welcome to Python Pirate Trader")


def get_firm_name():
    # firm_name = input("Please enter your name: ")
    return "Testing Firm"


def get_starting_options():
    starting_options = "1"
    if starting_options == "1":
        opts = (250, 250, 0)
    else:
        opts = (0, 0, 5)
    return opts


# Create Products


# GEt Game Options
welcome_message()
firm_name = get_firm_name()

cash, debt, cannons = get_starting_options()
game = GameManager(firm_name, cash, debt, cannons, 100)

# Start up Game
game.StartUp()

