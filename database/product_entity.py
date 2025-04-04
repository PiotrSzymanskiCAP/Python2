from sqlalchemy.orm import Mapped, mapped_column

from database.db import Base


class ProductEntity(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_id: Mapped[int]
    title: Mapped[str]
    price: Mapped[float]
    category: Mapped[str]

    def __init__(
            self,
            product_id: int,
            title: str,
            price: float,
            category: str,
    ):
        self.product_id = product_id
        self.title = title
        self.price = price
        self.category = category

    def __repr__(self):
        return f"{self.id} | Product with ID: {self.product_id} -> {self.title} Price: {self.price} Category: {self.category}\n"
