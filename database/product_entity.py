from sqlalchemy.orm import Mapped, mapped_column

from database.db import Base


class ProductEntity(Base):
    __tablename__ = "products"

    uuid: Mapped[str] = mapped_column(primary_key=True)
    id: Mapped[int]
    title: Mapped[str]
    price: Mapped[float]
    category: Mapped[str]

    def __init__(
            self,
            uuid: str,
            id: int,
            title: str,
            price: float,
            category: str,
    ):
        self.uuid = uuid
        self.id = id
        self.title = title
        self.price = price
        self.category = category

    def __repr__(self):
        return f"{self.uuid} | Product with ID: {self.id} -> {self.title} Price: {self.price} Category: {self.category}\n"
