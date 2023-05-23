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
        data = file.read()
    result = search(data, data_searсh)    
    print(result)


def search(book: str, info: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    #return [contact for contact in book if info.lower() in contact.lower()]
    return list(filter(lambda contact: info.lower() in contact.lower(), book))    
