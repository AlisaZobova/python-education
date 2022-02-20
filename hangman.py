"""Implementation of the 'hangman' game"""
from colorama import init
from colorama import Fore, Style
import game_functions
init()

command = input("ВАС ПРИВЕТСТВУЕТ ИГРА 'ВИСЕЛИЦА'.\n"
                "ВВЕДИТЕ: 1 - ДЛЯ НАЧАЛА ИГРЫ, 2 - ДЛЯ ВЫХОДА.\n")

while command:
    try:
        if command == '1':
            command = game_functions.do_command1()

        if command == '2':
            game_functions.do_command2()
            break

        if command == '3':
            command = game_functions.do_command3()

        else:
            raise ValueError(Fore.RED + "\nНЕКОРРЕКТНАЯ КОМАНДА." + Style.RESET_ALL)

    except ValueError as err:
        print(err)
        command = input("\nВВЕДИТЕ: 1 - ДЛЯ НОВОЙ ИГРЫ, 2 - ДЛЯ ВЫХОДА, "
                        "3 - ДЛЯ ПРОСМОТРА ПРОШЛЫХ СЛОВ.\n")
