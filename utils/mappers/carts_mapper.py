from database.cart_entity import CartEntity
from models.cart import Cart


def map_carts_from_data(carts_data: list[dict]) -> list[Cart]:
    all_carts = []
    for cart in carts_data:
        new_cart = map_cart_from_data(cart)
        all_carts.append(new_cart)
    return all_carts


def map_cart_from_data(cart) -> Cart:
    new_cart = Cart(cart["id"], cart["userId"])
    for product in cart["products"]:
        new_cart.add_product(product["id"], product["quantity"])
    return new_cart


def map_cart_to_entity(cart: Cart) -> CartEntity:
    return CartEntity(
        cart._cart_id,
        cart._user_id,
        cart._products,
    )
