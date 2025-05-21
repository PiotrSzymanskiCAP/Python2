from typing import List

from sqlalchemy.orm import Session

from adapters.database.user_entity import UserEntity
from application.domain.models.pydantic_models import User
from application.domain.ports.user_repository import UserRepository


class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[User]:
        users = self.session.query(UserEntity).all()
        return [User.model_validate(u) for u in users]
