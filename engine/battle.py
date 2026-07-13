"""
battle.py
Отвечает только за проведение боя.
"""

import random


class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start(self):  # """Главный цикл боя."""
        print("Бой начался!")
        
        pass

    def player_turn(self):
        """Ход игрока."""
        pass

    def enemy_turn(self):
        """Ход врага."""
        pass

    def choose_action(self):
        """Выбор действия игроком."""
        pass

    def attack(self, attacker, defender):
        """Обычная атака."""
        pass

    def defence(self, character):
        """Защитная стойка."""
        pass

    def evasion(self, character):
        """Попытка уклониться."""
        pass

    def escape(self):
        """Попытка сбежать."""
        pass

    def calculate_damage(self, attacker, defender):
        """Расчет урона."""
        pass

    def check_hit(self, chance):
        """Проверка успешности действия."""
        pass

    def is_battle_over(self):
        """Проверяет, закончился ли бой."""
        pass

    def print_status(self):
        """Вывод HP игрока и врага."""
        pass