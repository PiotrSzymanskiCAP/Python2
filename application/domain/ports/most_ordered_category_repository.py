from abc import ABC, abstractmethod
from typing import Dict


class MostOrderedCategoryRepository(ABC):
    @abstractmethod
    def get_most_ordered_category_by_user(self) -> Dict[int, str]:
        pass
