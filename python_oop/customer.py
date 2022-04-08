""""Class customer"""

from order import Order


class Customer:
    """Class for storing customers' properties and methods"""
    customers = []

    def __init__(self, name: str, phone_number: str, order: Order):
        """Class constructor"""
        self.name = name
        self._phone_number = phone_number
        self.order = order
        Customer.customers.append(self)

    def explore_the_menu(self):
        """Method that reports that the client is exploring the menu"""
        print(f"The customer {self.name} is exploring the menu...")

    def dishes_in_order(self):
        """Method for accepting an order from a customer"""
        for i in self.order.order_dishes:
            print("-", i.name)

    @staticmethod
    def pay(money: float):
        """Method that returns the amount of money the customer has paid"""
        return money
