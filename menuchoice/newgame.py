# нужно выводить меню выбора персонажа текстом, а не просто цифрами, чтобы игрок понимал, что он выбирает. напишы choice == "4" вернуться в главное меню
from entities.player import Player


def choose_class():
    print("Выберите класс")
    print("1. Воин")
    print("2. Маг")
    print("3. Лучник")
    print("4. Вернуться в главное меню")
    choice = input("> ")

    if choice == "1":
        print("Вы выбрали воина")
        return Player("Воин", "Воин", 1, 0, 100, 50, 10, 10, 10)

    elif choice == "2":
        print("Вы выбрали мага")
        return Player("Маг", "Маг", 1, 0, 80, 100, 5, 15, 20)

    elif choice == "3":
        print("Вы выбрали лучника")
        return Player("Лучник", "Лучник", 1, 0, 90, 60, 8, 20, 15)

    elif choice == "4":
        print("Возвращаемся в главное меню")
        return None

    else:
        print("Неизвестная команда")
        return None