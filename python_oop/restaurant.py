"""The main class restaurant"""

from menu import Menu
from waiter import Waiter
from supplier import Supplier
from deliveryman import Deliveryman
from customer import Customer
from promotion import Promotion
from car import Car
from dish import Dish
from order import Order
from cuisine import Cuisine


class Restaurant:
    """Class describing the activities of the restaurant"""
    restaurants = []

    def __init__(self, name: str, location: str, status: str = "opened"):
        """Class constructor"""
        self.name = name
        self.status = status
        self.location = location
        self.menus = []
        self.waiters = []
        self.suppliers = []
        self.deliveries = []
        self.customers = []
        self.promotions = []

    def print_restaurant_location(self):
        """Prints out the location of the restaurant"""
        print(f"Restaurant '{self.name}' located in {self.location}.")

    def new_customer(self, customer: Customer):
        """Adds a new client and greets him"""
        self.customers.append(customer)
        print(f"Welcome, {customer.name}!")

    def restaurant_cuisines(self):
        """Describes menus and cuisines of the restaurant"""
        print(f"'{self.name}' restaurant offers you a variety of cuisines!")
        for menu in self.menus:
            menu.menu_description()

    def restaurant_promotions(self):
        """Describes promotions of the restaurant"""
        print(f"{self.name}'s promotions:")
        for promo in self.promotions:
            if promo.status == "is running" or promo.status == "has started":
                print(f"{promo.promo_name}: {promo.description}")

    def open(self):
        """Announces the opening of the restaurant"""
        self.status = "opened"
        print(f"Restaurant '{self.name}' {self.status}!")

    def work(self):
        """Informs that the restaurant is working"""
        self.status = "is working"
        print(f"Restaurant '{self.name}' {self.status}...")

    def close(self):
        """Informs that the restaurant is closed"""
        self.status = "closed"
        print(f"Restaurant '{self.name}' {self.status}!")

    def repair(self):
        """Informs that the restaurant is being repaired"""
        self.status = "is being repaired"
        print(f"Restaurant '{self.name}' {self.status}...")


RESTAURANT = Restaurant("Italy", "Kharkiv on Pushkinskaya street, 25")


