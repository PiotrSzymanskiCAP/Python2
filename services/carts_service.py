import logging

from controllers.carts_controller import CartsController
from models.cart import Cart
from utils.mappers.carts_mapper import map_carts_from_data


def save_carts_to_file(carts):
    with open("carts_output.txt", "w") as file:
        file.write(f"{carts !r}")

    print("Output has been saved to carts_output.txt")


class CartService:
    cart_controller = CartsController()

    def fetch_all_carts_info(self, page_limit: int, limit: int) -> list[Cart]:
        all_carts = []
        skip = 0
        total_carts = 0

        while total_carts < page_limit * limit:
            carts_data = self.cart_controller.get_carts_info(skip, limit)
            if carts_data and carts_data["carts"]:
                all_carts.extend(map_carts_from_data(carts_data["carts"]))
                logging.info(f"Range: {skip} - {skip + limit}")
                skip += limit
                total_carts += len(carts_data["carts"])
            else:
                break
        return all_carts
