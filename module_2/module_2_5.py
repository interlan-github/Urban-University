#!/usr/bin/python3

# Пункты задачи:

# Объявите функцию get_matrix и напишите в ней параметры n, m и value.
# Создайте пустой список matrix внутри функции get_matrix.
# Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
# В первом цикле добавляйте пустой список в список matrix.
# Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
# Во втором цикле пополняйте ранее добавленный пустой список значениями value.
# После всех циклов верните значение переменной matrix.
# Выведите на экран(консоль) результат работы функции get_matrix.

def get_matrix(n, m ,value):
    matrix_n = []
    for counter_n in range(n):
        matrix_m = []
        for counter_m in range(m):
            matrix_m.append(value)
        matrix_n.append(matrix_m)
    return matrix_n

result_1 = get_matrix(2, 2, 10)
result_2 = get_matrix(3, 5, 42)
result_3 = get_matrix(4, 2, 13)
print (result_1)
print (result_2)
print (result_3)