if __name__ == "__main__":

    #  restaurant methods
    print("\nRestaurant methods:")
    RESTAURANT.menus.append(Menu("Mixed"))
    RESTAURANT.waiters.append(Waiter("John", "0665874565", "15/10/20", 7800))
    RESTAURANT.suppliers.append(Supplier("Alex", "0998567415", 8500, "12/5/21"))
    RESTAURANT.promotions.append(Promotion("1+1=3", "8.04.2022 - 25.04.2022",
                                           "Buy two dishes - get the third one for free.",
                                           "has started"))
    RESTAURANT.deliveries.append(Deliveryman("Max", "0978523414", "5/11/19",
                                             6400, car=Car("HU7890RE", 8, "gas")))
    RESTAURANT.print_restaurant_location()
    RESTAURANT.restaurant_promotions()
    RESTAURANT.open()
    RESTAURANT.work()
    RESTAURANT.repair()
    RESTAURANT.close()

    #  menu methods
    print("\nMenu methods:")
    RESTAURANT.menus[0].add_new_cuisines([Cuisine("Jewish"),
                                          Cuisine("Ukrainian"), Cuisine("English")])
    RESTAURANT.menus[0].menu_description()
    RESTAURANT.menus[0].update([Cuisine("Jewish"), Cuisine("Ukrainian"),
                                Cuisine("English"), Cuisine("Indian")])
    RESTAURANT.menus[0].del_cuisines([1])
    RESTAURANT.menus[0].menu_description()

    #  cuisine methods
    print("\nCuisine methods:")
    RESTAURANT.menus[0].cuisines[0].add_new_dishes(
        [Dish("cake", 15.6, 250, {"flour": 100, "egg": 50, "sugar": 100}, "cook"),
         Dish("cheesy", 20.4, 250, {"starch": 100, "egg": 50, "sugar": 100}, "cook"),
         Dish("pie", 35, 250, {"starch": 100, "egg": 50, "jam": 100}, "cook")])
    RESTAURANT.menus[0].cuisines[0].del_dishes([0])
    RESTAURANT.menus[0].cuisines[0].print_cuisine_items()
    RESTAURANT.menus[0].cuisines[0].update(
        [Dish("coconut", 15.6, 250, {"coconut shavings": 100, "egg": 50, "sugar": 100}, "cook"),
         Dish("cheesy", 20.4, 250, {"starch": 100, "egg": 50, "sugar": 100}, "cook"),
         Dish("pie", 35, 250, {"starch": 100, "egg": 50, "jam": 100}, "cook")])
    RESTAURANT.menus[0].cuisines[0].print_cuisine_items()

    #  dish methods
    print("\nDish methods:")
    for dish in RESTAURANT.menus[0].cuisines[0].dishes:
        dish.check_short_composition()

    print(f"Dish1 recipe: {RESTAURANT.menus[0].cuisines[0].dishes[0].recipe}.")
    RESTAURANT.menus[0].cuisines[0].dishes[0].recipe = "boil"
    print(f"New dish1 recipe: {RESTAURANT.menus[0].cuisines[0].dishes[0].recipe}.")

    #  add the first customer and show restaurant cuisines
    print("\nAdd the first customer and show restaurant cuisines:")
    RESTAURANT.new_customer(customer=Customer("Ann", "0954589785", Order(1, [1, 2], "ACCEPTED")))
    RESTAURANT.restaurant_cuisines()

    #  customer methods
    print("\nCustomer methods:")
    RESTAURANT.customers[0].explore_the_menu()
    print(f"In {RESTAURANT.customers[0].name}'s order:")
    RESTAURANT.customers[0].dishes_in_order()
    print(f"The client paid {RESTAURANT.customers[0].pay(520)} UAH.")
    RESTAURANT.customers[0].order.add_new_dish(dish=Dish.items[0])
    print(f"Now in {RESTAURANT.customers[0].name}'s order:")
    RESTAURANT.customers[0].dishes_in_order()

    #  deliveryman methods
    print("\nDeliveryman methods:")
    print(RESTAURANT.deliveries[0].pick_up_order(order=Order(2, [0, 1], "Formed")))
    print(RESTAURANT.deliveries[0].deliver_the_order(2))
    print(RESTAURANT.deliveries[0].orders)
    RESTAURANT.deliveries[0].change_car(car=Car("HM5489KE", 10, "gas"))
    print(RESTAURANT.deliveries[0].give_change(RESTAURANT.deliveries[0].get_paid(580), 460))
    RESTAURANT.deliveries[0].get_salary(8300)
    RESTAURANT.deliveries[0].salary_increase()

    #  car methods
    print("\nCar methods:")
    RESTAURANT.deliveries[0].car.car_description()
    RESTAURANT.deliveries[0].car.drive()
    RESTAURANT.deliveries[0].car.refuel()
    RESTAURANT.deliveries[0].car.fix()

    #  promotion methods
    print("\nPromotion methods:")
    RESTAURANT.promotions[0].start()
    RESTAURANT.promotions[0].run()
    RESTAURANT.promotions[0].stop()

    #  supplier methods
    print("\nSupplier methods:")
    RESTAURANT.suppliers[0].accept_order({"carrot": 5, "flour": 8, "lemon": 4})
    RESTAURANT.suppliers[0].deliver_products(0)
    RESTAURANT.suppliers[0].get_salary(8500)
    RESTAURANT.suppliers[0].salary_increase()

    #  waiter methods
    print("\nWaiter methods:")
    RESTAURANT.waiters[0].accept_order(order=RESTAURANT.customers[0].order)
    RESTAURANT.waiters[0].bring_the_order(2)
    RESTAURANT.waiters[0].work()
    print(RESTAURANT.waiters[0].give_change(RESTAURANT.waiters[0].get_paid(850), 700))
    RESTAURANT.waiters[0].get_salary(9800)
    RESTAURANT.waiters[0].salary_increase()

    #  order methods
    print("\nOrder methods:")
    print(RESTAURANT.customers[0].order.order_price_calculation())
    RESTAURANT.customers[0].order.del_dish(1)
    RESTAURANT.customers[0].order.add_new_dish(dish=Dish("ice", 25, 250, {"ice": 250}, "cook"))
    print(RESTAURANT.customers[0].order.order_price_calculation())
    RESTAURANT.customers[0].order.cancel_the_order()
    print(f"Order status is '{RESTAURANT.customers[0].order.order_status}'.")
