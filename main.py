import json
import random


# Функция Меню
def menu():
    print('----------------------------')
    print('1. Добавить книгу')
    print('2. Удалить книгу')
    print('3. Поиск')
    print('4. Все книги')
    print('5. Изменение статуса книги')
    print('6. Выход')
    print('----------------------------')
    try:
        num = int(input('[?] Ввод: '))
        if num == 1:
            add()
        elif num == 2:
            delete()
        elif num == 3:
            search()
        elif num == 4:
            all_books()
        elif num == 5:
            edit_status()
        elif num == 6:
            exit()
        else:
            print('[?] Такого пункта меню нету!')
            menu()
    except Exception:
        print('[?] Ошибка!')
        menu()


# Функция добавления книг в библ.
def add():
    print('----------------------------')
    print('1. Назад')
    print('2. Ввод книги')
    print('----------------------------')
    try:
        num = int(input('[?] Ввод: '))
        if num == 1:
            menu()
        elif num == 2:
            title = input('[?] Введите названеи книги: ')
            author = input('[?] Введите автора книги: ')
            year = input('[?] Введите год книги: ')
            id = random.randint(1, 1000)

            # Открываем json файл
            with open('package.json', 'r', encoding='utf-8') as file:
                loaded_data = json.load(file)

            # Добавляем новую книгу
            loaded_data.append({
                "id": id,
                "title": title,
                "author": author,
                "year": year,
                "status": "В наличии"
            })

            # Записывваем в json файл
            with open('package.json', 'w', encoding='utf-8') as file:
                json.dump(loaded_data, file, ensure_ascii=False, indent=4)
            menu()
        else:
            print('[?] Такого пункта меню нету!')
            menu()
    except Exception:
        print('[?] Ошибка!')
        menu()


# Функция удаления книг из библ.
def delete():
    print('----------------------------')
    print('1. Назад')
    print('2. Удалить книгу')
    print('----------------------------')
    try:
        num = int(input('[?] Ввод: '))
        if num == 1:
            menu()
        elif num == 2:
            deletes = int(input('[?] Введите ID книги: '))
            # Открываем json файл
            with open('package.json', 'r', encoding='utf-8') as file:
                loaded_data = json.load(file)
            nums = len(loaded_data)
            # Поиск книги по ID и удаление
            for num in range(0, nums):
                if deletes == loaded_data[num]['id']:
                    del loaded_data[num]
                    print('[?] Книга удалена!')
                    # Запись json без удаленной книги
                    with open('package.json', 'w', encoding='utf-8') as file:
                        json.dump(loaded_data, file, ensure_ascii=False, indent=4)
            print('[?] Такой книге нету!')
            menu()
        else:
            print('[?] Такого пункта меню нету!')
            menu()
    except Exception:
        print('[?] Ошибка!')
        menu()


# Функция поиска книг в библ.
def search():
    print('----------------------------')
    print('1. Назад')
    print('2. Поиск')
    print('----------------------------')
    try:
        num = int(input('[?] Ввод: '))
        if num == 1:
            menu()
        elif num == 2:
            print('----------------------------')
            print('1. Название')
            print('2. Автор')
            print('3. Год')
            print('----------------------------')
            categ = int(input('[?] Ввод: '))
            # Поиск книги по title
            if categ == 1:
                title = input('[?] Введите название книги: ')
                # Открываем json файл
                with open('package.json', 'r', encoding='utf-8') as file:
                    loaded_data = json.load(file)
                nums = len(loaded_data)
                # Циклом находим нужную книгу по title, если такой книги нету в библ. то возвращает к стартовому меню
                for num in range(0, nums):
                    if title == loaded_data[num]['title']:
                        print('============================')
                        print('ID:', loaded_data[num]['id'])
                        print('Название:', loaded_data[num]['title'])
                        print('Автор:', loaded_data[num]['author'])
                        print('Год:', loaded_data[num]['year'])
                        print('Статус:', loaded_data[num]['status'])
                        print('============================')
                        menu()
                    print('[?] Такой книге нету!')
                    menu()
            # Поиск книги по author
            elif categ == 2:
                author = input('[?] Введите Автора книги: ')
                # Открываем json файл
                with open('package.json', 'r', encoding='utf-8') as file:
                    loaded_data = json.load(file)
                nums = len(loaded_data)
                # Циклом находим нужную книгу по author, если такой книги нету в библ. то возвращает к стартовому меню
                for num in range(0, nums):
                    if author == loaded_data[num]['author']:
                        print('============================')
                        print('ID:', loaded_data[num]['id'])
                        print('Название:', loaded_data[num]['title'])
                        print('Автор:', loaded_data[num]['author'])
                        print('Год:', loaded_data[num]['year'])
                        print('Статус:', loaded_data[num]['status'])
                        print('============================')
                        menu()
                    print('[?] Такой книге нету!')
                    menu()
            # Поиск книги по author
            elif categ == 3:
                year = input('[?] Введите год: ')
                # Открываем json файл
                with open('package.json', 'r', encoding='utf-8') as file:
                    loaded_data = json.load(file)
                nums = len(loaded_data)
                # Циклом находим нужную книгу по year, если такой книги нету в библ. то возвращает к стартовому меню
                for num in range(0, nums):
                    if year == loaded_data[num]['year']:
                        print('============================')
                        print('ID:', loaded_data[num]['id'])
                        print('Название:', loaded_data[num]['title'])
                        print('Автор:', loaded_data[num]['author'])
                        print('Год:', loaded_data[num]['year'])
                        print('Статус:', loaded_data[num]['status'])
                        print('============================')
                        menu()
                    print('[?] Такой книге нету!')
                    menu()
            else:
                search()
        else:
            print('[?] Такого пункта меню нету!')
            menu()
    except Exception:
        print('[?] Ошибка!')
        menu()


# Функция показа всех книг в библ.
def all_books():
    try:
        # Открываем json файл
        with open('package.json', 'r', encoding='utf-8') as file:
            loaded_data = json.load(file)
        nums = len(loaded_data)
        # Цикл для вывода всех книг
        for num in range(0, nums):
            print('============================')
            print('ID:', loaded_data[num]['id'])
            print('Название:', loaded_data[num]['title'])
            print('Автор:', loaded_data[num]['author'])
            print('Год:', loaded_data[num]['year'])
            print('Статус:',loaded_data[num]['status'])
            print('============================')
        menu()
    except Exception:
        print('[?] Ошибка!')
        menu()


# Функция изменения статуса книги в библ.
def edit_status():
    print('----------------------------')
    print('1. Назад')
    print('2. Изменить статус')
    print('----------------------------')
    try:
        num = int(input('[?] Ввод: '))
        if num == 1:
            menu()
        elif num == 2:
            edit = int(input('[?] Введите ID книги: '))
            # Открываем json файл
            with open('package.json', 'r', encoding='utf-8') as file:
                loaded_data = json.load(file)
            nums = len(loaded_data)
            # Циклом находим нужную книгу по ID, если такой книги нету в библ. то возвращает к стартовому меню
            for num in range(0, nums):
                if edit == loaded_data[num]['id']:
                    print(f'[?] Статус книги на данный момент', loaded_data[num]["status"])
                    status = input('Введите статус: ')
                    loaded_data[num]['status'] = status # Меняется статус книги
                    print('[?] Статус изменён!')
                    with open('package.json', 'w', encoding='utf-8') as file:
                        json.dump(loaded_data, file, ensure_ascii=False, indent=4)
            menu()
        else:
            print('[?] Такого пункта меню нету!')
            menu()
    except Exception:
        print('[?] Ошибка!')
        menu()


# Выход
def exit():
    quit()


menu()