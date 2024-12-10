#!/usr/bin/python3
# Мне стало скучно и я сделал недо-полнотекстовый поиск
import glob

# Перебор всех txt-файлов в каталоге
txt_file_list = (glob.glob('./module_7/test_files/*.txt', recursive=True))

# Выкидываем всякие знаки
replacer = [',', '.', '=', '!', '?', ';', ':', ' - ', ' ', '\n'] 

# Строим словарь (первый проход)
dictionary = []
for file in txt_file_list:
    with open(file, encoding='UTF8') as file:
        for line in file:
            new_line = line
            for fixer in replacer:
                line=line.replace(fixer, ' ')
            for word in line.split(' '):
                if word not in dictionary and word !='' and word !=' ':
                    dictionary.append(word.lower())

print ('Чистый словарь уникальных слов:' + str(dictionary))

# Второй проход поиск по тексту (Но у нас же просто занятия по работе с файлами, и я типа умею)
search_word = 'solr' #Тут можно уже со словарем играть, но есть более простые решения, чем этот изврат
for file in txt_file_list:
    with open(file, encoding='UTF8') as file:
        for line in file:
            lower_line = line.lower()
            if lower_line.find('solr') != -1:
                print (f'Нашли {search_word} в файле {str(file)}')
