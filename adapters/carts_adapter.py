import logging
from typing import Dict, Any

import requests


class CartsAdapter:
    base_url = "https://dummyjson.com/"
    endpoint = "carts"

    def get_carts_info(self, skip: int, limit: int) -> Dict[str, Any]:
        url = f"{self.base_url}{self.endpoint}?skip={skip}&limit={limit}"
        response = requests.get(url)

        if response.status_code == 200:
            logging.info("Successfully fetched carts data")
            return response.json()

        else:
            logging.error("Request failed to fetch data")
