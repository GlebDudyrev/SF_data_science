"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number:int = 1) -> int:
    """Компьютер угадывает число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # счетчик попыток
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла
        
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): алгоритм угадывания

    Returns:
        int: Среднее число попыток
    """
    count_ls = [] # список количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size = 1000) # список чисел, которые будем угадывать
    
    for number in random_array:
        count_ls.append(random_predict(number)) # добавляем кол-во попыток в список
        
    score = int(np.mean(count_ls))  # считаем среднее количество попыток
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')


# RUN
if __name__ == '__main__':
    score_game(random_predict)
        
    