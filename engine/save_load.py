import json

class Game_state:
    def __init__(self, hero_name):
        self.hero_name = hero_name
        self.location = "Город"
        self.gold = 100

    # 1. МЕТОД ДЛЯ СОХРАНЕНИЯ
    def save_game(self, filename="save.json"):
        # Создаем обычный словарь с данными
        data_to_save = {
            "hero_name": self.hero_name,
            "location": self.location,
            "gold": self.gold
        }
        
        # Открываем файл для записи (w) и сохраняем JSON
        with open(filename, "w", encoding="utf-8") as file:
            # ensure_ascii=False нужен, чтобы русский текст не превратился в кракозябры
            # indent=4 делает красивую структуру с отступами
            json.dump(data_to_save, file, ensure_ascii=False, indent=4)
        print("Игра успешно сохранена!")

    # 2. МЕТОД ДЛЯ ЗАГРУЗКИ
    def load_game(self, filename="save.json"):
        try:
            # Открываем файл для чтения (r)
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file) # Превращаем текст JSON в словарь Python
                
            # Обновляем состояние нашего класса из загруженного словаря
            self.hero_name = data["hero_name"]
            self.location = data["location"]
            self.gold = data["gold"]
            print("Игра успешно загружена!")
            
        except FileNotFoundError:
            print("Файл сохранения не найден! Начинаем новую игру.")
