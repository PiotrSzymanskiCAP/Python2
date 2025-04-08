import logging

import requests


# connector / ADAPTER


class CartsAdapter:
    base_url = "https://dummyjson.com/"
    endpoint = "carts"

    def get_carts_info(self, skip: int, limit: int):
        url = f"{self.base_url}{self.endpoint}?skip={skip}&limit={limit}"
        response = requests.get(url)

        if response.status_code == 200:
            logging.info("Successfully fetched carts data")
            return response.json()

        else:
            logging.info("Request failed to fetch data")
