import logging

from controllers.products_controller import ProductsController
from models.product import Product
from utils.mappers.products_mapper import map_product_from_data


class ProductsService:
    products_controller = ProductsController()

    def fetch_all_products_info(self, page_limit: int, limit: int) -> list[Product]:
        all_products = []
        skip = 0
        total_products = 0

        while total_products < page_limit * limit:
            products_data = self.products_controller.get_products_info(skip, limit)
            if products_data and products_data["products"]:
                all_products.extend(map_product_from_data(products_data["products"]))
                logging.info(f"Range: {skip} - {skip + limit}")
                skip += limit
                total_products += len(products_data["users"])
            else:
                break
        return all_products
