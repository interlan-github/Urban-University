#!/usr/bin/python3

# Необходимо дополнить класс House следующими специальными методами:

# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

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

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
print (len(h1))
print (len(h2))

print (h1)
print (h2)