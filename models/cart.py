from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class Cart:
    cart_id: int
    user_id: int
    products: Dict[int, int]

    def __str__(self):
        return (
            f"Cart with ID: {self.cart_id}, for user with ID: {self.user_id} -> "
            f"Products(ID, Quantity) {self.products!r}"
        )

    def __repr__(self):
        return f"Cart(cart_id={self.cart_id}, user_id={self.user_id}, products={self.products})"
