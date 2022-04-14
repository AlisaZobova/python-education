""""Class car"""


class Car:
    """Class for storing cars' properties and methods"""
    cars = []

    def __init__(self, car_num: str, fuel_consumption: float, fuel_type: str):
        """Class constructor"""
        self.car_num = car_num
        self.fuel_consumption = fuel_consumption
        self.fuel_type = fuel_type
        self.condition = "riding"
        Car.cars.append(self)

    def car_description(self):
        """Method that describes the car"""
        print(f"The car with number {self.car_num} is {self.condition}. "
              f"Fuel type: {self.fuel_type}, fuel consumption: {self.fuel_consumption} l/100 km")

    def drive(self):
        """Method for driving a car"""
        self.condition = "riding"
        print(f"The car is {self.condition}...")

    def refuel(self):
        """Method for refueling a car"""
        self.condition = "refueling"
        print(f"The car is {self.condition}...")

    def fix(self):
        """Method for fixing a car"""
        self.condition = "fixing"
        print(f"The car is {self.condition}...")
