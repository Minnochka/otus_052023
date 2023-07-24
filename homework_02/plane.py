"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload
class Plane(Vehicle):
    cargo:int
    max_cargo:int
    def __init__(self, weight: int, fuel: int, fuel_consumption: int, max_cargo: int):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, cargo:int):
        if self.cargo + cargo <= self.max_cargo:
            self.cargo += cargo
        else:
            raise CargoOverload(cargo)

    def remove_all_cargo(self) -> int:
        old_cargo, self.cargo = self.cargo, 0
        return old_cargo


