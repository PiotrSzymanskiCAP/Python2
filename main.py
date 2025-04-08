import logging

from database.cart_entity import CartEntity
from database.db import Base, db, Session
from database.product_entity import ProductEntity
from database.user_entity import UserEntity
from services.carts_service import CartService
from services.most_ordered import (
    get_most_ordered_category_by_user,
    save_most_ordered_to_file,
)
from services.products_service import ProductsService
from services.users_service import UserService


def main():
    Base.metadata.create_all(db)
    user_service = UserService()
    product_service = ProductsService()
    cart_service = CartService()

    with Session() as session:
        user_service.fetch_and_save_all_users_info(40, session)
        print(session.query(UserEntity).all())

        product_service.fetch_and_save_all_products_info(40, session)
        print(session.query(ProductEntity).all())

        cart_service.fetch_and_save_all_cats_info(40, session)
        print(session.query(CartEntity).all())

        # endpoint REST could be problem to fetch all data before fastAPI
        most_ordered = get_most_ordered_category_by_user(session)
        print(f"{most_ordered}")
        save_most_ordered_to_file(most_ordered)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    main()

    # fast api - start env
    # start batch
