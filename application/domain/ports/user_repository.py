from abc import ABC, abstractmethod
from typing import List

from application.domain.models.pydantic_models import User


class UserRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[User]:
        pass
