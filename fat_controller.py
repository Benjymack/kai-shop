import json

from category.category_controller import CategoryController
from category.category_model import CategoryModel
from category.category_view import CategoriesView

from product.product_controller import ProductController
from product.product_model import ProductModel
from product.product_view import ProductsView

from order.order_controller import OrderController
from order.order_model import OrderModel
from order.order_view import OrderView


class FatController:
    def __init__(self, categories_view: CategoriesView, products_view: ProductsView, order_view: OrderView,
                 order_model: OrderModel):
        self._categories_view = categories_view
        self._products_view = products_view
        self._order_view = order_view
        self._order_model = order_model

        self._product_controller = ProductController(self._products_view)
        self._category_controller = CategoryController(self._categories_view,
                                                       self._product_controller.set_current_category)
        self._order_controller = OrderController(self._order_view, self._order_model)

    def initialise(self):
        self._load_products_from_file()
        self._category_controller.initialise()
        self._product_controller.initialise_categories(self._order_controller.add_product)

    def _load_products_from_file(self):
        with open('menu.json', 'r', encoding='utf-8') as file:
            json_products = json.load(file)

        categories = set()

        for json_product in json_products:
            self._product_controller.add_product(ProductModel(**json_product))
            categories.add(json_product['category'])

        for category in categories:
            self._category_controller.add_category(CategoryModel(category))
