"""Class airplane"""
from transport import Transport
from wheel import Wheel


class Airplane(Transport, Wheel):
    """Class airplane"""
    def __init__(self, num: str, fuel_consumption: float, remaining_fuel: float,
                 max_number_of_passengers: int, brand: str, pilot: str, wheel_material: str,
                 tire_diameter: int, tire_width: int, tire_type: str):
        """Class constructor"""
        Transport.__init__(self, num, fuel_consumption, remaining_fuel,
                           max_number_of_passengers, brand)
        Wheel.__init__(self, wheel_material, tire_diameter, tire_width, tire_type)
        self.__pilot = pilot

    @property
    def pilot(self):
        """Pilot getter"""
        return self.__pilot

    @pilot.setter
    def pilot(self, pilot):
        """Pilot setter"""
        self.__pilot = pilot

    @pilot.deleter
    def pilot(self):
        """Pilot deleter"""
        del self.__pilot

    @classmethod
    def description(cls):
        """Method that prints information about the class"""
        print(f"Class {cls.__name__} is dedicated to one of "
              f"the types of air transport - an airplane.")

    @staticmethod
    def get_flight_permit(weather):
        """Method for obtaining permission to fly"""
        if weather == "good":
            print("Flight will take place.")
        else:
            print("Flight canceled.")

    def refuel(self, liters: float, transport_type="airplane"):
        """Method for refueling"""
        super().refuel(liters, transport_type)

    def breaking(self, part: str, thing: str, transport_type="Airplane"):
        """Method reporting about the breakdown of an airplane."""
        if part == "wheel":
            Wheel.breaking(self, thing)
        super().breaking(transport_type, part)

    def move(self, km: float):
        """
        A method for checking the ability of a ship
        to travel a given number of kilometers and
        reporting about the airplane movement
        """
        print(f"Airplane number {self.num} flies.")
        super().move(km)


AIRPLANE = Airplane("GH478568", 5.7, 184, 35, "BMW", "Peter", "aluminum", 16, 20, "summer")
Airplane.description()
AIRPLANE.pilot = "Fred"
print(AIRPLANE.pilot)
AIRPLANE.get_flight_permit("bad")
AIRPLANE.refuel(80)
print(AIRPLANE.undergo_technical_inspection())
AIRPLANE.breaking("wing", "wall")
AIRPLANE.fixing()
AIRPLANE.breaking("wheel", "metal pin")
print(AIRPLANE.undergo_technical_inspection())
AIRPLANE.move(9000)
AIRPLANE += 20
print(AIRPLANE.number_of_passengers)
AIRPLANE += 90
print(AIRPLANE.number_of_passengers)

AIRPLANE1 = Airplane("GH478568", 5.7, 523, 35, "BMW", "Max", "aluminum", 16, 20, "summer")

print(AIRPLANE == AIRPLANE1)
print(bool(AIRPLANE))
print(bool(AIRPLANE1))
