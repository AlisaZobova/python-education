""""Class supplier"""

from datetime import datetime
from employee import Employee


class Supplier(Employee):
    """Class for storing suppliers' properties and methods"""
    suppliers = []

    def __init__(self, name: str, phone_number: str, salary_rate: float, date_of_employment: str):
        """Class constructor"""
        super().__init__(name, phone_number, salary_rate)
        self.orders = []
        self.__date_of_employment = date_of_employment
        Supplier.suppliers.append(self)

    def accept_order(self, positions_amount: dict):
        """Method for accepting an order"""
        self.orders.append(positions_amount)
        print(f"{self.name} accepted order #{self.orders.index(positions_amount)+1}:")
        for key, value in positions_amount.items():
            print(f"{key} - {value} pcs")

    def deliver_products(self, index: int):
        """Method for notification of delivery and verification of goods"""
        print(f"Order #{index+1} has been delivered. Check the product names and quantities:")
        for key, value in self.orders[index].items():
            print(f"{key} - {value} pcs")

    def get_salary(self, salary: float):
        """Method that prints a message about receiving a salary and returns its amount"""
        print(f"Supplier {self.name} received a salary of {salary} UAH.")
        return super().get_salary(salary)

    def salary_increase(self):
        """Method for increasing salary after a year of work"""
        if (datetime.today() - datetime.strptime(self.__date_of_employment, '%d/%m/%y')).days > 365:
            self.salary_rate *= 1.3
            print(f"The salary has been raised! "
                  f"Now {self.name}'s salary is {self.salary_rate} UAH.")
        else:
            print("Unfortunately, a year has not yet passed since the date of employment. "
                  "Try later.")
