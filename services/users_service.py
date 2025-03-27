import logging

from controllers.users_controller import UserController
from models.user import User
from utils.mappers.users_mapper import map_users_from_data, map_user_from_data


def save_users_to_file(users):
    with open("user_output.txt", "w") as file:
        file.write(f"{users !r}")

    print("Output has been saved to user_output.txt")


class UserService:
    user_controller = UserController()

    def fetch_all_users_info(self, page_limit: int, limit: int) -> list[User]:
        all_users = []
        skip = 0
        total_users = 0

        while total_users < page_limit * limit:
            user_data = self.user_controller.get_users_info(skip, limit)
            if user_data and user_data["users"]:
                all_users.extend(map_users_from_data(user_data["users"]))
                logging.info(f"Range: {skip} - {skip + limit}")
                skip += limit
                total_users += len(user_data["users"])
            else:
                break
        return all_users

    def fetch_user_info(self, user_id: int) -> User | None:
        user_data = self.user_controller.get_all_users_info()
        if user_data and user_data["users"]:
            user_list = user_data["users"]
            for user in user_list:
                if user["id"] == user_id:
                    return map_user_from_data(user)
            print(f"User ID {user_id} not found.")
        else:
            print("Failed to fetch user data")
        return None
