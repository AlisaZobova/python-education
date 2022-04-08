""""Class promotion"""


class Promotion:
    """Class for storing information about promotions"""
    promotions = []

    def __init__(self, promo_name: str, terms: str, description: str, status: str):
        """Class constructor"""
        self.promo_name = promo_name
        self.terms = terms
        self.description = description
        self.status = status
        Promotion.promotions.append(self)

    def start(self):
        """Informs about the start of the promotion"""
        self.status = "has started"
        print(f"Promotion '{self.promo_name}' {self.status}! "
              f"{self.description}")

    def run(self):
        """Notifies that a promotion is running"""
        self.status = "is running"
        print(f"Promotion '{self.promo_name}' {self.status}... "
              f"It's terms: {self.terms}.")

    def stop(self):
        """Informs that the promotion has ended"""
        self.status = "has stopped"
        print(f"Promotion '{self.promo_name}' {self.status}!")
