def custom_write(file_name, strings):
    strings_positions = {} # зададим пустой словарь, в кот. будут позиции строк и они сами

    # откр. файл в режиме записи с кодировкой utf-8
    file = open(file_name, 'w', encoding='utf-8')
    for i, string in enumerate(strings): # перебир. строки с возвратом индекса и эл.
        position = file.tell() # возврат кол-ва байт
        file.write(string + '\n') # запис. строку в файл и "Энтер"
        # добавим позицию строки и ее саму в словарь (ключ - кортеж)
        # i+1 - нумерация строк с 1
        strings_positions[(i+1, position)] = string
    file.close() # закр. файл

    return strings_positions # возвращ. словаря с данными

# Пример выполняемого кода:

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)