import random


class Product(object):
    products = []

    def __init__(self, name, minprice, maxprice):
        self.name = name
        self.minprice = minprice
        self.maxprice = maxprice
        self.price = random.randint(self.minprice, self.maxprice)
        self.shipqty = 0
        self.warehouseqty = 0

    @classmethod
    def create_products(cls):
        cls.products.append(Product("General Goods", 3, 20))
        cls.products.append(Product("Arms", 10, 75))