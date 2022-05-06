"""Abstract class view"""

# pylint: disable=R0903

from abc import ABC, abstractmethod


class View(ABC):
    """Class for viewing"""

    @staticmethod
    @abstractmethod
    def print_field(field: list):
        """Method for printing a field"""
        raise NotImplementedError

    @staticmethod
    def coordinate_request(name: str, field: list):
        """Method for getting coordinates"""
        raise NotImplementedError

    @staticmethod
    def action_request():
        """Method for getting desired action"""
        raise NotImplementedError

    @staticmethod
    def name_request(num: str):
        """Method for creating player name"""
        raise NotImplementedError

    @staticmethod
    def get_answer():
        """Method for getting answer"""
        raise NotImplementedError
