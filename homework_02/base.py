from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 100
    started = False
    fuel = 200
    fuel_consumption = 0
    def __init__(self, weight:int, fuel:int, fuel_consumption:int):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError


    def move(self, distance:int):
        if self.fuel - distance * self.fuel_consumption >= 0:
            self.fuel -= distance * self.fuel_consumption
        else:
            raise NotEnoughFuel(distance)
