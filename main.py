from menuchoice.newgame import choose_class


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
                print(f"Вы создали персонажа: {hero.name},\
                     класс: {hero.player_class}")
                # Здесь можно добавить дальнейшую логику игры с созданным персонажем
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
