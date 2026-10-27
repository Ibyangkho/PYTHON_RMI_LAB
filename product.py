"""product.py - Equivalent of Product.java (remote interface)."""
from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def get_name(self) -> str: ...

    @abstractmethod
    def get_description(self) -> str: ...

    @abstractmethod
    def get_price(self) -> float: ...