import os
import datetime

from product import Product
from city import City

MENU_DIVIDER = "-------------------------------------"
GAME_TITLE = "Python Pirate Trader 0.1A"
PRESS_ANY_KEY = "Press any key to continue"


class GameManager(object):
    def __init__(self, **kwargs):
        self.firm_name = kwargs['name']
        self.cash = kwargs['cash']
        self.debt = kwargs['debt']
        self.cannons = kwargs['cannons']
        self.bank = 0
        self.maxshiphold = kwargs['shiphold']
        self.currentshiphold = 0
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
        buy_select = input("Which Product do you want to buy (1 - %s) - C)ancel :" % str(len(Product.products)))
        if buy_select == "C":
            return
        product_to_buy = Product.products[int(buy_select)-1]
        qty_to_buy = input("How many %s do you wish to buy?" % product_to_buy.name)
        cost_to_buy = product_to_buy.price * int(qty_to_buy)
        print(cost_to_buy)
        if cost_to_buy <= self.cash:
            if self.currentshiphold + int(qty_to_buy) <= self.maxshiphold:
                self.cash -= cost_to_buy
                product_to_buy.shipqty += int(qty_to_buy)
                self.currentshiphold += int(qty_to_buy)
            else:
                print("There is not enough space to  hold items")
                input(PRESS_ANY_KEY)
        else:
            print("Sorry, You don't have enough money.")
            input("continue...")

    def sell(self):
        sell_select = input("Which Product do you want to buy (1 - %s) - C)ancel :" % str(len(Product.products)))
        if sell_select == "C":
            return
        product_to_sell = Product.products[int(sell_select) - 1]
        qty_to_sell = input("How many %s do you wish to sell?" % product_to_sell.name)
        if int(qty_to_sell) <= product_to_sell.shipqty:
            self.cash += int(qty_to_sell) * product_to_sell.price
            product_to_sell.shipqty -= int(qty_to_sell)
            self.currentshiphold -= int(qty_to_sell)
        else:
            print("You don't have that many to sell")
            input(PRESS_ANY_KEY)

    def visit_bank(self):
        input("How much to transfer to the bank?: ")

    def display_products(self):
        i = 1
        for product in Product.products:
            print(str(i) + ")" + product.name + " -- " + str(product.price) + "---" + str(product.shipqty))
            i += 1


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