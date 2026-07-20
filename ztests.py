# import random
# import entities.player

# print(entities.player.__file__)



# GAME_FIGHT_ENGINE



# def game():
#     # Характеристики персонажей
#     player_hp = 100
#     goblin_hp = 100
    
#     print("--- Битва: Рыцарь против Гоблина! ---")
    
#     while player_hp > 0 and goblin_hp > 0:
#         print(f"\nВаше здоровье: {player_hp} | Здоровье гоблина: {goblin_hp}")
#         print("Выберите действие:")
#         print("1 - Атаковать")
#         print("2 - Защита")
#         print("3 - Уклонение")
#         print("4 - Бросить бомбу")
        
#         choice = input("Ваш выбор (1/2/3/4): ")
        
#         # Логика хода гоблина (случайное действие)
#         goblin_action = random.choice(['attack', 'attack', 'nothing'])
        
#         # Обработка действий игрока
#         player_damage = 0
#         goblin_damage = 15
        
#         if choice == '1':
#             print("Вы нанесли удар мечом!")
#             goblin_hp -= 20
#         elif choice == '2':
#             print("Вы подняли щит, урон от гоблина будет снижен.")
#             goblin_damage = 5
#         elif choice == '3':
#             if random.random() > 0.5:
#                 print("Вы успешно уклонились от атаки!")
#                 goblin_damage = 0
#             else:
#                 print("Вы пытались уклониться, но споткнулись!")
#         elif choice == '4':
#             if random.random() > 0.5:
#                 print("Бабах!")
#                 goblin_hp -= 20
#             else:
#                 print("гоблин отбил бомбу и вы получили урон!")
#                 player_hp -= 10
#         else:
#             print("Неверный ввод, вы пропустили ход!")
            
#         # Урон от гоблина
#         if goblin_action == 'attack':
#             player_hp -= goblin_damage
#             print(f"Гоблин атакует и наносит {goblin_damage} урона!")
#         else:
#             print("Гоблин замешкался и пропустил ход.")

#     # Финал игры
#     if player_hp <= 0:
#         print("\nВы погибли... Гоблин победил!")
#     else:
#         print("\nПоздравляю! Вы победили гоблина!")

# if __name__ == "__main__":
#     game()



# JSON_TESTS



import json
import os

# Имя файла для сохранения
SAVE_FILE = "tavern_save.json"

# Начальное состояние игры (Обычный словарь Python)
game_data = {
    "tavern_name": "Пьяный Дракон",
    "gold": 150,
    "is_open": True,
    "menu": ["Эль", "Жареная курица"],
    "reputation": 4.5
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_status():
    print("=" * 40)
    print(f"📊 ТЕКУЩИЙ СЛОВАРЬ В PYTHON:")
    print(f"Название: {game_data['tavern_name']} | Золото: {game_data['gold']} | Открыто: {game_data['is_open']}")
    print(f"Меню: {game_data['menu']} | Репутация: {game_data['reputation']}")
    print("=" * 40)

def main():
    global game_data
    while True:
        clear_screen()
        show_status()
        
        print("📜 ВЫБЕРИ ДЕЙСТВИЕ ДЛЯ ИЗУЧЕНИЯ JSON:")
        print("1. Изменить данные в игре (Просто поменять переменные)")
        print("2. 💾 json.dump() — Сохранить игру в файл (Запись JSON)")
        print("3. 📂 json.load() — Загрузить игру из файла (Чтение JSON)")
        print("4. 🔍 json.dumps() — Посмотреть, как данные выглядят в виде строки JSON")
        print("5. 🧠 json.loads() — Превратить строку JSON обратно в словарь")
        print("0. Выход")
        
        choice = input("\nТвой ход (0-5): ")

        if choice == "1":
            # Модификация данных в Python
            game_data["gold"] += 50
            game_data["menu"].append("Эль")
            print("\n➕ Ты продал Эль! Золото увеличено, новое блюдо добавлено в меню.")
            input("\nНажми Enter, чтобы продолжить...")

        elif choice == "2":
            # json.dump() записывает данные напрямую В ФАЙЛ
            with open(SAVE_FILE, "w", encoding="utf-8") as f:
                json.dump(game_data, f, ensure_ascii=False, indent=4)
            print(f"\n💾 Сработало! Данные сохранены в файл '{SAVE_FILE}'.")
            print("Загляни в эту папку, там появился файл. Открой его через блокнот или VS Code!")
            input("\nНажми Enter, чтобы продолжить...")

        elif choice == "3":
            # json.load() читает данные ИЗ ФАЙЛА
            if os.path.exists(SAVE_FILE):
                with open(SAVE_FILE, "r", encoding="utf-8") as f:
                    game_data = json.load(f)
                print("\n📂 Успешно! Данные прочитаны из файла и загружены в игру.")
            else:
                print("\n❌ Файл сохранения еще не создан! Сначала выбери пункт 2.")
            input("\nНажми Enter, чтобы продолжить...")

        elif choice == "4":
            # json.dumps() (с буквой 's' -> string) не создает файл! 
            # Он просто превращает словарь в красивую строку текста.
            json_string = json.dumps(game_data, ensure_ascii=False, indent=4)
            print("\n🔍 Вот как твои данные выглядят внутри формата JSON (в виде текста):")
            print("-" * 30)
            print(json_string)
            print("-" * 30)
            print("Обрати внимание: True превратился в true, а списки взяты в строгие кавычки!")
            input("\nНажми Enter, чтобы продолжить...")

        elif choice == "5":
            # json.loads() (с буквой 's') берет СТРОКУ текста и делает из нее словарь
            raw_text = '{"tavern_name": "Новая Таверна", "gold": 999, "is_open": false, "menu": ["Вода"], "reputation": 1.0}'
            print("\n🧠 У нас есть сырой текст (строка) из другой игры:")
            print(raw_text)
            
            # Превращаем текст в объект Python
            game_data = json.loads(raw_text)
            print("\nПарсинг успешен! Строка превратилась в рабочий Python-словарь.")
            input("\nНажми Enter, чтобы продолжить...")

        elif choice == "0":
            print("\nУдачи в кодинге!")
            break
        else:
            print("\nНеверный ввод, попробуй еще раз.")
            input("\nНажми Enter...")

if __name__ == "__main__":
    main()
