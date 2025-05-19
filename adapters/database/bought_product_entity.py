from sqlalchemy.orm import Mapped, mapped_column

from adapters.database.db import Base


class BoughtProductEntity(Base):
    __tablename__ = "bought_products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cart_id: Mapped[int]
    product_id: Mapped[int]
    quantity: Mapped[int]

    def __init__(self, cart_id: int, product_id: int, quantity: int):
        self.cart_id = cart_id
        self.product_id = product_id
        self.quantity = quantity

    def __str__(self):
        return (
            f"{self.id} | Cart with ID: {self.cart_id} -> Bought product ID: {self.product_id}, "
            f"Quantity: {self.quantity} \n"
        )

    def __repr__(self):
        return (
            f"BoughtProductEntity(id={self.id}, cart_id={self.cart_id}, "
            f"product_id={self.product_id}, quantity={self.quantity})"
        )
