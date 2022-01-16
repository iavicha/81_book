"""
This is my version of game Bagels

 © Ilia Vetchinin

 ivetchinin@gmail.com

"""

import random

clui = random.randint(99, 1000)

number_of_tries = 10

try_ = 0

version_ = ...


def enter(error=False):
    global version_
    if not error:
        version_ = input("Ведите Ваш вариант\n")
    else:
        version_ = input("Ошибка ввода. Ведите Ваш вариант\n")

    if len(version_) != 3:
        enter(True)

    try:
        int(version_)

    except ValueError:
        enter(True)

    return version_


enter()

