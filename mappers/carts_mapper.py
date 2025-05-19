from adapters.database.bought_product_entity import BoughtProductEntity
from adapters.database.cart_entity import CartEntity
from application.domain.models.cart import Cart


def map_carts_from_data(carts_data: list[dict]) -> list[Cart]:
    all_carts = []
    for cart in carts_data:
        new_cart = map_cart_from_data(cart)
        all_carts.append(new_cart)
    return all_carts


def map_cart_from_data(cart: dict) -> Cart:
    products = cart["products"]
    unwrapped_products = {}

    for product in products:
        unwrapped_products[product["id"]] = product["quantity"]
    return Cart(cart["id"], cart["userId"], unwrapped_products)


def map_cart_to_entity(cart: Cart) -> CartEntity:
    return CartEntity(cart.cart_id, cart.user_id)


def map_cart_to_bought_products_entities(cart: Cart) -> list:
    bought_product_entities = []
    for product_id, quantity in cart.products.items():
        bought_product_entity = BoughtProductEntity(cart.cart_id, product_id, quantity)
        bought_product_entities.append(bought_product_entity)
    return bought_product_entities
