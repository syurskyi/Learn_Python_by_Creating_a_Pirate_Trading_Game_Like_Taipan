import os
import datetime
import random

from product import Product
from city import City
from PirateEncounter import PirateEncounter
from gamedata import load_city_data


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
        self.ship_health = 100
        Product.create_products()
        load_city_data(City)
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
        city_product = self.current_city.city_products[int(buy_select)-1]
        qty_to_buy = input("How many %s do you wish to buy?" % city_product.product.name)
        cost_to_buy = city_product.price * int(qty_to_buy)
        print(cost_to_buy)
        if cost_to_buy <= self.cash:
            if self.currentshiphold + int(qty_to_buy) <= self.maxshiphold:
                self.cash -= cost_to_buy
                city_product.product.shipqty += int(qty_to_buy)
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
        city_product = self.current_city.city_products[int(sell_select) - 1]
        qty_to_sell = input("How many %s do you wish to sell?" % city_product.product.name)
        if int(qty_to_sell) <= city_product.product.shipqty:
            self.cash += int(qty_to_sell) * city_product.price
            city_product.product.shipqty -= int(qty_to_sell)
            self.currentshiphold -= int(qty_to_sell)
        else:
            print("You don't have that many to sell")
            input(PRESS_ANY_KEY)

    def visit_bank(self):
        input("How much to transfer to the bank?: ")

    def display_products(self):
        i = 1
        for cityproduct in self.current_city.city_products:
            print(str(i) + ")" + cityproduct.product.name + " -- " + str(cityproduct.price) + "---" +
                  str(cityproduct.product.shipqty))
            i += 1

    def check_price_change(self):
        result = random.randint(0, 100)
        if result >= 75:
            for city_product in self.current_city.city_products:
                city_product.generate_random_price()

    def increased_debt(self):
        self.debt *= 1.15

    def visit_money_lender(self):
        payback = input("How much do you wish to pay back?")
        if int(payback) <= self.cash:
            self.debt -= int(payback)
            self.cash -= int(payback)
        borrow = input("How much do you wish to borrow?")
        if int(borrow) <= self.cash*20:
            self.debt += int(borrow)
            self.cash += int(borrow)

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
            print("Debt: {:.0f}".format(self.debt))
            print("Cannons: %d " % self.cannons)
            print("City: %s" % self.current_city.name)
            print("Ship Health: %s" % self.ship_health)
            # print("Date: {}".format(current_date))
            # http://strtime.org
            print("Date: {:%B %d, %Y}".format(self.current_date))
            print(MENU_DIVIDER)
            print("-------City Products-----------")
            self.display_products()

            has_bank_string = ""

            if self.current_city.has_bank == True:
                has_bank_string = "V)isit Bank,"
            has_moneylender = ""
            if self.current_city.has_moneylender == True:
                has_moneylender = "M)oney Lender,"
            print("Menu: L)eave Port, B)uy, S)ell, T)ransfer Warehouse, %s %s Q)uit" % (has_bank_string, has_moneylender))
            menu_option = input("What is your options?:")
            if menu_option == "L":
                self.current_city, self.current_date = self.leave_port(City.cities, self.current_date)
                self.check_price_change()
                self.increased_debt()
                pirates = PirateEncounter(self)
            elif menu_option == "B":
                self.buy()
            elif menu_option == "M":
                self.visit_money_lender()
            elif menu_option == "S":
                self.sell()
            elif menu_option == "V" and self.current_city.has_bank == True:
                self.visit_bank()
            elif menu_option == "Q":
                game_running = False