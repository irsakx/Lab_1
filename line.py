# Начальная база данных квартир для демонстрации
database = [
    {'rooms': 2, 'floor': 5, 'area': 55.0, 'address': 'ул. Ленина, 10, кв. 25'},
    {'rooms': 3, 'floor': 7, 'area': 72.5, 'address': 'пр. Мира, 45, кв. 112'},
    {'rooms': 1, 'floor': 2, 'area': 38.0, 'address': 'ул. Садовая, 3, кв. 8'},
    {'rooms': 2, 'floor': 5, 'area': 58.2, 'address': 'ул. Парковая, 22, кв. 41'}
]

# Основной цикл программы
while True:
    # Вывод меню
    print("\n--- Бюро обмена квартир ---")
    print("1. Подать заявку на обмен")
    print("2. Показать все доступные варианты")
    print("3. Выход")
    
    choice = input("Выберите действие: ")

    # Обработка выбора пользователя
    if choice == '1':
        print("\n--- Ввод новой заявки ---")
        try:
            # Получение и валидация данных от пользователя
            req_rooms = int(input("Количество комнат: "))
            req_floor = int(input("Этаж: "))
            req_area = float(input("Площадь (кв.м): "))
            req_address = input("Адрес: ")

            new_request = {
                'rooms': req_rooms,
                'floor': req_floor,
                'area': req_area,
                'address': req_address
            }

            match_found = False
            item_to_remove = None

            # Поиск подходящего варианта в базе данных
            for item in database:
                # Проверка совпадения комнат и этажа
                if item['rooms'] == new_request['rooms'] and item['floor'] == new_request['floor']:
                    # Проверка площади в пределах 10%
                    area_diff = abs(item['area'] - new_request['area'])
                    if area_diff <= (new_request['area'] * 0.10):
                        print("\nНайден подходящий вариант для обмена:")
                        print(f"Адрес: {item['address']}, Комнат: {item['rooms']}, Этаж: {item['floor']}, Площадь: {item['area']}")
                        item_to_remove = item
                        match_found = True
                        break # Прерываем цикл после нахождения первого совпадения
            
            # Обработка результата поиска
            if match_found:
                database.remove(item_to_remove)
                print("Данный вариант удален из картотеки.")
            else:
                database.append(new_request)
                print("\nПодходящих вариантов не найдено. Ваша заявка добавлена в картотеку.")

        except ValueError:
            print("\nОшибка ввода! Количество комнат, этаж и площадь должны быть числами.")

    elif choice == '2':
        print("\n--- Текущая картотека квартир ---")
        if not database:
            print("Картотека пуста.")
        else:
            # Вывод всех записей в базе
            for idx, item in enumerate(database, 1):
                print(f"{idx}. Адрес: {item['address']}, Комнат: {item['rooms']}, Этаж: {item['floor']}, Площадь: {item['area']}")

    elif choice == '3':
        print("Завершение работы программы.")
        break

    else:
        print("\nНеверный выбор. Пожалуйста, введите число от 1 до 3.")
