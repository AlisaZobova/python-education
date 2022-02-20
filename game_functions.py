import random
from colorama import init
from colorama import Fore, Style
init()


def get_new_word():
    try:
        with open("hangman_words", 'r') as w:
            words = []
            for line in w:
                words.append(line.rstrip('\n'))
        with open("used_words", 'r') as u_w:
            used_words = []
            for line in u_w:
                used_words.append(line.rstrip('\n'))
        with open("used_words", 'a') as list_u_w:
            game_words = set(words).symmetric_difference(set(used_words))
            current_word = random.choice(list(game_words))
            list_u_w.write(current_word + '\n')
        return current_word
    except Exception as e:
        print(e)


def main_func(health_points, start_word, all_let, used_let, current_word, wrong_let):
    make_man_picture(health_points)
    print(Fore.GREEN + '\nСЛОВО:' + Style.RESET_ALL, *start_word)
    print(Fore.YELLOW + f'''КОЛИЧЕСТВО ЖИЗНЕЙ: {Style.RESET_ALL}{health_points}''')
    letter = input("ВВЕДИТЕ БУКВУ: ").upper()
    while letter not in all_let:
        letter = input(Fore.RED + f'ЗАДАНО НЕКОРРЕКТНОЕ ЗНАЧЕНИЕ!\n{Style.RESET_ALL}'
                       f'ВВЕДИТЕ БУКВУ РУССКОГО АЛФАВИТА: ').upper()
    while letter in used_let:
        letter = input(Fore.RED + f'БУКВА УЖЕ ИСПОЛЬЗОВАЛАСЬ!{Style.RESET_ALL}\nВВЕДИТЕ ДРУГУЮ: ').upper()
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


def get_command_after_game(start_word, current_word, health_points):
    if ''.join(start_word) == current_word:
        print(Fore.GREEN + f"\nВЫ ПОБЕДИЛИ! СЛОВО {Fore.YELLOW}{current_word}{Style.RESET_ALL}{Fore.GREEN} "
                           f"РАЗГАДАНО!" + Style.RESET_ALL)
        command = input("\nВВЕДИТЕ: 1 - ДЛЯ НОВОЙ ИГРЫ, 2 - ДЛЯ ВЫХОДА, 3 - ДЛЯ ПРОСМОТРА ПРОШЛЫХ СЛОВ.\n")
    else:
        print(Fore.RED + "\nК СОЖАЛЕНИЮ, ВЫ ПРОИГРАЛИ." + Style.RESET_ALL)
        make_man_picture(health_points)
        command = input("\nВВЕДИТЕ: 1 - ДЛЯ НОВОЙ ИГРЫ, 2 - ДЛЯ ВЫХОДА, 3 - ДЛЯ ПРОСМОТРА ПРОШЛЫХ СЛОВ.\n")
    return command


def make_man_picture(health_points):
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
