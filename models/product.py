import uuid


class Product:

    def __init__(self, id: int, title: str, price: float, category: str):
        self._uuid = uuid.uuid4()
        self._id = id
        self._title = title
        self._price = price
        self._category = category

    def __repr__(self):
        return f"Product with ID: {self._id} -> {self._title} Price: {self._price} Category: {self._category}\n"
