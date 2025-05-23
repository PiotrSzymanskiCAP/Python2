from adapters.database.user_entity import UserEntity
from application.domain.models.user import User


def map_users_from_data(user_data: list[dict]) -> list[User]:
    all_users = []
    for user in user_data:
        new_user = map_user_from_data(user)
        all_users.append(new_user)
    return all_users


def map_user_from_data(user: dict) -> User:
    return User(
        user["id"],
        user["firstName"],
        user["lastName"],
        user["age"],
        user["address"]["coordinates"]["lat"],
        user["address"]["coordinates"]["lng"],
    )


def map_user_to_entity(user: User) -> UserEntity:
    return UserEntity(
        user.user_id,
        user.first_name,
        user.last_name,
        user.age,
        user.latitude,
        user.longitude,
        user._country,
    )
