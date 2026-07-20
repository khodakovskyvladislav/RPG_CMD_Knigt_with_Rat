from menuchoice.newgame import choose_class
from loop.gameloop import game_loop

def main_menu():
    while True:
        print("=== TERMINAL LEGENDS ===")
        print("1. Новая игра")
        print("2. Загрузить")
        print("3. Настройки")
        print("4. Авторы")
        print("5. Выход")

        choice = input("> ")

        if choice == "1":
            hero = choose_class()
            if hero:
                game_loop(hero)
                
        elif choice == "2":
            print("Загрузка")

        elif choice == "3":
            print("Настройки")

        elif choice == "4":
            print("Авторы")

        elif choice == "5":
            print("До свидания")
            break

        else:
            print("Неизвестная команда")


main_menu() #
