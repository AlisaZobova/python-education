"""Functional of the game"""
import random
from colorama import init
from colorama import Fore, Style
init()


def get_new_word():
    """Get a new word for the game"""
    try:
        with open("hangman_words", 'r') as w:
            words = []
            for line in w:
                words.append(line.rstrip('\n'))
    except FileNotFoundError:
        print('Файл hangman_words не найден!')

    try:
        with open("used_words", 'r') as u_w:
            used_words = []
            for line in u_w:
                used_words.append(line.rstrip('\n'))

        with open("used_words", 'a') as list_u_w:
            game_words = set(words).symmetric_difference(set(used_words))
            current_word = random.choice(list(game_words))
            list_u_w.write(current_word + '\n')

        return current_word

    except FileNotFoundError:
        print('Файл used_words не найден!')


def main_func(health_points, start_word, all_let, used_let, current_word, wrong_let):
    """Main functionality"""
    make_man_picture(health_points)
    print(Fore.GREEN + '\nСЛОВО:' + Style.RESET_ALL, *start_word)
    print(Fore.YELLOW + f'''КОЛИЧЕСТВО ЖИЗНЕЙ: {Style.RESET_ALL}{health_points}''')
    letter = input("ВВЕДИТЕ БУКВУ: ").upper()

    while letter not in all_let:
        letter = input(Fore.RED + f'ЗАДАНО НЕКОРРЕКТНОЕ ЗНАЧЕНИЕ!\n{Style.RESET_ALL}'
                       f'ВВЕДИТЕ БУКВУ РУССКОГО АЛФАВИТА: ').upper()

    while letter in used_let:
        letter = input(Fore.RED + f'БУКВА УЖЕ ИСПОЛЬЗОВАЛАСЬ!{Style.RESET_ALL}\n'
                                  f'ВВЕДИТЕ ДРУГУЮ: ').upper()

    if letter in current_word:
        indexes = [i for i in range(len(current_word)) if current_word.startswith(letter, i)]
        for i in indexes:
            start_word[i] = letter

    else:
        health_points -= 1
        wrong_let.append(letter)

    print(Fore.RED + 'НЕУГАДАННЫЕ БУКВЫ:' + Style.RESET_ALL, *sorted(wrong_let))
    used_let.append(letter)

    return health_points


def do_command1():
    """Do 1-st command"""
    current_word = get_new_word()
    start_word = list("_" * len(current_word))
    health_points = 8
    a = ord('а')
    all_let = list(''.join([chr(i).upper() for i in range(a, a + 32)]))
    wrong_let = []
    used_let = []

    while health_points > 0 and "_" in start_word:
        health_points = main_func(
            health_points, start_word, all_let, used_let, current_word, wrong_let)
    else:
        command = get_command_after_game(start_word, current_word, health_points)

    return command


def do_command2():
    """Do 2-nd command"""
    with open("used_words", 'w') as u_w:
        u_w.write("")
    print(Fore.YELLOW + "СПАСИБО ЗА ИГРУ. ХОРОШЕГО ДНЯ!" + Style.RESET_ALL)


def do_command3():
    """Do 3-rd command"""
    try:
        with open("used_words", 'r') as w:
            for line in w:
                print(line.rstrip('\n'))
        command = input("\nВВЕДИТЕ: 1 - ДЛЯ НОВОЙ ИГРЫ, 2 - ДЛЯ ВЫХОДА, "
                        "3 - ДЛЯ ПРОСМОТРА ПРОШЛЫХ СЛОВ.\n")
    except FileNotFoundError:
        print('Файл used_words не найден!')

    return command


def get_command_after_game(start_word, current_word, health_points):
    """Receive a new team after the end of the game"""
    if ''.join(start_word) == current_word:
        print(Fore.GREEN + f"\nВЫ ПОБЕДИЛИ! СЛОВО {Fore.YELLOW}"
                           f"{current_word}{Style.RESET_ALL}{Fore.GREEN} "
                           f"РАЗГАДАНО!" + Style.RESET_ALL)
        command = input("\nВВЕДИТЕ: 1 - ДЛЯ НОВОЙ ИГРЫ, 2 - ДЛЯ ВЫХОДА, "
                        "3 - ДЛЯ ПРОСМОТРА ПРОШЛЫХ СЛОВ.\n")
    else:
        print(Fore.RED + "\nК СОЖАЛЕНИЮ, ВЫ ПРОИГРАЛИ." + Style.RESET_ALL)
        make_man_picture(health_points)
        command = input("\nВВЕДИТЕ: 1 - ДЛЯ НОВОЙ ИГРЫ, 2 - ДЛЯ ВЫХОДА, "
                        "3 - ДЛЯ ПРОСМОТРА ПРОШЛЫХ СЛОВ.\n")

    return command


def make_man_picture(health_points):
    """Draw the current state of the person"""
    if health_points == 8:
        print("""
                ---------
                |       
                |       
                |      
                |       
                |      
                -
                """)
    if health_points == 7:
        print("""
                ---------
                |       |
                |       
                |      
                |       
                |      
                -
                """)
    if health_points == 6:
        print("""
                ---------
                |       |
                |       ◯
                |      
                |       
                |      
                -
                """)
    if health_points == 5:
        print("""
                ---------
                |       |
                |       ◯
                |       |
                |       
                |      
                -
                """)
    if health_points == 4:
        print("""
                ---------
                |       |
                |       ◯
                |       |
                |       |
                |      
                -
                """)
    if health_points == 3:
        print("""
                ---------
                |       |
                |       ◯
                |      /|
                |       |
                |      
                -
                """)
    if health_points == 2:
        print("""
                ---------
                |       |
                |       ◯
                |      /|\\
                |       |
                |      
                -
                """)
    if health_points == 1:
        print("""
                ---------
                |       |
                |       ◯
                |      /|\\
                |       |
                |      /
                -
                """)
    if health_points == 0:
        print("""
                ---------
                |       |
                |       ◯
                |      /|\\
                |       |
                |      / \\
                -
                """)
