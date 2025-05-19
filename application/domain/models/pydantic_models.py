from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    firstname: str
    lastname: str
    age: int
    latitude: float
    longitude: float
    country: str

    class Config:
        from_attributes = True


class Product(BaseModel):
    product_id: int
    title: str
    price: float
    category: str

    class Config:
        from_attributes = True


class Cart(BaseModel):
    cart_id: int
    user_id: int

    class Config:
        from_attributes = True


class BoughtProduct(BaseModel):
    cart_id: int
    product_id: int
    quantity: int

    class Config:
        from_attributes = True
