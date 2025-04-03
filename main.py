import logging

from database.cart_entity import CartEntity
from database.db import Base, db, Session
from database.product_entity import ProductEntity
from database.user_entity import UserEntity
from services.carts_service import CartService, save_carts_to_file
from services.most_ordered import (
    get_most_ordered_category_by_user,
    save_most_ordered_to_file,
)
from services.products_service import ProductsService, save_products_to_file
from services.users_service import UserService, save_users_to_file
from utils.mappers.carts_mapper import map_cart_to_entity
from utils.mappers.products_mapper import map_product_to_entity
from utils.mappers.users_mapper import map_user_to_entity


def main():
    Base.metadata.create_all(db)
    user_service = UserService()
    product_service = ProductsService()
    cart_service = CartService()

    all_products = product_service.fetch_all_products_info(10, 40)
    all_users = user_service.fetch_all_users_info(10, 40)
    all_carts = cart_service.fetch_all_carts_info(10, 40)
    save_users_to_file(all_users)
    save_products_to_file(all_products)
    save_carts_to_file(all_carts)
    # print(f"{all_users!r} ")
    # print(f"{all_products!r} ")

    # print(f"{user_service.fetch_user_info(8)}")
    # user_one = user_service.fetch_user_info(8)

    with Session() as session:
        for user in all_users:
            session.add(map_user_to_entity(user))
        # session.add(map_user_to_entity(user_one))
        session.commit()
        print(session.query(UserEntity).all())

        for product in all_products:
            session.add(map_product_to_entity(product))
        session.commit()
        print(session.query(ProductEntity).all())

        for cart in all_carts:
            session.add(map_cart_to_entity(cart))
        session.commit()
        print(session.query(CartEntity).all())

        most_ordered = get_most_ordered_category_by_user(session)
        print(f"{most_ordered}")
        save_most_ordered_to_file(most_ordered)

        # most_ordered_category = get_most_ordered_category_by_user_querry(session)
        # for user_id, category in most_ordered_category:
        #     print(f"User ID: {user_id}, Most Ordered Category: {category}")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    main()
