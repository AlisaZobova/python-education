"""Implementation of the 'hangman' game"""
from colorama import init
from colorama import Fore, Style
import game_functions
init()

command = input("ВАС ПРИВЕТСТВУЕТ ИГРА 'ВИСЕЛИЦА'.\n"
                "ВВЕДИТЕ: 1 - ДЛЯ НАЧАЛА ИГРЫ, 2 - ДЛЯ ВЫХОДА.\n")

while command:

    if command == '1':
        current_word = game_functions.get_new_word()
        start_word = list("_" * len(current_word))
        health_points = 8
        a = ord('а')
        all_let = list(''.join([chr(i).upper() for i in range(a, a + 32)]))
        wrong_let = []
        used_let = []
        while health_points > 0 and "_" in start_word:
            health_points = game_functions.main_func(
                health_points, start_word, all_let, used_let, current_word, wrong_let)
        else:
            command = game_functions.get_command_after_game(start_word, current_word, health_points)

    if command == '2':
        with open("used_words", 'w') as u_w:
            u_w.write("")
        print(Fore.YELLOW + "СПАСИБО ЗА ИГРУ. ХОРОШЕГО ДНЯ!" + Style.RESET_ALL)
        break

    if command == '3':
        try:
            with open("used_words", 'r') as w:
                for line in w:
                    print(line.rstrip('\n'))
            command = input("\nВВЕДИТЕ: 1 - ДЛЯ НОВОЙ ИГРЫ, 2 - ДЛЯ ВЫХОДА, 3 - ДЛЯ ПРОСМОТРА ПРОШЛЫХ СЛОВ.\n")
        except Exception as e:
            print(e)

    else:
        print(Fore.RED + "\nНЕКОРРЕКТНАЯ КОМАНДА." + Style.RESET_ALL)
        command = input("\nВВЕДИТЕ: 1 - ДЛЯ НОВОЙ ИГРЫ, 2 - ДЛЯ ВЫХОДА, 3 - ДЛЯ ПРОСМОТРА ПРОШЛЫХ СЛОВ.\n")
