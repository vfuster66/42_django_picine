import random
from machine import CoffeeMachine
from beverages import Coffee, Tea, Chocolate, Cappuccino

if __name__ == "__main__":
    machine = CoffeeMachine()

    for _ in range(15):  # Essayer de servir plus de 10 boissons
        try:
            drink = machine.serve(
                random.choice([Coffee, Tea, Chocolate, Cappuccino])
            )
            print(drink)
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            print("Réparation en cours...")
            machine.repair()
        except Exception as e:
            print(f"Erreur inattendue : {e}")
