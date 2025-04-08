import logging

from adapters.carts_adapter import CartsAdapter
from database.db import Session
from models.cart import Cart
from services.file_service import clear_file, save_data_to_file
from utils.mappers.carts_mapper import map_carts_from_data, map_cart_to_entity


def save_carts_to_db(session: Session, carts: [Cart]):
    for cart in carts:
        session.add(map_cart_to_entity(cart))
    session.commit()


class CartService:
    cart_controller = CartsAdapter()
    file_name = "carts_output.txt"

    def fetch_and_save_all_cats_info(self, batch_size: int, session: Session):
        clear_file(self.file_name)
        skip = 0

        initial_data = self.cart_controller.get_carts_info(skip, batch_size)
        if not initial_data or "total" not in initial_data:
            return

        total_carts = initial_data["total"]
        mapped_carts = map_carts_from_data(initial_data["carts"])
        save_data_to_file(mapped_carts, self.file_name)
        save_carts_to_db(session, mapped_carts)

        skip += batch_size

        while skip < total_carts:
            try:
                cart_data = self.cart_controller.get_carts_info(skip, batch_size)
                if cart_data and cart_data["carts"]:
                    mapped_carts = map_carts_from_data(cart_data["carts"])
                    save_data_to_file(mapped_carts, self.file_name)
                    save_carts_to_db(session, mapped_carts)
                    logging.info(f"Range: {skip} - {skip + batch_size}")
                    skip += batch_size
                else:
                    break

            except Exception as e:
                logging.error(
                    f"Error fetching data for range {skip} - {skip + batch_size}: {e}"
                )
                break
