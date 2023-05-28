def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone_num = int(input('Введите тел: '))
    with open('book.txt', 'a', encoding='utf-8') as book:
        book.write(f'{fio} | {phone_num}\n')
        

def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    data_searсh = input("Введите что ищем: ")
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = [i.strip() for i in file]
    result = search(data, data_searсh)
    print('Результаты:')
    for i in range(len(result)):    
        print(f'{i+1}. {result[i]}')


def search(book: list[str], info: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    #return [contact for contact in book if info.lower() in contact.lower()]
    return list(filter(lambda contact: info.lower() in contact.lower(), book))    

def del_func():
    data_searсh = input("Введите что ищем: ") 
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = [i.strip() for i in file]
    print(data)
    del_list = search(data, data_searсh)
    print(del_list)
    count = len(del_list)
    if count == 0:
        print("Ничего не найдено")
    elif count == 1:
        data.remove(del_list[0])
        print(data)
    elif count > 1:
        for i in range(len(del_list)):
            print(f'{i+1}. {del_list[i]}')
        new_search = int(input("Уточните какой контакт хотите удалить?: "))
        if new_search > 0 and count+1 > new_search:
            print(f'Удаляем [{del_list[new_search-1]}]')
            data_searсh= del_list[new_search-1]
            data.remove(del_list[new_search-1])
        else:
            print("Указано неверноe значение для редактирования")
    with open('book.txt', 'w', encoding='utf-8') as file:
        for i in range(len(data)):
            with open('book.txt', 'a', encoding='utf-8') as f:
                f.write(f'{data[i]}\n') 
        print(f'Запись Удалена!')



def change():
    data_searсh = input("Введите что ищем: ") 
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = [i.strip() for i in file]
    change_list = search(data, data_searсh)
    count = len(change_list)
    if count == 0:
        print("Ничего не найдено")
    elif count == 1:
        print(change_list[0])
        new_fio = input('Введите ФИО: ')
        new_phone_num = int(input('Введите тел: '))
        data[data.index(change_list[0])] = str(f'{new_fio} {new_phone_num}')
    elif count > 1:
        for i in range(len(change_list)):
            print(f'{i+1}. {change_list[i]}')
        new_search = int(input("Уточните какой контакт хотите заменить?: "))
        if new_search > 0 and count+1 > new_search:
            print(f'Изменяем [{change_list[new_search-1]}]')
            zamena = change_list[new_search-1]
            new_fio = input('Введите ФИО: ')
            new_phone_num = int(input('Введите тел: '))
            data[data.index(zamena)] = str(f'{new_fio} {new_phone_num}')
        else:
            print("Указано неверноe значение для редактирования")
    with open('book.txt', 'w', encoding='utf-8') as file:
        for i in range(len(data)):
            with open('book.txt', 'a', encoding='utf-8') as f:
                f.write(f'{data[i]}\n') 
        print(f'Запись отредактирована!')  