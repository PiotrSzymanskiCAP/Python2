from typing import List

from application.domain.models.pydantic_models import BoughtProduct
from application.domain.ports.bought_product_repository import BoughtProductRepository


class GetAllBoughtProductsUseCase:
    def __init__(self, bought_product_repository: BoughtProductRepository):
        self.bought_product_repository = bought_product_repository

    def execute(self) -> List[BoughtProduct]:
        return self.bought_product_repository.get_all()
