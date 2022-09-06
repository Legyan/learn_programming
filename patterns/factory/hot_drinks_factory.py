from abc import ABC, abstractmethod
from enum import Enum


class HotDrink(ABC):

    @abstractmethod
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('Very tasty tea!')


class Coffee(HotDrink):
    def consume(self):
        print('Very tasty coffee!')


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water, '
              f'pour {amount}ml, enjoy!')


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind sme beans, boil water, '
              f'pour {amount}ml, enjoy!')


class HotDrinkMachine:

    class AvailableDrinks(Enum):
        COFFEE = 1
        TEA = 2

    factories = {}
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for drink in self.AvailableDrinks:
                factory_name = drink.name.title() + 'Factory'
                self.factories[drink] = eval(factory_name)()

    def print_drinks(self) -> None:
        print('Drinks:')
        num = 0
        for drink in self.AvailableDrinks:
            print(f"{drink.value}. {drink.name}")
            num += 1

    def choose_drink(self) -> int:
        lf = len(self.AvailableDrinks)
        return int(input(f'Choose drink (1–{lf}): '))

    @staticmethod
    def choose_amount() -> int:
        return int(input('How much (ml): '))

    def make_drink(self):
        self.print_drinks()
        idx = self.choose_drink()
        amount = self.choose_amount()
        return self.factories[self.AvailableDrinks(idx)].prepare(amount)


if __name__ == '__main__':
    hdm = HotDrinkMachine()
    hdm.make_drink()
