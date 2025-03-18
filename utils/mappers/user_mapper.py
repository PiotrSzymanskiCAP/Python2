from models.user import User


def map_users_from_data(user_data: list[dict]) -> list[User]:
    all_users = []
    for user in user_data:
        new_user = User(
            user["id"],
            user["firstName"],
            user["lastName"],
            user["age"],
            user["address"]["coordinates"]["lat"],
            user["address"]["coordinates"]["lng"],
        )
        all_users.append(new_user)
    return all_users
