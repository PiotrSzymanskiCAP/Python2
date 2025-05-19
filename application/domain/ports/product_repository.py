from abc import ABC, abstractmethod
from typing import List

from application.domain.models.pydantic_models import Product


class ProductRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Product]:
        pass
