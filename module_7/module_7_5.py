#!/usr/bin/python3
import os
from datetime import datetime

# Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
# Примените os.path.join для формирования полного пути к файлам.
# Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
# Используйте os.path.getsize для получения размера файла.
# Используйте os.path.dirname для получения родительской директории файла.

for dir, dirs, files in os.walk('.'+os.sep):
    for name in files:
        full_name = os.path.join(dir, name)
        m_time = os.path.getmtime(full_name)
        m_time_str = datetime.fromtimestamp(m_time).strftime('%Y-%m-%d %H:%M:%S')
        print(print(f'Обнаружен файл: {full_name}, Путь: {full_name}, Размер: {os.path.getsize(full_name)} байт, Время изменения: {m_time_str}, Родительская директория: {dir}'))
