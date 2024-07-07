from logger import input_data, print_data

def interface():
    print("Добрый день! Вы попали на специальный бот-справочник от GeekBrains! \n 1 - записать данные. \n 2 - вывод данных. \n 3 - удалить данные.")
    command = int(input('Введите число '))
    
    # обработчик ошибок
    while command != 1 and command != 2 and command != 3:
        print("Неправильный ввод ")
        command = int(input('Введите число '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        delete_data()
  