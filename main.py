import logging

from services.user_service import UserService


def main():
    print("Hello")
    user_service = UserService()
    print(f"{user_service.fetch_all_users_info(10, 40) !r} ")
    print(f"{user_service.fetch_user_info(8)}")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    main()
