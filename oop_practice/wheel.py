"""Class wheel"""
from tire import Tire


class Wheel(Tire):
    """Wheel class"""
    wheels_amount = 0

    def __init__(self, material: str, diameter: int, width: int, tire_type: str):
        """Class constructor"""
        super().__init__(diameter, width, tire_type)
        self.material = material
        self.condition = "ok"
        Wheel.wheels_amount += 1

    def breaking(self, thing: str):
        """Method reporting about the breakdown of wheel"""
        print(f"Wheel hit by a {thing}.")
        self.condition = "break"

    def spin(self):
        """Method reporting about wheel spin"""
        self.condition = "ok"
        print(f"The wheel is spinning...")

    def change_of_season(self, season: str):
        """A method that changes the type of tires depending on the season"""
        super().tire_replacement(season)


if __name__ == "__main__":
    WHEEL = Wheel("aluminum", 16, 20, "summer")
    WHEEL1 = Wheel("steel", 16, 20, "summer")
    WHEEL2 = Wheel("steel", 18, 20, "summer")
    print(WHEEL == WHEEL1)
    print(WHEEL == WHEEL2)
    print(WHEEL < WHEEL2)
