from models.user import User
from utils.mappers.users_mapper import (
    map_users_from_data,
    map_user_to_entity,
    map_user_from_data,
)


def test_map_users_from_data():
    user_data_list = [
        {
            "id": 1,
            "firstName": "Alice",
            "lastName": "Wonderland",
            "age": 99,
            "address": {"coordinates": {"lat": 1.0, "lng": 2.0}},
        },
        {
            "id": 2,
            "firstName": "Bob",
            "lastName": "Builder",
            "age": 45,
            "address": {"coordinates": {"lat": 3.0, "lng": 4.0}},
        },
    ]

    users = map_users_from_data(user_data_list)

    assert len(users) == 2
    assert users[0].user_id == 1
    assert users[0].first_name == "Alice"
    assert users[0].last_name == "Wonderland"
    assert users[0].age == 99
    assert users[0].latitude == 1.0
    assert users[0].longitude == 2.0

    assert users[1].user_id == 2
    assert users[1].first_name == "Bob"
    assert users[1].last_name == "Builder"
    assert users[1].age == 45
    assert users[1].latitude == 3.0
    assert users[1].longitude == 4.0


def test_map_user_to_entity():
    user = User(
        user_id=1,
        first_name="Alice",
        last_name="Wonderland",
        age=99,
        latitude=1.0,
        longitude=2.0,
    )

    user_entity = map_user_to_entity(user)

    assert user_entity.user_id == 1
    assert user_entity.firstname == "Alice"
    assert user_entity.lastname == "Wonderland"
    assert user_entity.age == 99
    assert user_entity.latitude == 1.0
    assert user_entity.longitude == 2.0


def test_map_user_from_data():
    user_data = {
        "id": 1,
        "firstName": "Alice",
        "lastName": "Wonderland",
        "age": 99,
        "address": {"coordinates": {"lat": 1.0, "lng": 2.0}},
    }

    user = map_user_from_data(user_data)

    assert user.user_id == 1
    assert user.first_name == "Alice"
    assert user.last_name == "Wonderland"
    assert user.age == 99
    assert user.latitude == 1.0
    assert user.longitude == 2.0
