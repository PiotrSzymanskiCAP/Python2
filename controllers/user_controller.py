import requests
import logging

class UserController:

    base_url ="https://dummyjson.com/"
    endpoint = "users"


    def get_user_info(self, page=1, limit=10):
        url = f"{self.base_url}{self.endpoint}?page={page}&limit={limit}"
        response = requests.get(url)

        if response.status_code == 200:
            logging.info("Successfully fetched data")
            return response.json()

        else:
            logging.info("Request failed to fetch data")

    def get_all_user_info(self):
        url = f"{self.base_url}{self.endpoint}"
        response = requests.get(url)

        if response.status_code == 200:
            logging.info("Successfully fetched data")
            return response.json()

        else:
            logging.info("Request failed to fetch data")

    def get_pages(self, response):
        return response["info"]["pages"]