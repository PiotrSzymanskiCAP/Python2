from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    product_id: int
    title: str
    price: float
    category: str

    def __str__(self):
        return f"Product with ID: {self.product_id} -> {self.title} Price: {self.price} Category: {self.category}"

    def __repr__(self):
        return (
            f"Product(product_id={self.product_id}, title={self.title!r}, "
            f"price={self.price}, category={self.category!r})"
        )
