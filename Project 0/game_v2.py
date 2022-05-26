'''Игра угадай число'''

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0  # initially counter value =0 (начальное значение счётчика)
    predict_number = 50  # initial prediction (начальное значение угадываемого числа)
    interval = 50  # prediction step (шаг изменения угадываемого числа)
    
    while True:
        count += 1  # count attempts (считаем каждую попытку)
        interval = round(interval*0.5)  # reducing the step (уменьшаем шаг изменения угадываемого числа)
        
        if predict_number > number:
            predict_number -= interval  # decreasing our prediction (уменьшаем угадываемое число на шаг)
                    
        elif predict_number < number:
            predict_number += interval  # increasing our prediction (увеличиваем угадываемое число на шаг)
            
        elif number == predict_number:
            break  # выход из цикла если угадали

    return count # return the number of attempts (возвращаем номер успешной попытки)


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм
 
    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(100)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))  # добавляем счётчик успешнх попыток в журнал

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток') 
    return(score) 

# RUN
if __name__ == '__main__':
    score_game(random_predict)