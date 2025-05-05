from dataclasses import dataclass


@dataclass
class Car:
    fuel_price: float
    brand: str
    fuel_consumption: float

    @staticmethod
    def calculate_fuel_cost(
            fuel_consumption: float,
            distance: float,
            fuel_price: float
    ) -> float:
        return (fuel_consumption * distance / 100) * fuel_price
