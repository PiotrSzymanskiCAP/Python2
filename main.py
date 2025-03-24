import logging

from database.db import Base, db, Session
from database.product_entity import ProductEntity
from database.user_entity import UserEntity
from services.products_service import ProductsService, save_products_to_file
from services.user_service import UserService, save_users_to_file
from utils.mappers.products_mapper import map_product_to_entity
from utils.mappers.user_mapper import map_user_to_entity


def main():
    Base.metadata.create_all(db)
    user_service = UserService()
    product_service = ProductsService()

    all_products = product_service.fetch_all_products_info(10, 40)
    all_users = user_service.fetch_all_users_info(10, 40)
    save_users_to_file(all_users)
    save_products_to_file(all_products)
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


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    main()
