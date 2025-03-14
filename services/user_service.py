import logging

from controllers.user_controller import UserController
import json

class UserService:
    user_controller = UserController()


    def fetch_all_user(self):
        user_data = self.user_controller.get_user_info()
        print(user_data)
        print(len(user_data["users"]))

    def fetch_all_users_info(self,page_limit, limit=10):
        all_users = []
        page = 1
        while page <= page_limit:
            user_data = self.user_controller.get_user_info(page, limit)
            if user_data and user_data['users']:
                all_users.extend(user_data['users'])
                logging.info(f"Page: {page}")
                page += 1
            else:
                break
        return all_users



    def fetch_user_info(self, user_id):
        user_data = self.user_controller.get_user_info()
        if user_data:
            user_dict = {user['id']: user for user in user_data['users']}
            if user_id in user_dict:
                print(user_dict[user_id]["firstName"])
            else:
                print(f"User ID {user_id} not found.")
        else:
            print("Failed to fetch user data")