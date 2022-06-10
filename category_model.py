class CategoryModel:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def image_path(self):
        formatted_name = self.name.lower()
        return './images/' + formatted_name + '/' + formatted_name + '.jpg'
