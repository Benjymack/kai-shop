from product.product_model import ProductModel
from dataclasses import dataclass


class OrderModel:
    def __init__(self):
        self._order_items: list[OrderItem] = []

    def add_order_item(self, product: ProductModel, count: int = 1):
        for order_item in self._order_items:
            if order_item.product == product:
                order_item.count += count
                return
        self._order_items.append(OrderItem(product, count))

    def get_order_total(self) -> float:
        total = 0
        for order_item in self._order_items:
            total += order_item.product.price * order_item.count
        return total

    def get_order_items(self) -> list['OrderItem']:
        return self._order_items

    def clear_all_items(self):
        self._order_items = []

    def remove_order_item(self, order_item_id: int):
        del self._order_items[order_item_id]


@dataclass
class OrderItem:
    _product: ProductModel
    _count: int

    @property
    def product(self):
        return self._product

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, new_count: int):
        self._count = new_count
