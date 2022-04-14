"""Class tire (created for mro)"""


class Tire:
    """Class tire for wheels"""
    def __init__(self, diameter: int, width: int, tire_type: str):
        """Class constructor"""
        self.diameter = diameter
        self.width = width
        self.tire_type = tire_type

    def tire_replacement(self, tire_type):
        """Method reporting about tire replacement"""
        self.tire_type = tire_type
        print(f"The tire has been replaced. New tire type: {self.tire_type}.")

    def __eq__(self, other):
        """Overridden method __eq__ that compares tire diameters"""
        return self.diameter == other.diameter

    def __lt__(self, other):
        """Overridden method __lt__ to check if one diameter is less than another"""
        return self.diameter < other.diameter
