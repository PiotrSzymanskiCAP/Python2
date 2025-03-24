import logging

from database.db import Base, db, Session
from database.user_entity import UserEntity
from services.user_service import UserService, save_users_to_file
from utils.mappers.user_mapper import map_user_to_entity


def main():
    Base.metadata.create_all(db)

    print("Hello")
    user_service = UserService()
    all_users = user_service.fetch_all_users_info(10, 40)
    save_users_to_file(all_users)
    print(f"{all_users!r} ")

    # print(f"{user_service.fetch_user_info(8)}")
    # user_one = user_service.fetch_user_info(8)

    with Session() as session:
        for user in all_users:
            session.add(map_user_to_entity(user))
        # session.add(map_user_to_entity(user_one))
        session.commit()
        print(session.query(UserEntity).all())


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    main()
