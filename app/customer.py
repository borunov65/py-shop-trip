from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int | float
    car: dict

    @staticmethod
    def calculate_distance(location1: list, location2: list) -> float:
        return ((location1[0] - location2[0]) ** 2
                + (location1[1] - location2[1]) ** 2) ** 0.5
