from typing import List

from application.domain.models.pydantic_models import User
from application.domain.ports.user_repository import UserRepository


class GetAllUsersUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self) -> List[User]:
        return self.user_repository.get_all()
