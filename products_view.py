from typing import Callable, Any

from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QStackedWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize, Qt

from product_model import ProductModel


class ProductsView(QStackedWidget):
    def __init__(self):
        super().__init__()

        self._category_indexes: dict[str, int] = {}

    def add_products(self, products: list[ProductModel], callback: Callable[[ProductModel], None]):
        category_products = {}

        for product in products:
            if product.category not in category_products:
                category_products[product.category] = []
            category_products[product.category].append(product)

        current_index = 0
        for category, products in category_products.items():
            product_category_view = ProductCategoryView()
            product_category_view.add_products(products, callback)
            self.addWidget(product_category_view)

            self._category_indexes[category] = current_index
            current_index += 1

    def set_current_category(self, category_name: str):
        self.setCurrentIndex(self._category_indexes[category_name])


class ProductCategoryView(QWidget):
    def __init__(self):
        super().__init__()

        self._layout = QHBoxLayout()
        self.setLayout(self._layout)

    def add_products(self, products: list[ProductModel], callback: Callable[[ProductModel], None]):
        for product in products:
            product_view = ProductView(product)
            self._layout.addWidget(product_view)
            product_view.clicked.connect(lambda e=None, p=product: callback(p))


class ProductView(QPushButton):
    def __init__(self, product: ProductModel):
        super().__init__()

        self._layout = QVBoxLayout()
        self._layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self._layout)

        self._image_label = QLabel()
        pixmap = QPixmap(product.image_path)
        pixmap = pixmap.scaledToHeight(100)
        self._image_label.setPixmap(pixmap)
        self._layout.addWidget(self._image_label, alignment=Qt.AlignCenter)

        self._name_label = QLabel(product.name)
        self._layout.addWidget(self._name_label, alignment=Qt.AlignCenter)

        self._is_vegetarian_label = QLabel(f'Vegetarian: {"✓" if product.is_vegetarian else "❌"}')
        self._layout.addWidget(self._is_vegetarian_label, alignment=Qt.AlignCenter)

        self._is_vegan_label = QLabel(f'Vegan: {"✓" if product.is_vegan else "❌"}')
        self._layout.addWidget(self._is_vegan_label, alignment=Qt.AlignCenter)

    def sizeHint(self) -> QSize:
        return QSize(150, 200)