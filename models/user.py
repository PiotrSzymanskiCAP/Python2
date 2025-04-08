import reverse_geocode


def get_country_name(latitude: float, longitude: float) -> str:
    location = reverse_geocode.get((latitude, longitude))
    return location["country"]


# Dataclass frozen? // validate post init
class User:

    def __init__(
        self,
        user_id: int,
        first_name: str,
        last_name: str,
        age: int,
        latitude: float,
        longitude: float,
    ):
        self._user_id = user_id
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self._lat = latitude
        self._lng = longitude
        self._country = get_country_name(self._lat, self._lng)

    def __repr__(self):
        return f"User with ID: {self._user_id} -> {self._first_name} {self._last_name} Age: {self._age} Cord: {self._lat}, {self._lng} -> {self._country}\n"
