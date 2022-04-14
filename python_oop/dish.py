""""Class dish"""


class Dish:
    """Class for storing information about dishes"""
    items = []

    def __init__(self, name: str, price: float, weight: int, grams: dict,
                 recipe: str):
        """Class constructor"""
        self.name = name
        self.price = price
        self.weight = weight
        self.grams = grams
        self.__recipe = recipe
        Dish.items.append(self)

    @property
    def recipe(self):
        """Recipe getter"""
        return self.__recipe

    @recipe.setter
    def recipe(self, recipe: str):
        """Recipe setter"""
        self.__recipe = recipe

    def check_short_composition(self):
        """Displays the ingredients of the dish"""
        print(f"Short composition of {self.name}:")
        for i in self.grams.keys():
            print("-", i)
