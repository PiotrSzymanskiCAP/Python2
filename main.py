from services.user_service import UserService
import logging


def main():
    print("Hello")
    user_service = UserService()

    #user_service.fetch_all_user()
    #user_service.fetch_all_users_info(10)
    print(f"{user_service.fetch_all_users_info(10, 30) !r} ")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    main()
