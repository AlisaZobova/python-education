"""TASK 2 - CODESTYLE"""


class Calculator:
    """Class for mathematical calculations"""
    def __init__(self, first_num, second_num):
        """Class constructor"""
        self.first_num = first_num
        self.second_num = second_num

    def addition(self):
        """Addition method"""
        return self.first_num + self.second_num

    def subtraction(self):
        """Subtraction method"""
        return self.first_num - self.second_num

    def multiplication(self):
        """Multiplication method"""
        return self.first_num * self.second_num

    def division(self):
        """Division method"""
        try:
            return self.first_num / self.second_num
        except ZeroDivisionError:
            print("На ноль делить нельзя!")
