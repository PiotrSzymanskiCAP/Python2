from typing import List

from adapters.database.bought_product_entity import BoughtProductEntity
from application.domain.models.pydantic_models import BoughtProduct


class SqlAlchemyBoughtProductRepository:
    def __init__(self, session):
        self.session = session

    def get_all(self) -> List[BoughtProduct]:
        bought_products = self.session.query(BoughtProductEntity).all()
        return [BoughtProduct.model_validate(bp) for bp in bought_products]
