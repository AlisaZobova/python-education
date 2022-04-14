""""Class menu"""


class Menu:
    """Class for storing information about menus"""
    menus = []

    def __init__(self, menu_type: str):
        """Class constructor"""
        self.menu_type = menu_type
        self.cuisines = []
        Menu.menus.append(self)

    def update(self, cuisines: list):
        """Method for updating menu"""
        self.cuisines = cuisines

    def add_new_cuisines(self, cuisines: list):
        """Method for adding new cuisine"""
        for i in cuisines:
            self.cuisines.append(i)

    def del_cuisines(self, cuisines_id: list):
        """Method for deleting cuisine"""
        for i in cuisines_id:
            del self.cuisines[i]

    def menu_description(self):
        """Method for printing menu description"""
        print(f"{self.menu_type} menu contains such cuisines:")
        for i in self.cuisines:
            print("-", i.name)
