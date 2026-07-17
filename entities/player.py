# сделать клас создания персонажей. базовые первые три это воин маг и лучник. потом можно добавить других. добваь анотации
class Player:
    def __init__(self, name: str, player_class: str, level: int = 1, experience: int = 0, health: int = 100, mana: int = 50, strength: int = 10, agility: int = 10, intelligence: int = 10):
        self.name = name
        self.player_class = player_class
        self.level = level
        self.experience = experience
        self.health = health
        self.mana = mana
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence

    def level_up(self):
        self.level += 1
        self.health += 20
        self.mana += 10
        self.strength += 2
        self.agility += 2
        self.intelligence += 2

    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= 100:
            self.level_up()
            self.experience -= 100

    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Class: {self.player_class}")
        print(f"Level: {self.level}")
        print(f"Experience: {self.experience}/100")
        print(f"Health: {self.health}")
        print(f"Mana: {self.mana}")
        print(f"Strength: {self.strength}")
        print(f"Agility: {self.agility}")
        print(f"Intelligence: {self.intelligence}")