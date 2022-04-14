""""Class deliveryman"""

from datetime import datetime
from order import Order
from car import Car
from employee import Employee


class Deliveryman(Employee):
    """Class for storing deliveries' properties and methods"""
    deliveries = []

    def __init__(self, name: str, phone_number: str, date_of_employment: str,
                 salary_rate: float, car: Car):
        """Class constructor"""
        super().__init__(name, phone_number, salary_rate)
        self.__date_of_employment = date_of_employment
        self.orders = []
        self.car = car
        Deliveryman.deliveries.append(self)

    def pick_up_order(self, order: Order):
        """Method for adding a taken order to the list"""
        self.orders.append(order)
        return f"Order #{order.order_id} was taken."

    def deliver_the_order(self, order_id: int):
        """Order delivery notification method"""
        for order in self.orders:
            if order.order_id == order_id:
                self.orders.remove(order)
        return f"Order #{order_id} was delivered."

    def change_car(self, car: Car):
        """Method for changing a car"""
        self.car = car

    @staticmethod
    def get_paid(payment: float):
        """Method of receiving payment"""
        return payment

    @staticmethod
    def give_change(payment: float, total: float):
        """Change return method"""
        return f"Change is {payment - total} UAH."

    def get_salary(self, salary: float):
        """Method that prints a message about receiving a salary and returns its amount"""
        print(f"Deliveryman {self.name} received a salary of {salary} UAH.")
        return super().get_salary(salary)

    def salary_increase(self):
        """Method for increasing salary after a year of work"""
        if (datetime.today() - datetime.strptime(self.__date_of_employment, '%d/%m/%y')).days > 365:
            self.salary_rate *= 1.5
            print(f"The salary has been raised! "
                  f"Now {self.name}'s salary is {self.salary_rate} UAH.")
        else:
            print("Unfortunately, a year has not yet passed since the date of employment. "
                  "Try later.")
