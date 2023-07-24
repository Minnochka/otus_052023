"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    def __init__(self):
        super().__init__("Low Fuel")

    """def __str__(self):
        return "Недостаточно топлива для старта"""

class NotEnoughFuel(Exception):
    def __init__(self, distance = 0):
        super().__init__("Not Enough Fuel")
        self.distance = distance

    """def __str__(self):
        return f"Недостаточно топлива для поездки на {self.distance} км."""

class CargoOverload(Exception):
    def __init__(self, cargo = 0):
        super().__init__("Cargo overload")
        self.cargo = cargo

    """def __str__(self):
        return f"Недостаточно места для загрузки еще {self.cargo} кг"""