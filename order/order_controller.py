from .order_model import OrderModel
from .order_view import OrderView
from product.product_model import ProductModel


class OrderController:
    def __init__(self, order_view: OrderView, order_model: OrderModel):
        self._order_model = order_model
        self._order_view = order_view

        self._order_view.set_order_callback(self.order_clicked)

    def get_order_total(self):
        return self._order_model.get_order_total()

    def get_order_items(self):
        return self._order_model.get_order_items()

    def remove_order_item(self, order_item_id: int):
        self._order_model.remove_order_item(order_item_id)
        self._order_view.update_order(self._order_model, self.remove_order_item)

    def add_product(self, product: ProductModel):
        self._order_model.add_order_item(product)
        self._order_view.update_order(self._order_model, self.remove_order_item)

    def order_clicked(self):
        self._order_model.clear_all_items()
        self._order_view.update_order(self._order_model, self.remove_order_item)
