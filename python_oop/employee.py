""""Abstract class employee"""

from abc import ABC, abstractmethod


class Employee(ABC):
    """Abstract class that stores a template of restaurant employees' properties and methods"""
    @abstractmethod
    def __init__(self, name: str, phone_number: str, salary_rate: float):
        """Class constructor"""
        self.name = name
        self._phone_number = phone_number
        self.salary_rate = salary_rate

    @abstractmethod
    def get_salary(self, salary: float):
        """An abstract method for receiving a salary"""
        return salary

    @abstractmethod
    def salary_increase(self):
        """An abstract method for increasing salary"""
