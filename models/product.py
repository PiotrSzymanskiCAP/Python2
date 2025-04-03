class Product:

    def __init__(self, _product_id: int, title: str, price: float, category: str):
        self._product_id = _product_id
        self._title = title
        self._price = price
        self._category = category

    def __repr__(self):
        return f"Product with ID: {self._product_id} -> {self._title} Price: {self._price} Category: {self._category}\n"
