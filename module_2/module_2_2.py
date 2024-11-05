#!/usr/bin/python3

# Задача "Все ли равны?":
# На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
# Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.
# Пункты задачи:
# Если все числа равны между собой, то вывести 3
# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
# Если равных чисел среди 3-х вообще нет, то вывести 0

first = 123
second = 124
third = 125

if first == second and first == third:
    print (3)
else:
    digital_array = [first,second,third]
    digital_set_len =  (3 - len(set(digital_array)))
    if digital_set_len == 1:
        print (2)
    else:
        print (0)