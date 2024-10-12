#!/usr/bin/python

# 2. Работа со словарями:
#   - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
# Например: Имя(str)-Год рождения(int).
my_dict = {'Anton':1982,'Ivan':2003,'Polina':1982,'Slava':1987}
#   - Выведите на экран словарь my_dict.
print (my_dict)
#   - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
print(my_dict.get('Izabella'))
#   - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
my_dict['Denis'] = True
my_dict['Iona'] = False

#  - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
my_dict.pop('Iona')
#   - Выведите на экран словарь my_dict.
print (my_dict)

# 3. Работа с множествами:
#   - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
my_set = {2,4,1,6,True,False,"a",2,4,"b","a"}
#   - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
print (my_set)
#   - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
my_set.add(12)
my_set.update({45,23,21})
#   - Удалите один любой элемент из множества my_set.
#   - Выведите на экран измененное множество my_set.
print (my_set)