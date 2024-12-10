#!/usr/bin/python3
import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _cords = [0, 0, 0]
    def __init__(self, speed):
        self.speed = speed
        pass
    def get_cords(self):
        print (self._cords)
    def move (self, dx, dy, dz):
        x = self._cords [0] + dx * self.speed
        y = self._cords [1] + dy * self.speed
        z = self._cords [2] + dz * self.speed
        if z < 0:
            print ('It\'s too deep, i can\'t dive :(')
        else:
            self._cords [0] = x
            self._cords [1] = y
            self._cords [2] = z
    def attack (self):
        if self._DEGREE_OF_DANGER > 5:
            print ('Be careful, i\'m attacking you 0_0')
        else:
            print ('Sorry, i\'m peaceful :)')
    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True
    def lay_eggs(self):
        print ('Here are(is) '+str(random.randint(1, 4))+' eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        self._cords[2] = self._cords[2] - dz * self.speed
        if self._cords[2] < 0:
            self._cords [2] = 0
            print ('It\'s too deep, i can\'t dive :(')

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(AquaticAnimal, PoisonousAnimal, Bird):
    def __init__(self, speed):
        self.sound = "Click-click-click"
        super().__init__(speed)

db = Bird (10)
print (Duckbill.mro())
db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()