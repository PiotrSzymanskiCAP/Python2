from typing import List

from application.domain.models.pydantic_models import Cart
from application.domain.ports.cart_repository import CartRepository


class GetAllCartsUseCase:
    def __init__(self, cart_repository: CartRepository):
        self.cart_repository = cart_repository

    def execute(self) -> List[Cart]:
        return self.cart_repository.get_all()
