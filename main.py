import logging

from database.bought_product_entity import BoughtProductEntity
from database.cart_entity import CartEntity
from database.db import Base, db, Session
from database.product_entity import ProductEntity
from database.user_entity import UserEntity
from services.carts_service import CartService
from services.most_ordered_service import (
    get_most_ordered_category_by_user_querry,
)
from services.products_service import ProductsService
from services.users_service import UserService


def main():
    Base.metadata.create_all(db)
    user_service = UserService()
    product_service = ProductsService()
    cart_service = CartService()

    user_service.fetch_and_save_all_users_info(40)
    cart_service.fetch_and_save_all_carts_info(40)
    product_service.fetch_and_save_all_products_info(40)

    with Session() as session:
        print(session.query(UserEntity).all())
        print(session.query(ProductEntity).all())
        print(session.query(CartEntity).all())
        print(session.query(BoughtProductEntity).all())
        # get_most_ordered_category_by_user(session)
        get_most_ordered_category_by_user_querry(session)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    main()

    # fast api - start env
    # start batch
