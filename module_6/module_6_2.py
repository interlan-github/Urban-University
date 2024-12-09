#!/usr/bin/python3

class Vehicle:
    # Predefined values
    owner = None
    __model = None
    __engine_power = None
    __color = None
    def __init__(self, **kwargs):
        self.owner = kwargs.get('owner')
        self.__model = kwargs.get('model')
        self.__engine_power = kwargs.get('engine_power')
        self.__color = kwargs.get('color')
        self.COLOR_VARIANTS = ['Желтый','Белый','Синий']
        pass
    def get_owner(self):
        return self.owner
    def get_model(self):
        return self.__model
    def get_horsepower(self):
        return self.__engine_power
    def get_color(self):
        if self.__color not in self.COLOR_VARIANTS:
            print ('Такого цвета не бывает')
        return self.__color
    def print_info(self):
        return 'Владелец: ' + self.owner + ' - Мощь в конях: ' + str (self.__engine_power) + ' - цвет: ' + self.__color
    def set_color(self, new_color):
        self.__color = new_color
        print (self.COLOR_VARIANTS)
        if self.__color not in self.COLOR_VARIANTS:
            print ('Такого цвета не бывает')
        pass
    
print ('Первая машина')
base_auto = Vehicle(owner = 'Иван', model = 'Запорожец', engine_power = 'Пердячья тяга', color = 'Желтый')
print (base_auto.get_owner())
print (base_auto.get_model())
print (base_auto.get_horsepower())
print (base_auto.get_color())
print (base_auto.print_info())
print ('------------------ \nВторая машина')
base_auto_test = Vehicle(owner = 'Колян', model = 'Мерс', engine_power = 120, color = 'Странный')
print (base_auto_test.get_color())
print ('Перекрашиваем')
print (base_auto_test.set_color('Желтый'))
print (base_auto_test.print_info())
print ('Перекрашиваем')

# Еще одна тачка
print ('------------------ \nЕще одна машина')
class Sedan(Vehicle):
    def __init__(self, **kwargs):
        Vehicle.__init__(self, **kwargs)
        self.COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
        self.PASSENGERS_LIMIT = 5

my_new_car = Sedan(owner = 'Жека', model = 'Мерс', engine_power = 120, color = 'red')
my_new_car.set_color('red')
print (my_new_car.print_info())
print (my_new_car.COLOR_VARIANTS)
