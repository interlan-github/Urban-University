#!/usr/bin/python3

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

file_name = 'lines.txt'
write_file = open(file_name,'w',encoding='utf8')
line_number = 0
result = {}
for line in info:
    line_number += 1
    lwb=line+'\n'
    write_file.write(lwb)
    start_position = write_file.tell()
    result.update({(line_number,start_position):line})
print (result)
write_file.close()