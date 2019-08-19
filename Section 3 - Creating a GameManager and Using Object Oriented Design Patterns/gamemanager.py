import os
import datetime

from product import Product
from city import City

MENU_DIVIDER = "-------------------------------------"
GAME_TITLE = "Python Pirate Trader 0.1A"


class GameManager(object):
    def __init__(self, **args):
        self.firm_name = args['name']
        self.cash = args['cash']
        self.debt = args['debt']
        self.cannons = args[3]
        self.bank = 0
        self.shiphold = args[4]
        Product.create_products()
        City.create_cities()
        self.current_city = City.cities[0]
        self.current_date = datetime.datetime(1820, 1, 1)

    def leave_port(self, city_list, current_date):
        i = 1
        for city in city_list:
            print("{0} {1}".format(i, city.name))
            i = i + 1
        select_city = input("Which city do you wish to go to?: ")
        current_date += datetime.timedelta(days=1)
        return city_list[int(select_city) - 1], current_date

    def buy(self):
        input("What do you want to buy?")

    def sell(self):
        input("What do you want to sell?")

    def visit_bank(self):
        input("How much to transfer to the bank?: ")

    def display_products(self):
        for product in Product.products:
            print(product.name + " -- " + str(product.price))

    def StartUp(self):

        game_running = True

        while game_running:
            # Display Main Game Interface
            os.system("cls")  # clear terminal
            # Stuff to debuggin
            # --------------------
            print(MENU_DIVIDER)
            print(GAME_TITLE)
            print(MENU_DIVIDER)

            print("Firm Name: %s" % self.firm_name)
            print("Cash: {} ".format(self.cash))
            print(f"Debt: {self.debt}")
            print("Cannons: %d " % self.cannons)
            print("City: %s" % self.current_city.name)
            # print("Date: {}".format(current_date))
            # http://strtime.org
            print("Date: {:%B %d, %Y}".format(self.current_date))
            print(MENU_DIVIDER)
            print("-------City Products-----------")
            self.display_products()

            has_bank_string = ""

            if self.current_city.has_bank == True:
                has_bank_string = "V)isit Bank,"

            print("Menu: L)eave Port, B)uy, S)ell, T)ransfer Warehouse, %s Q)uit" % has_bank_string)
            menu_option = input("What is your options?:")
            if menu_option == "L":
                self.current_city, self.current_date = self.leave_port(City.cities, self.current_date)
            elif menu_option == "B":
                self.buy()
            elif menu_option == "S":
                self.sell()
            elif menu_option == "V" and self.current_city.has_bank == True:
                self.visit_bank()
            elif menu_option == "Q":
                game_running = False