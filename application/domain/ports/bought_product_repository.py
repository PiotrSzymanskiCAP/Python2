from abc import ABC, abstractmethod
from typing import List

from application.domain.models.pydantic_models import BoughtProduct


class BoughtProductRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[BoughtProduct]:
        pass
