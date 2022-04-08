""""Class cuisine"""


class Cuisine:
    """Class for storing cuisines' properties and methods"""
    cuisines = []

    def __init__(self, name: str):
        """Class constructor"""
        self.name = name
        self.dishes = []
        Cuisine.cuisines.append(self)

    def add_new_dishes(self, dishes: list):
        """Method for adding new dish"""
        for i in dishes:
            self.dishes.append(i)

    def del_dishes(self, dishes_id: list):
        """Method for deleting cuisine"""
        for i in dishes_id:
            del self.dishes[i]

    def update(self, dishes: list):
        """Method for updating dishes in the cuisine"""
        self.dishes = dishes

    def print_cuisine_items(self):
        """Method for printing cuisine dishes"""
        print(f"{self.name} cuisine:")
        for i in self.dishes:
            print("-", i.name)
