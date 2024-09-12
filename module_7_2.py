def custom_write(file_name, strings):
    strings_positions = {}
    string_num = 0
    file = open(file_name, 'a', encoding='utf-8')
    for string in strings:
        string_num += 1
        if string_num == 1:
            ft = file.tell()
            file.write(f'{string}')
        else:
            ft = file.tell()+2
            file.write(f'\n{string}')

        strings_positions[(string_num, ft)] = f'{string}'
    file.close()

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


