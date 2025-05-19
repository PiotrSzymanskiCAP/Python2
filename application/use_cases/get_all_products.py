from typing import List

from application.domain.models.pydantic_models import Product
from application.domain.ports.product_repository import ProductRepository


class GetAllProductsUseCase:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def execute(self) -> List[Product]:
        return self.product_repository.get_all()
