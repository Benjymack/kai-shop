from typing import Callable

from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, \
    QVBoxLayout, QComboBox
from PySide6.QtCore import QSize

from .order_model import OrderModel


DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']


class OrderView(QWidget):
    def __init__(self):
        super().__init__()

        self._layout = QVBoxLayout()
        self.setLayout(self._layout)

        self._current_day_select = QComboBox()
        self._current_day_select.addItems(DAYS)
        self._layout.addWidget(self._current_day_select)

        self._order_items_layout = QGridLayout()
        self._layout.addLayout(self._order_items_layout)

        self._layout.addStretch()
        
        self._total_label = QLabel()
        self._layout.addWidget(self._total_label)

        self._order_button = QPushButton('Submit Order')
        self._layout.addWidget(self._order_button)

        self._remove_item_callback = lambda x: None

    def update_order(self, order_model: OrderModel):
        order_items = order_model.get_order_items()

        while True:
            widget = self._order_items_layout.takeAt(0)
            if widget is None:
                break
            widget.widget().deleteLater()

        for current_row, order_item in enumerate(order_items):
            product_name_label = QLabel(order_item.product.name)
            self._order_items_layout.addWidget(product_name_label,
                                               current_row, 0)

            product_quantity_label = QLabel(f'x{order_item.count}')
            self._order_items_layout.addWidget(product_quantity_label,
                                               current_row, 1)

            product_price_label = QLabel(f'${order_item.product.price:.2f}')
            self._order_items_layout.addWidget(product_price_label,
                                               current_row, 2)

            remove_button = QPushButton('-')
            remove_button.setFixedSize(QSize(20, 20))
            remove_button.clicked.connect(
                lambda e=None, r=current_row: self._remove_item_callback(r))
            self._order_items_layout.addWidget(remove_button, current_row, 3)

        self._total_label.setText(
            f'Total: ${order_model.get_order_total():.2f}')

    def set_order_callback(self,
                           order_clicked_callback: Callable[[bool], None]):
        self._order_button.clicked.connect(order_clicked_callback)

    def set_remove_item_callback(self,
                                 remove_item_callback: Callable[[int], None]):
        self._remove_item_callback = remove_item_callback

    def set_day_callback(self, day_callback: Callable[[str], None]):
        self._current_day_select.currentTextChanged.connect(day_callback)
        self._current_day_select.setCurrentIndex(0)  # TODO: Side effect
        day_callback(self._current_day_select.currentText())
