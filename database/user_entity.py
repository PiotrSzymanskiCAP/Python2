from sqlalchemy.orm import Mapped, mapped_column

from database.db import Base


class UserEntity(Base):
    __tablename__ = "users"

    uuid: Mapped[str] = mapped_column(primary_key=True)
    id: Mapped[int]
    firstname: Mapped[str]
    lastname: Mapped[str]
    age: Mapped[int]
    latitude: Mapped[int]
    longitude: Mapped[int]
    country: Mapped[str]

    def __init__(
        self,
        uuid: str,
        id: int,
        firstname: str,
        lastname: str,
        age: int,
        latitude: float,
        longitude: float,
        country: str,
    ):
        self.uuid = uuid
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.latitude = latitude
        self.longitude = longitude
        self.country = country

    def __repr__(self):
        return f"{self.uuid} | User with ID: {self.id} -> {self.firstname} {self.lastname} Age: {self.age} Cord: {self.latitude}, {self.longitude} -> {self.country}\n"
