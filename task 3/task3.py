import json

def fill_values(tests, values_dict):
    """Рекурсивно заполняем поле value в tests.json на основе values.json."""
    for test in tests:
        test_id = test['id']
        if test_id in values_dict:
            test['value'] = values_dict[test_id]
        if 'values' in test:
            fill_values(test['values'], values_dict)

def read_data(path, data):
    if data == 0:
        with open(path, "r") as read_file:
            return json.load(read_file)
    else:
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

while True:
    user_input = (input("Введите три аргумента(абсолютные пути к файлам values.json, tests.json, report.json) через запятую: ")).split(", ")
    
    if len(user_input) > 3 or len(user_input) == 0:
        print("Введите ровно два аргумента или exit для выхода.")
        continue

    if "exit" in user_input:
        print("Программа завершена.")
        exit()
    try:
        values_path, tests_path, report_path = user_input
        values_data = read_data(values_path, 0)
        tests_data = read_data(tests_path, 0)

    except:
        print("Пожалуйста, проверьте корректность введенных данных в файлах!")
    else:
        break

# Преобразуем список значений в словарь для удобства поиска по id
values_dict = {item['id']: item['value'] for item in values_data['values']}

# Заполняем структуру tests данными из values
fill_values(tests_data['tests'], values_dict)

# Записываем результат в report.json
read_data(report_path, tests_data)
