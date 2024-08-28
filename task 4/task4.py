def read_data(filename):
    """Чтение координат точек из файла."""
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            numbers.append(int(line))
    return numbers

def min_moves_to_equal(nums):
    # Сортируем массив
    nums.sort()
    print(nums)
    # Находим медиану
    median = nums[len(nums) // 2]
    print(median)
    # Считаем количество шагов для приведения всех элементов к медиане
    moves = sum(abs(num - median) for num in nums)
    
    return moves

while True:
    numbers_path = (input("Введите абсолютный пути к файлу numbers.txt: "))

    try:
        numbers_data = read_data(numbers_path)
        print(numbers_data)
    except:
        print("Пожалуйста, проверьте корректность введенных данных в файле!")
    else:
        break


print(min_moves_to_equal(numbers_data))