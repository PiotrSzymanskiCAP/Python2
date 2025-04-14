from dataclasses import dataclass, field

import reverse_geocode


def get_country_name(latitude: float, longitude: float) -> str:
    location = reverse_geocode.get((latitude, longitude))
    return location["country"]


@dataclass(frozen=True)
class User:
    user_id: int
    first_name: str
    last_name: str
    age: int
    latitude: float
    longitude: float
    _country: str = field(init=False, repr=False)

    def __post_init__(self):
        object.__setattr__(
            self, "_country", get_country_name(self.latitude, self.longitude)
        )

    def __str__(self):
        return (
            f"User with ID: {self.user_id} -> {self.first_name} {self.last_name} "
            f"Age: {self.age} Cord: {self.latitude}, {self.longitude} -> {self._country}"
        )

    def __repr__(self):
        return (
            f"User(user_id={self.user_id}, first_name={self.first_name!r}, "
            f"last_name={self.last_name!r}, age={self.age}, "
            f"latitude={self.latitude}, longitude={self.longitude}, country={self._country!r})"
        )
