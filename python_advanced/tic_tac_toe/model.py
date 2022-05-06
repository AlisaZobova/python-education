"""Class game"""
import os
from random import randint
from player import Player
from board import Board
from loggers import logger


class Game:
    """Main class game"""
    def __init__(self, player1: Player, player2: Player, board=Board()):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.move_count = 1

    @staticmethod
    def info():
        """Method to greet and call the method to show the menu"""
        logger.info("Hi! This is tic-tac-toe game!")

    @staticmethod
    def create_game(player1: Player, player2: Player):
        """Method for creating game"""
        game = Game(player1, player2)
        logger.critical("%s and %s started the game!", game.player1.name, game.player2.name)
        return game

    def start_game(self):
        """Method for choosing the player who will move first"""
        player_num = randint(1, 2)

        if player_num == 1:
            self.player1.num = 1
            self.player2.num = 2

        if player_num == 2:
            self.player2.num = 1
            self.player1.num = 2
            self.player1, self.player2 = self.player2, self.player1

        logger.info("%s moves first.", self.player1.name)

    def move(self, coords):
        """Method for making move"""
        width, height = coords
        if self.move_count % 2 != 0:
            self.board.field[height - 1][width - 1] = 'x'
            logger.info('%s made a move.', self.player1.name)
        else:
            self.board.field[height - 1][width - 1] = 'o'
            logger.info('%s made a move.', self.player2.name)

    def check_win(self):
        """Method to check if it's already a win or not"""
        win = False
        x_win = ['x', 'x', 'x']
        o_win = ['o', 'o', 'o']

        rows = self.board.field
        len_r = len(rows)

        columns = [[i[k] for i in rows] for k in range(len_r)]

        diagonal1 = [[i[k] for i in rows for k in range(len_r) if k == rows.index(i)]]
        diagonal2 = [[i[k] for i in rows for k in range(len_r) if k + rows.index(i) == len_r - 1]]
        diagonals = diagonal1 + diagonal2

        if (any(i in (x_win, o_win) for i in rows)
                or any(j in (x_win, o_win) for j in columns)
                or any(d in (x_win, o_win) for d in diagonals)):
            win = True

        if win:
            self.determination_winner()

        return win

    def determination_winner(self):
        """Method for determining the winner and displaying the number of wins at this stage"""
        if self.move_count % 2 != 0:
            logger.critical("%s won!", self.player1.name)
            self.player1.victories += 1
        else:
            logger.critical("%s won!", self.player2.name)
            self.player2.victories += 1
        self.player1.print_victories()
        self.player2.print_victories()

    @staticmethod
    def get_results():
        """Method for getting results of the game"""
        with open('file_game.log', 'r') as results:
            for line in results.read().splitlines():
                logger.info(line)

    @staticmethod
    def delete_results():
        """Method for deleting game results"""
        os.system(r' >file_game.log')  # deletes the contents of a file
