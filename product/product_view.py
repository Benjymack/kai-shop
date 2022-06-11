from typing import Callable

from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QStackedWidget, \
    QVBoxLayout, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize, Qt

from .product_model import ProductModel


class ProductsView(QStackedWidget):
    def __init__(self):
        super().__init__()

        self._category_indexes: dict[str, int] = {}

    def add_products(self, products: list[ProductModel], callback: Callable[[ProductModel], None]):
        category_products = {}
        self._category_indexes = {}

        current_category_index = self.currentIndex()

        while self.count() > 0:
            widget = self.widget(0)
            self.removeWidget(widget)
            widget.deleteLater()

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

        self.setCurrentIndex(current_category_index)

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
        self._add_widget(self._image_label)

        self._name_label = QLabel(product.name)
        self._add_widget(self._name_label)

        self._is_vegetarian_label = QLabel(f'Vegetarian: {"✓" if product.is_vegetarian else "❌"}')
        self._add_widget(self._is_vegetarian_label)

        self._is_vegan_label = QLabel(f'Vegan: {"✓" if product.is_vegan else "❌"}')
        self._add_widget(self._is_vegan_label)

        self._sugar_label = QLabel(f'Added Sugar: {"✓" if product.contains_sugar else "❌"}')
        self._add_widget(self._sugar_label)

        if product.country is not None:
            self._country_label = QLabel(product.country)
            self._add_widget(self._country_label)

        self._cost_label = QLabel(f'${product.price:.2f}')
        self._add_widget(self._cost_label)

    def sizeHint(self) -> QSize:
        return QSize(150, 200)

    def _add_widget(self, widget: QWidget):
        self._layout.addWidget(widget, alignment=Qt.AlignCenter)
