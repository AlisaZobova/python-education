"""Class ship"""
from transport import Transport


class Ship(Transport):
    """Class ship"""
    def __init__(self, num: str, fuel_consumption: float, remaining_fuel: float,
                 max_number_of_passengers: int, brand: str, captain: str):
        """Class constructor"""
        super().__init__(num, fuel_consumption, remaining_fuel, max_number_of_passengers, brand)
        self.__captain = captain

    @property
    def captain(self):
        """Captain getter"""
        return self.__captain

    @captain.setter
    def captain(self, captain):
        """Captain setter"""
        self.__captain = captain

    @captain.deleter
    def captain(self):
        """Captain deleter"""
        del self.__captain

    @classmethod
    def description(cls):
        """Method that prints information about the class"""
        print(f"Class {cls.__name__} is dedicated to one of the types of water transport - a ship.")

    @staticmethod
    def get_cruise_permit(weather):
        """Method for obtaining permission to sail"""
        if weather == "good":
            print("You can sail away.")
        else:
            print("Cruise canceled.")

    def refuel(self, liters: float, transport_type="ship"):
        """Method for refueling"""
        super().refuel(liters, transport_type)

    def breaking(self, thing: str, part: str, transport_type="Ship"):
        """
        Method reporting about the breakdown of a ship.
        If the ship was broken on an iceberg, it is removed.
        """
        if thing == "iceberg":
            print(f"The ship {self.num} was destroyed by an iceberg.")
            del self
        else:
            super().breaking(transport_type, part)

    def move(self, km: float):
        """
        A method for checking the ability of a ship
        to travel a given number of kilometers and
        reporting about the ship movement
        """
        print("The ship sailed on a cruise...")
        return super().move(km)


SHIP = Ship("ANN", 15, 800, 100, "Selle", "Max")
SHIP1 = Ship("ANASTASIA", 20, 450, 90, "Selle", "George")
Ship.description()
SHIP.captain = "Alex"
print(SHIP.captain)
SHIP.get_cruise_permit("good")
SHIP.refuel(85)
SHIP.move(15)
print(SHIP.undergo_technical_inspection())
print(bool(SHIP))
SHIP.breaking("stone", "bow")
print(SHIP.undergo_technical_inspection())
SHIP.fixing()
print(bool(SHIP))
SHIP.breaking("iceberg", "bow")
SHIP += 800
print(SHIP.number_of_passengers)
SHIP += 40
print(SHIP.number_of_passengers)
print(SHIP == SHIP1)
