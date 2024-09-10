def custom_write(file_name, strings):
    strings_positions = {}
    string_num = 0
    for string in strings:
        string_num += 1
        file = open(file_name, 'a+', encoding='utf-8')
        ft = file.tell()
        file.write(f'\n {string}')
        file.close()
        file = open(file_name, 'r', encoding='utf-8')
        file.seek(ft)
        strings_positions[(string_num, ft)] = f'{file.read()}'

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
