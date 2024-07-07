from data_create import name_data, surname_data, phone_data, address_data
import os
import re

def remove_old_indices(block, delimiter):
    lines = block.strip().split(delimiter)
    # Предполагаем, что индекс находится в первой строке блока и он состоит только из чисел
    if re.match(r'^\d+$', lines[0]):
        return delimiter.join(lines[1:])
    return block.strip()

def enumerate_and_save_data(file_name, delimiter='\n'):
    if not os.path.exists(file_name):
        print(f"Файл {file_name} не найден.")
        return
    
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.read()
    
    blocks = data.strip().split('\n\n')
    enumerated_blocks = []

    for index, block in enumerate(blocks):
        if block.strip():  # Игнорируем пустые блоки
            block = remove_old_indices(block, delimiter)
            enumerated_block = f"{index + 1}{delimiter}{block}"
            enumerated_blocks.append(enumerated_block)
    
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(enumerated_blocks))
        f.write('\n\n')  # Добавляем пустую строку в конце для разделения новых данных

def process_files():
    enumerate_and_save_data('data_first_variant.csv', delimiter='\n')
    enumerate_and_save_data('data_second_variant.csv', delimiter='; ')

# Запуск функции
process_files()


# функция ввода данных
def input_data():
    name = name_data() # функция имя
    surname = surname_data() # функция фамилия
    phone = phone_data() # функция телефон
    address = address_data() # функция адрес
    var = int(input(f"В каком формате записать данные \n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address} \n\n"
    f"2 Вариант: \n"
    f" {name};{surname};{phone};{address} \n"
    f"Выберите вариант: "))
    
        # обработчик ошибок
    while var != 1 and var != 2:
        print("Неправильный ввод ")
        var = int(input('Введите число '))
    
    if var == 1: # делаем проверку
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f: # открываем файл для записи
            f.write(f"{name}\n{surname}\n{phone}\n{address} \n\n") # и добавляем запись
    
    if var == 2: # делаем проверку
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f: # открываем файл для записи
            f.write(f"{name}; {surname}; {phone}; {address} \n\n") # и добавляем запись

# функция вывода данных
def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f: # открываем файл для чтения
        data_first = f.readlines() 
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1: # если равно \n или равно последней записи
                data_first_list.append(''.join(data_first[j:i+1])) # преобразовав список в строку, добавляем элементы с сомощью срезов
                j = i
        
        print(''.join(data_first))
    
    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f: # открываем файл для чтения
        data_second = f.readlines()
        print(*data_second)


# функция удаления данных
def delete_data(file_name, delimiter='\n'):
    if not os.path.exists(file_name):
        print(f"Файл {file_name} не найден.")
        return

    index_to_delete = int(input(f"Введите индекс записи для удаления из {file_name}: "))
    
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.read()
    
    blocks = data.strip().split('\n\n')
    updated_blocks = []

    for block in blocks:
        if block.strip():
            lines = block.strip().split(delimiter)
            if re.match(r'^\d+$', lines[0]) and int(lines[0]) == index_to_delete:
                continue  # Пропускаем блок с указанным индексом
            updated_blocks.append(block)
    
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(updated_blocks))
        f.write('\n\n')  # Добавляем пустую строку в конце для разделения новых данных

    # Перенумеруем оставшиеся блоки
    enumerate_and_save_data(file_name, delimiter)

# Пример использования:
# delete_data('data_first_variant.csv', delimiter='\n')
# delete_data('data_second_variant.csv', delimiter='; ')

#input_data()
#print_data()