#!/usr/bin/python3

# Задача "История строительства":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".
# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
# Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.

# Дополните метод __new__ так, чтобы:
# Название объекта добавлялось в список cls.houses_history.
# Название строения можно взять из args по индексу.
# Также переопределите метод __del__(self) в котором будет выводиться строка:
# "<название> снесён, но он останется в истории"
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history.

class House:
    houses_history = []
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors
        self.houses_history.append(self.name)
    def go_to (self, floor):
        if floor > self.floors:
            print ('"Такого этажа не существует"')
        else:
            for i in range (floor):
                ci = i +1
                print (ci)
    def __len__ (self):
        return self.floors
    def __str__(self):
        return "Название: "+self.name+", кол-во этажей: " + str (self.floors)
    def __eq__(self, other):
        return self.floors == other.floors
    def __lt__(self, other):
        return self.floors < other.floors
    def __gt__(self, other):
        return self.floors > other.floors
    def __ge__(self, other):
        return self.floors >= other.floors
    def __le__(self, other):
        return self.floors <= other.floors
    def __ne__(self, other):
        return self.floors != other.floors
    def __add__(self, other):
        self.floors = self.floors + other
        return self
    def __iadd__(self, other):
        self.floors += other
        return self
    def __radd__(self, other):
        self.floors = other + self.floors
        return self
    def __del__(self):
        print (f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)