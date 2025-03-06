import json

FILE = 'db.json'

# Открываем файл и считываем его содержимое
with open(FILE, 'r', encoding='utf-8') as file:
    json_data = file.read()

# Подсчитываем количество символов
symbol_count = len(json_data)

# Выводим результат
print(f"Symbol count in file '{FILE}': {symbol_count}")