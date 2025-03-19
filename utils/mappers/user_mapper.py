from database.user_entity import UserEntity
from models.user import User


def map_users_from_data(user_data: list[dict]) -> list[User]:
    all_users = []
    for user in user_data:
        new_user = map_user_from_data(user)
        all_users.append(new_user)
    return all_users


def map_user_from_data(user) -> User:
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
        str(user._uuid),
        user._id,
        user._first_name,
        user._last_name,
        user._age,
        user._lat,
        user._lng,
        user._country,
    )
