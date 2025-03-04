import json

# Открываем файл и считываем его содержимое
with open('db.json', 'r', encoding='utf-8') as file:
    json_data = file.read()

# Подсчитываем количество символов
symbol_count = len(json_data)

# Выводим результат
print(f"Количество символов в файле 'db.json': {symbol_count}")