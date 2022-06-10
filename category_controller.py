from typing import Optional, Callable

from category_model import CategoryModel
from categories_view import CategoriesView, CategoryView


class CategoryController:
    def __init__(self, categories_view: CategoriesView, category_changed_function: Callable[[str], None]):
        self._categories_view = categories_view

        self._categories: dict[str, CategoryModel] = {}
        self._current_category_name: Optional[str] = None

        self._category_views: list[tuple[CategoryModel, CategoryView]] = []
        self._category_changed_function = category_changed_function

    def get_category_names(self) -> list[str]:
        return list(self._categories.keys())

    def add_category(self, category: CategoryModel):
        self._categories[category.name] = category

    def set_current_category_name(self, category_name: Optional[str]):
        self._current_category_name = category_name

        for category, view in self._category_views:
            view.setChecked(category.name == self._current_category_name)

        self._category_changed_function(self._current_category_name)

    def initialise(self):
        self._category_views = self._categories_view.setup_categories(self._categories)

        for category, view in self._category_views:
            view.clicked.connect(
                lambda e=None, category_name=category.name: self.set_current_category_name(category_name))
