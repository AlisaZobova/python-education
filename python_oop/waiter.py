""""Class waiter"""

from datetime import datetime
from order import Order
from employee import Employee


class Waiter(Employee):
    """Class for storing waiters' properties and methods"""
    waiters = []

    def __init__(self, name: str, phone_number: str, date_of_employment: str, salary_rate: float):
        """Class constructor"""
        super().__init__(name, phone_number, salary_rate)
        self.__date_of_employment = date_of_employment
        self.orders = []
        Waiter.waiters.append(self)

    def accept_order(self, order: Order):
        """Method for accepting an order"""
        print("Your order:")
        dishes = [order.order_dishes[i].name for i in range(len(order.order_dishes))]
        print("-", '\n- '.join(dishes))
        answer = input("If everything right - print 'Yes':\n")
        if answer == "Yes":
            self.orders.append(order)
            print("OK, thanks!")
        else:
            print("Please clarify what exactly is wrong.")

    def bring_the_order(self, order_id: int):
        """Method for bringing an order"""
        print(f"Your order #{order_id} is ready. Bon appetit!")
        for order in self.orders:
            if order.order_id == order_id:
                self.orders.remove(order)

    def work(self):
        """Method to report that the waiter is working"""
        print(f"Waiter {self.name} is working now...")

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
        print(f"Waiter {self.name} received a salary of {salary} UAH.")
        return super().get_salary(salary)

    def salary_increase(self):
        """Method for increasing salary after a year of work"""
        if (datetime.today() - datetime.strptime(self.__date_of_employment, '%d/%m/%y')).days > 365:
            self.salary_rate *= 1.7
            print(f"The salary has been raised! "
                  f"Now {self.name}'s salary is {self.salary_rate} UAH.")
        else:
            print("Unfortunately, a year has not yet passed since the date of employment. "
                  "Try later.")
