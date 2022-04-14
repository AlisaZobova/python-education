""""Class order"""

from dish import Dish


class Order:
    """Class for storing information about orders"""
    orders = []

    def __init__(self, order_id: int, dishes_id: list, order_status: str):
        """Class constructor"""
        self.order_id = order_id
        self.order_dishes = [Dish.items[i] for i in dishes_id]
        self.order_status = order_status
        Order.orders.append(self)

    def add_new_dish(self, dish: Dish):
        """Method for adding new dish"""
        self.order_dishes.append(dish)

    def del_dish(self, dish_id: int):
        """Method for deleting dish"""
        del self.order_dishes[dish_id]

    def cancel_the_order(self):
        """Method for cancelling the order"""
        self.order_status = "Canceled"
        self.order_dishes = []

    def order_price_calculation(self):
        """Method for calculating total price"""
        prices = [i.price for i in self.order_dishes]
        total_price = sum(prices)
        return f"Order price: {total_price}"
