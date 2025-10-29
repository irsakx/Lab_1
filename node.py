def display_menu():
    """Выводит на экран главное меню программы."""
    print("\n--- Бюро обмена квартир ---")
    print("1. Подать заявку на обмен")
    print("2. Показать все доступные варианты")
    print("3. Выход")

def get_validated_request():
    """Запрашивает у пользователя данные, валидирует их и возвращает в виде словаря."""
    print("\n--- Ввод новой заявки ---")
    try:
        req_rooms = int(input("Количество комнат: "))
        req_floor = int(input("Этаж: "))
        req_area = float(input("Площадь (кв.м): "))
        req_address = input("Адрес: ")
        
        return {
            'rooms': req_rooms,
            'floor': req_floor,
            'area': req_area,
            'address': req_address
        }
    except ValueError:
        print("\nОшибка ввода! Количество комнат, этаж и площадь должны быть числами.")
        return None

def find_and_process_match(database, new_request):
    """Ищет подходящий вариант в базе, обрабатывает результат и возвращает найденный элемент."""
    for item in database:
        # Проверка совпадения комнат и этажа
        if item['rooms'] == new_request['rooms'] and item['floor'] == new_request['floor']:
            # Проверка площади в пределах 10%
            area_diff = abs(item['area'] - new_request['area'])
            if area_diff <= (new_request['area'] * 0.10):
                return item # Возвращаем найденный элемент
    return None # Если ничего не найдено

def display_database(database):
    """Выводит на экран все записи в картотеке."""
    print("\n--- Текущая картотека квартир ---")
    if not database:
        print("Картотека пуста.")
    else:
        for idx, item in enumerate(database, 1):
            print(f"{idx}. Адрес: {item['address']}, Комнат: {item['rooms']}, Этаж: {item['floor']}, Площадь: {item['area']}")

def main():
    """Главная функция, управляющая работой программы."""
    database = [
        {'rooms': 2, 'floor': 5, 'area': 55.0, 'address': 'ул. Ленина, 10, кв. 25'},
        {'rooms': 3, 'floor': 7, 'area': 72.5, 'address': 'пр. Мира, 45, кв. 112'},
        {'rooms': 1, 'floor': 2, 'area': 38.0, 'address': 'ул. Садовая, 3, кв. 8'},
        {'rooms': 2, 'floor': 5, 'area': 58.2, 'address': 'ул. Парковая, 22, кв. 41'}
    ]

    while True:
        display_menu()
        choice = input("Выберите действие: ")

        if choice == '1':
            request = get_validated_request()
            if request:
                matched_item = find_and_process_match(database, request)
                if matched_item:
                    print("\nНайден подходящий вариант для обмена:")
                    print(f"Адрес: {matched_item['address']}, Комнат: {matched_item['rooms']}, Этаж: {matched_item['floor']}, Площадь: {matched_item['area']}")
                    database.remove(matched_item)
                    print("Данный вариант удален из картотеки.")
                else:
                    database.append(request)
                    print("\nПодходящих вариантов не найдено. Ваша заявка добавлена в картотеку.")
        
        elif choice == '2':
            display_database(database)
        
        elif choice == '3':
            print("Завершение работы программы.")
            break
            
        else:
            print("\nНеверный выбор. Пожалуйста, введите число от 1 до 3.")

if __name__ == "__main__":
    main()
