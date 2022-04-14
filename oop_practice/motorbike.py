"""Class motorbike"""
from transport import Transport
from wheel import Wheel


class Motorbike(Transport, Wheel):
    """Class motorbike"""
    def __init__(self, num: str, fuel_consumption: float,
                 remaining_fuel: float, max_number_of_passengers: int, brand: str,
                 wheel_material: str, tire_diameter: int, tire_width: int, tire_type: str):
        """Class constructor"""
        Transport.__init__(self, num, fuel_consumption, remaining_fuel,
                           max_number_of_passengers, brand)
        Wheel.__init__(self, wheel_material, tire_diameter, tire_width, tire_type)

    @classmethod
    def description(cls):
        """Method that prints information about the class"""
        print(f"Class {cls.__name__} is dedicated to one of "
              f"the types of ground transport - a motorbike.")

    def refuel(self, liters: float, transport_type="motorbike"):
        """Method for refueling"""
        super().refuel(liters, transport_type)

    def breaking(self, part: str, thing: str, transport_type="Motorbike"):
        """Method reporting about the breakdown of a motorbike."""
        if part == "wheel":
            Wheel.breaking(self, thing)
        super().breaking(transport_type, part)

    def move(self, km: float):
        """
        A method for checking the ability of a motorbike
        to travel a given number of kilometers and
        reporting about the wheels spin
        """
        print(f"Motorbike number {self.num} rides.")
        Wheel.spin(self)
        return super().move(km)


MOTORBIKE = Motorbike("GH878HG", 8, 30, 2, "BMW", "aluminum", 14, 15, "summer")
Motorbike.description()
MOTORBIKE.refuel(5)
print(MOTORBIKE.undergo_technical_inspection())
MOTORBIKE.move(15)
MOTORBIKE.breaking("left side", "border")
MOTORBIKE.breaking("wheel", "piece of glass")
MOTORBIKE.fixing()
