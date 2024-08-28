import math

def is_point_in_circle(x_c, y_c, r, x_p, y_p):
    """Проверка, находится ли точка (x_p, y_p) внутри окружности с центром (x_c, y_c) и радиусом r."""
    distance = (x_p - x_c) ** 2 + (y_p - y_c) ** 2
    radius = r ** 2
    if distance == radius:
        return 0
    elif distance < radius:
        return 1
    else:
        return 2

def read_circle_data(filename):
    """Чтение данных окружности из файла."""
    with open(filename, 'r') as file:
        x_c, y_c = map(float, file.readline().strip().split())
        r = float(file.readline())
    return x_c, y_c, r

def read_points_data(filename):
    """Чтение координат точек из файла."""
    points = []
    with open(filename, 'r') as file:
        for line in file:
            x_p, y_p = map(float, line.strip().split())
            points.append((x_p, y_p))
    return points

while True:
    user_input = (input("Введите два аргумента(абсолютные пути к файлам circle.txt, dot.txt) через запятую: ")).split(", ")
    
    if len(user_input) > 2 or len(user_input) == 0:
        print("Введите ровно два аргумента или exit для выхода.")
        continue

    if "exit" in user_input:
        print("Программа завершена.")
        exit()
    try:
        circle_path, points_path = user_input
        x_c, y_c, r = read_circle_data(circle_path)
        points = read_points_data(points_path)

    except:
        print("Пожалуйста, проверьте корректность введенных данных в файлах!")
    else:
        break

# Проверка каждой точки
for (x_p, y_p) in points:
    print(is_point_in_circle(x_c, y_c, r, x_p, y_p))