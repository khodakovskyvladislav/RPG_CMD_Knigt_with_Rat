# import random
import entities.player

print(entities.player.__file__)

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