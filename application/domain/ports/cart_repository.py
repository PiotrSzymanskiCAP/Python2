from abc import ABC, abstractmethod
from typing import List

from application.domain.models.pydantic_models import Cart


class CartRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Cart]:
        pass
