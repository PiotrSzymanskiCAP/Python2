from typing import List

from sqlalchemy.orm import Session

from adapters.database.product_entity import ProductEntity
from application.domain.models.pydantic_models import Product
from application.domain.ports.product_repository import ProductRepository


class SqlAlchemyProductRepository(ProductRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Product]:
        products = self.session.query(ProductEntity).all()
        return [Product.model_validate(p) for p in products]
