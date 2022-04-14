"""Abstract class transport"""

from abc import ABC, abstractmethod


class Transport(ABC):
    """Abstract transport class"""
    def __init__(self, num: str, fuel_consumption: float,
                 remaining_fuel: float, max_number_of_passengers: int, brand: str):
        """Class constructor"""
        self.brand = brand
        self.num = num
        self.fuel_consumption = fuel_consumption
        self.condition = "ok"
        self.remaining_fuel = remaining_fuel
        self.max_number_of_passengers = max_number_of_passengers
        self.number_of_passengers = 0

    @abstractmethod
    def move(self, km: float):
        """
        A method for checking the ability of a transport
        to travel a given number of kilometers
        """
        try:
            if self.remaining_fuel - self.fuel_consumption * km / 100 < 0:
                raise ValueError
            self.remaining_fuel -= self.fuel_consumption * km / 100
        except ValueError:
            print("Not enough fuel for so many kilometers!")

    @abstractmethod
    def refuel(self, liters: float, transport_type: str):
        """Method for refueling"""
        self.remaining_fuel += liters
        print(f"The {transport_type} is filled with {liters} liters. "
              f"There are currently {self.remaining_fuel} liters in the tank.")

    def fixing(self):
        """Method that changes the state of the transport during repair"""
        self.condition = "fix"

    @abstractmethod
    def breaking(self, transport_type: str, part: str):
        """Method reporting about the breakdown of transport"""
        self.condition = "break"
        print(f"{transport_type} number {self.num} broke {part}.")

    def undergo_technical_inspection(self):
        """Technical inspection method"""
        if self.condition == "break":
            result = "failed"
        else:
            result = "passed"
        return result

    def __iadd__(self, other):
        """
        Overridden method __iadd__ that checking if it
        is possible to add a given number of passengers
        """
        try:
            if self.number_of_passengers + other > self.max_number_of_passengers:
                raise ValueError
            self.number_of_passengers += other
        except ValueError:
            print("Too many passengers")
        return self

    def __hash__(self):
        """Overridden method __hash__ that hashes the brand"""
        return hash(self.brand)

    def __eq__(self, other):
        """Overridden method __eq__ that checks if brands are the same"""
        return hash(self) == hash(other)

    def __bool__(self):
        """Overridden method __bool__ that checks if the transport has passed inspection"""
        if self.undergo_technical_inspection() == "passed":
            return True
        return False
