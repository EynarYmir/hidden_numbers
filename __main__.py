"""

Создайте программу, которая случайным образом выбирает загаданное число.
 У пользователя будет несколько шансов, причем при каждой неправильной попытке
он будет получать подсказку от компьютера, сообщающую о том, в какую сторону
 (большую или меньшую) он ошибся.

"""

import random
from termcolor import colored


def __main__():
    hidden_numb = random.randint(1, 1000)
    print(str(hidden_numb))
    attempts = 0
    print(colored("Угадайте загаданное число.\n", 'yellow', attrs=['underline']))

    while attempts < 5:
        attempt = input("Введите число: ")
        if int(attempt) == hidden_numb:
            print(colored("Поздравляю, вы угадали число!!!", 'red'))
            game = input("Сыграть еще раз?")
            if game.lower() == 'y' or game.lower() == 'yes':
                attempts = -1
            else:
                break
        elif int(attempt) < hidden_numb:
            print(colored("Загаданное число больше введенного числа", 'yellow'))
            attempt = input("Попробуйте еще раз.")
        elif int(attempt) > hidden_numb:
            print(colored("Загаданное число меньше введеного числа", 'yellow'))
            attempt = input("Попробуйте еще раз.")
        attempts += 1


if __name__ == "__main__":
    __main__()
