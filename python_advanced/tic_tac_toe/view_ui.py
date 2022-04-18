"""Class ViewUI"""

# pylint: disable=R0903

import re
from view import View
from loggers import logger


class ViewUI(View):
    """Class for view part"""
    @staticmethod
    def print_field(field: list):
        """Method for printing a field"""
        logger.info("-------------")
        for i in range(3):
            logger.info('| %s | %s | %s |', field[i][0], field[i][1], field[i][2])
            logger.info("-------------")

    @staticmethod
    def coordinate_request(name: str, field: list):
        """Method for getting coordinates"""
        width, height = int(input(f"{name}, enter width:\n")), int(input("Enter height:\n"))
        while True:
            try:
                if not isinstance(height, int) or not isinstance(height, int) \
                        or height <= 0 or width <= 0:
                    raise ValueError("You entered not a natural number!")

                if field[height - 1][width - 1] != " ":
                    raise ValueError("This cell is already taken!")

            except ValueError as exception:
                logger.error(exception)
                width, height = int(input(f"{name}, enter width:\n")), int(input("Enter height:\n"))

            except IndexError:
                logger.error("Invalid width or height!")
                width, height = int(input(f"{name}, enter width:\n")), int(input("Enter height:\n"))

            else:
                break

        return width, height

    @staticmethod
    def action_request():
        """Method for getting desired action"""
        action = input("Enter 1 - to start a new game, "
                       "2 - to view win log, 3 - to clear win log, Enter - to exit:\n")
        return action

    @staticmethod
    def name_request(num: str):
        """Method for creating player name"""
        name = input(f"Enter the name of the {num} player:\n")
        while True:
            is_name = re.match(r'^[A-Z][a-z]*$', name)
            if is_name is None:
                try:
                    raise ValueError("Incorrect name of the player!")
                except ValueError as error:
                    logger.error(error)
                    name = input(f"Enter the correct name:\n")
            else:
                break

        return name

    @staticmethod
    def get_answer():
        """Method for getting answer"""
        answer = input("Do you want to continue playing without changing opponents?\n"
                       "Enter 'yes' to continue, 'no' - to game completion:\n")
        while True:
            try:
                if answer not in ['yes', 'no']:
                    raise ValueError("Incorrect answer!")

            except ValueError as exception:
                logger.error(exception)
                answer = input("Do you want to continue playing without changing opponents?\n"
                               "Enter 'yes' to continue, 'no' - to game completion:\n")

            else:
                break

        return answer
