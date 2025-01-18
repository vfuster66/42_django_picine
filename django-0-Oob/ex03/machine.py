import random
from beverages import HotBeverage


class CoffeeMachine:
    def __init__(self):
        """Initialise la machine et le compteur de boissons servies."""
        self.is_broken = False
        self.counter = 0

    class EmptyCup(HotBeverage):
        def __init__(self):
            """Initialise une tasse vide avec des propriétés spécifiques."""
            super().__init__()
            self.name = "empty cup"
            self.price = 0.90

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            """Initialise une exception avec un message personnalisé."""
            super().__init__("This coffee machine has to be repaired.")

    def serve(self, beverage_class):
        """Retourne une boisson ou une tasse vide, ou lève une exception
        si la machine est cassée."""
        if self.is_broken:
            raise CoffeeMachine.BrokenMachineException()
        if self.counter >= 10:
            self.is_broken = True
            raise CoffeeMachine.BrokenMachineException()

        self.counter += 1
        if random.choice([True, False]):
            return beverage_class()
        else:
            return CoffeeMachine.EmptyCup()

    def repair(self):
        """Répare la machine."""
        self.is_broken = False
        self.counter = 0
