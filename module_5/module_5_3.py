#!/usr/bin/python3

# Необходимо дополнить класс House следующими специальными методами:
# __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
# Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
# __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
# __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).

class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors
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

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)
