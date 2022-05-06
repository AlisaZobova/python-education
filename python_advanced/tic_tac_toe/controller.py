"""Controller"""
from loggers import logger
from model import Game
from view_ui import ViewUI
from player import Player


class Controller:
    """Class controller"""
    def __init__(self, model: Game):
        self.view = ViewUI()
        self.model = model

    @staticmethod
    def main():
        """Method to greet and call the method to show the menu"""
        Game.info()
        Controller.menu(ViewUI.action_request())

    @staticmethod
    def menu(action):
        """Method menu"""
        while action not in ['1', '']:
            if action == '2':
                Game.get_results()
            if action == '3':
                Game.delete_results()
            action = ViewUI.action_request()
        if action == '1':
            Controller.start()
        else:
            logger.info("Have a good day!")

    @staticmethod
    def start():
        """Method to start the game"""
        controller = Controller(Game.create_game(
            Player(ViewUI.name_request('first')),
            Player(ViewUI.name_request('second'))))

        controller.run()

    def run(self):
        """Main method for playing"""
        self.model.start_game()
        self.view.print_field(self.model.board.field)

        while self.model.move_count < 10:
            if self.model.move_count % 2 != 0:
                self.model.move(self.view.coordinate_request(
                    self.model.player1.name, self.model.board.field))
            else:
                self.model.move(self.view.coordinate_request(
                    self.model.player2.name, self.model.board.field))
            self.view.print_field(self.model.board.field)
            if self.model.check_win():
                break
            self.model.move_count += 1
        else:
            logger.critical("Friendship wins in this game!")

        self.game_continue()

    def game_continue(self):
        """Method for choosing to continue or exit the game"""
        answer = self.view.get_answer()
        try:
            if answer == 'yes':
                self.model.move_count = 1
                self.model.board.clear()
                logger.info("\nOK, let's go!")
                self.run()

            elif answer == 'no':
                Controller.menu(ViewUI.action_request())

            else:
                raise ValueError("Incorrect answer!")

        except ValueError as exception:
            logger.error(exception)
            self.game_continue()


if __name__ == "__main__":
    Controller.main()
