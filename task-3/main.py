import json
import os

operations = 0  # счётчик операций
filename = "flowers.json"


# ---------- загрузка данных ----------
def load_data():
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


# ---------- сохранение данных ----------
def save_data(data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


while True:
    print("\n======= МЕНЮ =======")
    print("1. Вывести все записи")
    print("2. Вывести запись по id")
    print("3. Добавить запись")
    print("4. Удалить запись по id")
    print("5. Выйти из программы")
    print("====================")

    choice = input("Выберите пункт меню: ").strip()
    data = load_data()

    # ---------- 1. все записи ----------
    if choice == "1":
        if not data:
            print("Записей нет.")
        else:
            print("\n===== ВСЕ ЗАПИСИ =====")
            for i, item in enumerate(data, start=1):
                print(
                    f"[{i}] id: {item['id']}, "
                    f"name: {item['name']}, "
                    f"latin_name: {item['latin_name']}, "
                    f"is_red_book_flower: {item['is_red_book_flower']}, "
                    f"price: {item['price']}"
                )
        operations += 1

    # ---------- 2. поиск по id ----------
    elif choice == "2":
        try:
            find_id = int(input("Введите id: "))
        except ValueError:
            print("Некорректный id.")
            continue

        for index, item in enumerate(data, start=1):
            if item["id"] == find_id:
                print("\n===== НАЙДЕНО =====")
                print(f"Позиция: {index}")
                print(f"id: {item['id']}")
                print(f"name: {item['name']}")
                print(f"latin_name: {item['latin_name']}")
                print(f"is_red_book_flower: {item['is_red_book_flower']}")
                print(f"price: {item['price']}")
                break
        else:
            print("Запись не найдена!")

        operations += 1

    # ---------- 3. добавить ----------
    elif choice == "3":
        try:
            new_id = max([i["id"] for i in data], default=0) + 1
            name = input("Название: ").strip()
            latin = input("Латинское название: ").strip()
            redbook = input("Краснокнижный? (да/нет): ").lower() in ("да", "yes", "true", "1")
            price = float(input("Цена: "))
        except ValueError:
            print("Ошибка ввода данных!")
            continue

        data.append({
            "id": new_id,
            "name": name,
            "latin_name": latin,
            "is_red_book_flower": redbook,
            "price": price
        })

        save_data(data)
        print("Запись добавлена.")
        operations += 1

    # ---------- 4. удалить ----------
    elif choice == "4":
        try:
            del_id = int(input("Введите id для удаления: "))
        except ValueError:
            print("Некорректный id!")
            continue

        new_data = [item for item in data if item["id"] != del_id]

        if len(new_data) == len(data):
            print("Запись не найдена!")
        else:
            save_data(new_data)
            print("Запись удалена.")
            operations += 1

    # ---------- 5. выход ----------
    elif choice == "5":
        print("\n===================================")
        print("Вы завершили программу.")
        print("Количество операций:", operations)
        print("===================================")
        break

    else:
        print("Неверный пункт меню!")