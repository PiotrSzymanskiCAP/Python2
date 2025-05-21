from typing import List

from sqlalchemy.orm import Session

from adapters.database.cart_entity import CartEntity
from application.domain.models.pydantic_models import Cart
from application.domain.ports.cart_repository import CartRepository


class SqlAlchemyCartRepository(CartRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Cart]:
        carts = self.session.query(CartEntity).all()
        return [Cart.model_validate(c) for c in carts]
