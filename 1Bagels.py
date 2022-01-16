"""
This is my version of game Bagels
 © Ilia Vetchinin
 ivetchinin@gmail.com
"""

import random


NUMBER_OF_TRIES= 10
"""
NUMBER_OF_DIGITS max value = 10
"""

NUMBER_OF_DIGITS = 3



def start():
    print(f"Бейгл, дедуктивная логическая игра.\n Создано Ильей Ветчининым ivetchinin@gmail.com. \n\n "
          f"Я задумываю {NUMBER_OF_DIGITS} значную цифру. Попробуй угадать.\n "
          "Вот разбор хода игры.\n")
    gameEnginie(enter(), secretNumber())

def enter(error=False):
    global version_
    if not error:
        version_ = input("Ведите Ваш вариант\n")
    else:
        version_ = input("Ошибка ввода. Ведите Ваш вариант\n")

    if len(version_) != NUMBER_OF_DIGITS:
        enter(True)

    try:
        int(version_)

    except ValueError:
        enter(True)

    return version_

def secretNumber():
    secret = ''
    numbers = list('0123456789')
    random.shuffle(numbers)
    for i in range(NUMBER_OF_DIGITS):
        secret += str(numbers[i])
    return secret

def gameEnginie(version_, secret, PROGRESS = 0):
    pico = ''

    if version_ != secret and PROGRESS != NUMBER_OF_TRIES:
        for i in range(NUMBER_OF_DIGITS):
            if secret[i] == version_[i]:
                pico += "Pico "
        PROGRESS += 1
        if len(pico) != 0:
            print(f'You version {version_}\n{pico}')
            gameEnginie(enter(), secret, PROGRESS)
        else:
            print('Bronko')
            gameEnginie(enter(), secret, PROGRESS)

    if NUMBER_OF_TRIES == PROGRESS:
        y_n = input('You loose. D0 you want to try again?\n')
        list_of_yes = ['YES','Y','ДА','Д']
        if y_n.upper() in list_of_yes:
            gameEnginie(enter(), secretNumber())

    if version_ == secret:
        y_n = input('You win. D0 you want to try again?\n')
        list_of_yes = ['YES', 'Y', 'ДА', 'Д']
        if y_n.upper() in list_of_yes:
            gameEnginie(enter(), secretNumber())


if __name__ == '__main__':
    start()
