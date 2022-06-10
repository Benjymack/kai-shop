from typing import Optional, Callable

from product_model import ProductModel
from products_view import ProductsView


class ProductController:
    def __init__(self, products_view: ProductsView):
        self._products_view = products_view

        self._products: list[ProductModel] = []
        self._current_category_name: Optional[str] = None

    def set_current_category(self, category_name: str):
        self._current_category_name = category_name
        self._products_view.set_current_category(self._current_category_name)

    def _get_current_category_products(self) -> list[ProductModel]:
        return [product for product in self._products if product.category == self._current_category_name]

    def add_product(self, product: ProductModel):
        self._products.append(product)

    def get_category_names(self) -> list[str]:
        return list(set(product.category for product in self._products))

    def initialise_categories(self, callback: Callable[[ProductModel], None]):
        self._products_view.add_products(self._products, callback)
