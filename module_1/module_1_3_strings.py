#! /usr/bin/python

# В переменную example запишите любую строку.
example = "Мама мыла раму, а рама мыла Маму"
# Выведите на экран(в консоль) первый символ этой строки.
print (example[1])
# Выведите на экран(в консоль) последний символ этой строки (используя отрицательный индекс).
print (example[-1])
# Выведите на экран(в консоль) вторую половину этой строки (С нечётным количеством символов: 'Urban' -> 'ban').
offset = int(len(example)/2)
if not offset%2:
    offset=offset-1
print (example[offset:])
# Выведите на экран(в консоль) это слово наоборот.
print (example[::-1])
# Выведите на экран(в консоль) каждый второй символ этой строки. (Пример: 'Топинамбур'->'оиабр')
print (example[::2])