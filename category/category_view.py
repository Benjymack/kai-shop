from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize, Qt

from .category_model import CategoryModel


class CategoriesView(QWidget):
    def __init__(self):
        super().__init__()

        self._layout = QVBoxLayout()
        self.setLayout(self._layout)

        self._category_views = []

    def setup_categories(self, categories: dict[str, CategoryModel]) -> list[tuple[CategoryModel, 'CategoryView']]:
        for _, widget in self._category_views:
            self._layout.removeWidget(widget)
            widget.deleteLater()

        self._category_views = []

        for category in categories.values():
            category_view = CategoryView(category)
            self._layout.addWidget(category_view)
            self._category_views.append((category, category_view))

        return self._category_views


class CategoryView(QPushButton):
    def __init__(self, category: CategoryModel):
        super().__init__()

        self._category = category

        self._layout = QVBoxLayout()
        self.setLayout(self._layout)

        self._label = QLabel(self._category.name)
        self._layout.addWidget(self._label, alignment=Qt.AlignCenter)

        self.setCheckable(True)

        pixmap = QPixmap(self._category.image_path)
        if not pixmap.isNull():
            pixmap = pixmap.scaledToHeight(100)
            self._image_label = QLabel()
            self._image_label.setPixmap(pixmap)
            self._layout.addWidget(self._image_label, alignment=Qt.AlignCenter)

    def sizeHint(self) -> QSize:
        return QSize(150, 150)
