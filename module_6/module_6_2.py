#!/usr/bin/python3

class Animal:
    # Predefined values
    alive = True
    fed = False
    name = None
    # Init Animal
    def __init__(self, data):
        self.alive = data['alive']
        self.name = data['name']
        self.fed = data ['fed']
        pass

class Plant:
    # Predefined values
    edible = False
    name = None
    # Init Plant
    def __init__(self, data):
        self.edible = data['edible']
        self.name = data['name']
        pass

class Mammal(Animal):
    def eat (self, food):
        print (f'Я {self.name} поел {food.name}')
        if food.edible:
            print ('Спасибо вкусно')
        else:
            print ('Усе, я помер')
            self.alive = False

class Predator(Animal):
    def eat (self, food):
        print (f'Я {self.name} поел {food.name}')
        if food.edible:
            print ('Спасибо вкусно')
        else:
            print ('Усе, я помер')
            self.alive = False

# Растения
plant1 = Plant(data = {'edible':True,'name':'Помидорка'})
print (plant1.edible, plant1.name)

plant2 = Plant(data = {'edible':False,'name':'Мухомор'})
print (plant2.edible, plant2.name)

# Звери
cat1 = Animal(data = {'alive':True,'name':'Муська','fed':True})
print (cat1.alive, cat1.name, cat1.fed)

cat1 = Mammal(data = {'alive':True,'name':'Муська','fed':True})
cat1.eat (plant1)
print (cat1.alive, cat1.name, cat1.fed)

cat2 = Animal(data = {'alive':False,'name':'Дохлый бобер','fed':False})
print (cat2.alive, cat2.name, cat2.fed)

cat3 = Predator(data = {'alive':True,'name':'Тигра','fed':True})
cat3.eat (plant2)
print (cat3.alive, cat3.name, cat3.fed)
