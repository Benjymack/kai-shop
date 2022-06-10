from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout

from categories_view import CategoriesView

from order_model import OrderModel
from order_view import OrderView

from products_view import ProductsView

from fat_controller import FatController


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._order_model = OrderModel()

        self._categories_view = CategoriesView()
        self._products_view = ProductsView()
        self._order_view = OrderView()

        self._fat_controller = FatController(self._categories_view, self._products_view, self._order_view,
                                             self._order_model)

        self.setWindowTitle("Kai")

        self._main_widget = QWidget()
        self._layout = QHBoxLayout()
        self._main_widget.setLayout(self._layout)
        self.setCentralWidget(self._main_widget)

        self._layout.addWidget(self._categories_view)
        self._layout.addWidget(self._products_view)
        self._layout.addWidget(self._order_view)

        self._fat_controller.initialise()


if __name__ == '__main__':
    app = QApplication()
    main = MainWindow()
    main.show()
    app.exec()
