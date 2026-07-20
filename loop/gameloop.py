def game_loop(hero):
    while True:
        print("\n=== ГОРОД ===")
        print(f"Добро пожаловать, {hero.name}")
        print("1. Выйти на карту")
        print("2. Инвентарь")
        print("3. Персонаж")
        print("4. Выход в главное меню")

        choice = input("> ")

        if choice == "1":
            print("Вы вышли на карту")

        elif choice == "2":
            print("Инвентарь")

        elif choice == "3":
            hero.display_stats()

        elif choice == "4":
            break