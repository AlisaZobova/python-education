"""Class bus"""
from transport import Transport
from wheel import Wheel


class Bus(Transport, Wheel):
    """Class bus"""
    def __init__(self, num: str, fuel_consumption: float, remaining_fuel: float,
                 max_number_of_passengers: int, brand: str, wheel_material: str,
                 tire_diameter: int, tire_width: int, tire_type: str):
        """Class constructor"""
        Transport.__init__(self, num, fuel_consumption, remaining_fuel,
                           max_number_of_passengers, brand)
        Wheel.__init__(self, wheel_material, tire_diameter, tire_width, tire_type)

    @classmethod
    def description(cls):
        """Method that prints information about the class"""
        print(f"Class {cls.__name__} is dedicated to one of the types of ground transport - a bus.")

    def refuel(self, liters: float, transport_type="bus"):
        """Method for refueling"""
        super().refuel(liters, transport_type)

    def breaking(self, part: str, thing: str, transport_type="Bus"):
        """Method reporting about the breakdown of a bus."""
        if part == "wheel":
            Wheel.breaking(self, thing)
        Transport.breaking(self, transport_type, part)

    def move(self, km: float):
        """
        A method for checking the ability of a bus
        to travel a given number of kilometers and
        reporting about the wheels spin
        """
        print(f"Bus number {self.num} rides.")
        Wheel.spin(self)
        return super().move(km)


BUS = Bus("HJ8907JY", 9.0, 58, 15, "Bogdan", "aluminum", 16, 20, "summer")
Bus.description()
BUS.refuel(50)
BUS.breaking("left side", "tree")
BUS.breaking("wheel", "piece of glass")
print(BUS.undergo_technical_inspection())
BUS.fixing()
print(BUS.condition)
BUS.move(85)
BUS.change_of_season("winter")
