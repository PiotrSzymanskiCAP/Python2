import logging

from controllers.user_controller import UserController
from models.user import User


class UserService:
    user_controller = UserController()

    def fetch_all_users_info(self, page_limit, limit):
        all_users = []
        skip = 0
        total_users = 0

        while total_users < page_limit * limit:
            user_data = self.user_controller.get_user_info(skip, limit)
            if user_data and user_data["users"]:
                all_users.extend(self.fetch_users_from_data(user_data["users"]))
                logging.info(f"Range: {skip} - {skip + limit}")
                skip += limit
                total_users += len(user_data["users"])
            else:
                break
        return all_users

    def fetch_user_info(self, user_id):
        user_data = self.user_controller.get_user_info()
        if user_data:
            user_dict = {user["id"]: user for user in user_data["users"]}
            if user_id in user_dict:
                print(user_dict[user_id]["firstName"])
            else:
                print(f"User ID {user_id} not found.")
        else:
            print("Failed to fetch user data")

    def fetch_users_from_data(self, user_data):
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
