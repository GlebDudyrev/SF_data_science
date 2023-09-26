"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

# количество попыток
count = 0

# цикл, в котором угадывают число
while True:
    # увеличиваем количество попыток
    count += 1
    # угадываем число
    predict_number = int(input("Угадай число от 1 до 100: "))
    
    # проверяем угадали или нет
    if predict_number < number:
        print("Число должно быть больше")
    elif predict_number > number:
        print("Число доллжно быть меньше")
    else:
        print(f"Вы угадали число! Это число = {number} за {count}")
        # выход из цикла
        break