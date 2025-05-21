from typing import Dict

from application.domain.ports.most_ordered_category_repository import (
    MostOrderedCategoryRepository,
)


class GetMostOrderedCategoryUseCase:
    def __init__(self, repository: MostOrderedCategoryRepository):
        self.repository = repository

    def execute(self) -> Dict[int, str]:
        return self.repository.get_most_ordered_category_by_user()
