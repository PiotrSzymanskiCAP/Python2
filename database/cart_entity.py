from sqlalchemy import JSON, Integer, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column

from database.db import Base
from models.product import Product


class CartEntity(Base):
    __tablename__ = "carts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cart_id: Mapped[int]
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.user_id"), nullable=False
    )
    products: Mapped[dict] = mapped_column(JSON, nullable=False)

    def __init__(self, cart_id: int, user_id: int, products: dict):
        self.cart_id = cart_id
        self.user_id = user_id
        self.products = products

    def __repr__(self):
        return f"{self.id} | Cart with ID: {self.cart_id} -> User ID: {self.user_id} Products(ID's, Quantity): {self.products}\n"

    @hybrid_property
    def product_ids(self):
        return list(self.products.keys())

    @product_ids.expression
    def product_ids(self):
        return self.products.keys()

    def get_products(self, session):
        return (
            session.query(Product)
            .filter(Product._product_id.in_(self.product_ids))
            .all()
        )
