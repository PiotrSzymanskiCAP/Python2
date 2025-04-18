import logging

from adapters.products_adapter import ProductsAdapter
from database.db import Session
from models.product import Product
from services.file_service import clear_file, save_data_to_file
from utils.mappers.products_mapper import map_products_from_data, map_product_to_entity


def save_products_to_db(session: Session, products: [Product]):
    for product in products:
        session.add(map_product_to_entity(product))
    session.commit()


class ProductsService:
    products_controller = ProductsAdapter()
    file_name = "products_output.txt"

    def fetch_and_save_all_products_info(self, batch_size: int):
        session = Session()
        clear_file(self.file_name)
        skip = 0

        initial_data = self.products_controller.get_products_info(skip, batch_size)
        if not initial_data or "total" not in initial_data:
            return

        total_products = initial_data["total"]
        mapped_products = map_products_from_data(initial_data["products"])
        save_data_to_file(mapped_products, self.file_name)
        with session.begin():
            save_products_to_db(session, mapped_products)
        session.commit()

        skip += batch_size

        while skip < total_products:
            try:
                product_data = self.products_controller.get_products_info(
                    skip, batch_size
                )
                if product_data and product_data["products"]:
                    mapped_products = map_products_from_data(product_data["products"])
                    save_data_to_file(mapped_products, self.file_name)
                    with session.begin():
                        save_products_to_db(session, mapped_products)
                    session.commit()
                    logging.info(f"Range: {skip} - {skip + batch_size}")
                    skip += batch_size
                else:
                    break

            except Exception as e:
                logging.error(
                    f"Error fetching data for range {skip} - {skip + batch_size}: {e}"
                )
                break
