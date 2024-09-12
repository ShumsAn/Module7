import os
import time

directory = '.'
#Тренировочный вариант для усвоения
# for root, dirs, files in os.walk(directory):
#   for file in files:
#     filepath = os.path.join('C:', 'Users', 'user\PycharmProjects\pythonProject\Module_7', '\Module7_hard')
#     filetime = os.path.getmtime('/Users/user/PycharmProjects/pythonProject/Module_7/Module7_hard/')
#     formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#     filesize = os.path.getsize(file)
#     parent_dir = os.path.dirname(filepath)
#     print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
#
# Рабочий вариант
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root,file)
        filetime = os.path.getmtime(root)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(filepath)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

