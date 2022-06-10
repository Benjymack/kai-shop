from typing import Optional


class ProductModel:
    def __init__(self, name: str, is_vegetarian: bool, is_vegan: bool, contains_sugar: bool, price: float,
                 image_path: str, category: str, day: Optional[str] = None):
        self._name = name
        self._is_vegetarian = is_vegetarian
        self._is_vegan = is_vegan
        self._contains_sugar = contains_sugar
        self._price = price
        self._image_path = image_path
        self._category = category
        self._day = day

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_vegetarian(self) -> bool:
        return self._is_vegetarian

    @property
    def is_vegan(self) -> bool:
        return self._is_vegan

    @property
    def contains_sugar(self) -> bool:
        return self._contains_sugar

    @property
    def price(self) -> float:
        return self._price

    @property
    def image_path(self) -> str:
        return self._image_path

    @property
    def category(self) -> str:
        return self._category

    @property
    def day(self):
        return self._day

    def __hash__(self):
        return hash(repr(self))

    def __str__(self):
        return f"{self._name} ({self._category})"
