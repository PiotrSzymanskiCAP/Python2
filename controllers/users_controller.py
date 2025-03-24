import logging

import requests


class UserController:
    base_url = "https://dummyjson.com/"
    endpoint = "users"

    def get_users_info(self, skip: int, limit: int):
        url = f"{self.base_url}{self.endpoint}?skip={skip}&limit={limit}"
        response = requests.get(url)

        if response.status_code == 200:
            logging.info("Successfully fetched users data")
            return response.json()

        else:
            logging.info("Request failed to fetch data")

    def get_all_users_info(self):
        url = f"{self.base_url}{self.endpoint}"
        response = requests.get(url)

        if response.status_code == 200:
            logging.info("Successfully fetched users data")
            return response.json()

        else:
            logging.info("Request failed to fetch data")
