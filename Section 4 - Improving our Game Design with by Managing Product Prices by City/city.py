import random
from product import Product


class City(object):
    cities = []

    def __init__(self, name, has_warehouse, has_bank, has_moneylender):
        # print(name)
        # print(has_moneylender)
        # input("")
        self.name = name
        self.has_warehouse = has_warehouse
        self.has_bank = has_bank
        self.create_city_products()
        self.has_moneylender = has_moneylender
        self.create_city_products()

    def create_city_products(self):
        self.city_products = []
        for product in Product.products:
            self.city_products.append(CityProduct(self, product))

    @classmethod
    def create_city(cls, **kwargs):
        cls.cities.append(City(**kwargs))


class CityProduct(object):
    def __init__(self, city, product):
        self.city = city
        self.product = product
        self.generate_random_price()

    def generate_random_price(self):
        self.price = random.randint(self.product.minprice, self.product.maxprice)

