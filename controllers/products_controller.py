import logging

import requests


class ProductsController:
    base_url = "https://dummyjson.com/"
    endpoint = "products"

    def get_products_info(self, skip: int, limit: int):
        url = f"{self.base_url}{self.endpoint}?skip={skip}&limit={limit}"
        response = requests.get(url)

        if response.status_code == 200:
            logging.info("Successfully fetched products data")
            return response.json()

        else:
            logging.info("Request failed to fetch data")
