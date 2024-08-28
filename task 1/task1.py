def generate_intervals(n, m):
    array = list(range(1, n + 1))
    intervals = []
    index = 0
    
    while True:
        interval = []
        for j in range(m):
            interval.append(array[(index + j) % n])
        
        intervals.append(interval)
        index = (index + m - 1) % n  # Смещаемся на конец текущего интервала
        
        if interval[-1] == array[0]:
            break
    
    # Извлекаем путь
    path = []
    for interval in intervals:
        path.append(interval[0])

    return intervals, path


while True:
    user_input = (input("Введите размер массива(n) и длину интервала(m): ").lower()).split()
    
    if len(user_input) > 2 or len(user_input) == 0:
        print("Введите ровно два аргумента или exit для выхода.")
        continue

    if "exit" in user_input:
        print("Программа завершена.")
        exit()
    try:
        n, m = user_input
        
        n = int(n)
        m = int(m)
    except:
        print("Пожалуйста, введите два числа или exit для выхода!")
    else:
        if m>n:
            print("Длина интервала не может быть больше размера массива")
        else:
            break

intervals, path = generate_intervals(n, m)

print(f"Полученный путь: {''.join(map(str, path))}.")