#!/usr/bin/python3

def personal_sum(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

def calculate_average(input_numbers):
    numbers =[]
    if type(input_numbers) == int:
        return "Передана не коллекция"

    if type(input_numbers) == str:
        input_numbers_list = list(input_numbers)
        for item in input_numbers_list:
            try:
                numbers.append(int(item))
            except:
                print(f"Некорректный тип данных для подсчёта суммы - {item}")

    if type(input_numbers) == list:
        for item in input_numbers:
            try:
                numbers.append(int(item))
            except:
                print(f"Некорректный тип данных для подсчёта суммы - {item}")

    result = personal_sum(numbers)/len(numbers)
    return result

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать