#!/usr/bin/python3
from pathlib import Path

class Product():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return str(f'{self.name},{self.weight},{self.category}\n')


class Shop():
    __file_name = 'products.txt'
    products = []
    def add(self):
        pass
    def get_products(self):
        pass
    def add(self, *products):
        current_products = []
        filename = Path(self.__file_name)
        filename.touch(exist_ok=True)
        products_database = open (self.__file_name,'r')
        for exist_product in products_database.read().split('\n'):
            current_products.append(exist_product.split(',')[0])
        products_database.close()
        products_database = open (self.__file_name,'a')
        for item in products:
            if item.name in current_products:
                print (f'Продукт {item.name} уже есть в магазине')
            else:
                print (item)
                products_database.write(str(item))
        products_database.close()
        pass

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p4 = Product('Potato1', 5.5, 'Vegetables')
p3 = Product('Potato', 5.5, 'Vegetables')
p5 = Product('Spaghetti1', 3.4, 'Groceries')
s1.add(p1,p2,p3,p4,p5)