import csv

# Создаем список с данными о наградах
game_awards = [
    {"game": "Dragon Age: Inquisition", "award": "Game of the Year", "year": 2014},
    {"game": "The Witcher 3: Wild Hunt", "award": "Game of the Year", "year": 2015},
    {"game": "Overwatch", "award": "Game of the Year", "year": 2016},
    {"game": "The Legend of Zelda: Breath of the Wild", "award": "Game of the Year", "year": 2017},
    {"game": "God of War", "award": "Game of the Year", "year": 2018},
    {"game": "Sekiro: Shadows Die Twice", "award": "Game of the Year", "year": 2019},
    {"game": "The Last of Us Part II", "award": "Game of the Year", "year": 2020},
    {"game": "It Takes Two", "award": "Game of the Year", "year": 2021},
    {"game": "Elden Ring", "award": "Game of the Year", "year": 2022},
]


with open('game_awards.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["game", "award", "year"])
    writer.writeheader()
    writer.writerows(game_awards)


with open('game_awards.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    sorted_games = sorted(reader, key=lambda row: row['game'])


for game in sorted_games:
    print(game['game'], game['award'], game['year'])