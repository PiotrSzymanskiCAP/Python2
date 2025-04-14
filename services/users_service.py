import logging

from adapters.users_adapter import UserAdapter
from database.db import Session
from models.user import User
from services.file_service import clear_file, save_data_to_file
from utils.mappers.users_mapper import map_users_from_data, map_user_to_entity


def save_users_to_db(session: Session, users: [User]):
    for user in users:
        session.add(map_user_to_entity(user))
    session.commit()


class UserService:
    user_controller = UserAdapter()
    file_name = "users_output.txt"

    def fetch_and_save_all_users_info(self, batch_size: int):
        session = Session()
        clear_file(self.file_name)
        skip = 0

        initial_data = self.user_controller.get_users_info(skip, batch_size)
        if not initial_data or "total" not in initial_data:
            return

        total_users = initial_data["total"]
        mapped_users = map_users_from_data(initial_data["users"])
        save_data_to_file(mapped_users, self.file_name)
        with session.begin():
            save_users_to_db(session, mapped_users)
        session.commit()

        skip += batch_size

        while skip < total_users:
            try:
                user_data = self.user_controller.get_users_info(skip, batch_size)
                if user_data and user_data["users"]:
                    mapped_users = map_users_from_data(user_data["users"])
                    save_data_to_file(mapped_users, self.file_name)
                    with session.begin():
                        save_users_to_db(session, mapped_users)
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
