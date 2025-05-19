from unittest.mock import MagicMock, Mock

import pytest

from adapters.database.db import Session
from adapters.dummyjson.users_adapter import UserAdapter
from application.domain.services.users_service import save_users_to_db, UserService
from mappers.users_mapper import map_users_from_data


@pytest.fixture
def user_service():
    service = UserService()
    service.user_controller = MagicMock(spec=UserAdapter)
    return service


@pytest.fixture
def mock_session():
    session = Mock(spec=Session)
    session.begin = MagicMock()
    session.add = MagicMock()
    session.commit = MagicMock()
    return session


@pytest.fixture()
def mock_users():
    return [
        {
            "id": 1,
            "firstName": "Alice",
            "lastName": "Wonderland",
            "age": 99,
            "address": {
                "coordinates": {"lat": 1.0, "lng": 2.0},
                "country": "Equatorial Guinea",
            },
        },
        {
            "id": 2,
            "firstName": "Bob",
            "lastName": "Builder",
            "age": 45,
            "address": {
                "coordinates": {"lat": 3.0, "lng": 4.0},
                "country": "Builderland",
            },
        },
    ]


def test_save_users_to_db(mock_session, mock_users):
    mapped_mock_users = map_users_from_data(mock_users)
    save_users_to_db(mock_session, mapped_mock_users)

    assert mock_session.begin.called
    assert mock_session.add.call_count == len(mock_users)
    assert mock_session.commit.called


# @patch("services.file_service.clear_file")
# @patch("services.file_service.save_data_to_file")
# @patch("services.users_service.save_users_to_db")
# def test_fetch_and_save_all_users_info(
#     mock_save_users_to_db,
#     mock_save_data_to_file,
#     mock_clear_file,
#     user_service,
#     mock_session,
#     mock_users,
# ):
#     user_service.user_controller.get_users_info.side_effect = [
#         {"total": 2, "users": mock_users},
#         {"total": 2, "users": []},
#     ]
#
#     user_service.fetch_and_save_all_users_info(batch_size=2)
#
#     print(f"mock_clear_file.call_count: {mock_clear_file.call_count}")
#
#     mock_clear_file.assert_called_once_with(user_service.file_name)
#     mock_save_data_to_file.assert_called_once()
#     mock_save_users_to_db.assert_called_once_with(mock_session, mock_users)


# def test_process_and_save_users(user_service, mock_session, mock_users):
#     with (
#         patch(
#             "utils.mappers.users_mapper.map_users_from_data", return_value=mock_users
#         ) as mock_map_users_from_data,
#         patch("services.file_service.save_data_to_file") as mock_save_data_to_file,
#         patch("services.users_service.save_users_to_db") as mock_save_users_to_db,
#     ):
#         user_service.process_and_save_users(mock_session, mock_users)
#
#         mock_map_users_from_data.assert_called_once_with(mock_users)
#         mock_save_data_to_file.assert_called_once_with(
#             mock_users, user_service.file_name
#         )
#         mock_save_users_to_db.assert_called_once_with(mock_session, mock_users)
