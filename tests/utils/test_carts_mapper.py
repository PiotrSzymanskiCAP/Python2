from mappers.carts_mapper import (
    map_carts_from_data,
    map_cart_to_entity,
    map_cart_from_data,
    map_cart_to_bought_products_entities,
)
from models.cart import Cart


def test_map_cart_from_data():
    cart_data = {
        "id": 1,
        "userId": 1,
        "products": [{"id": 101, "quantity": 2}, {"id": 102, "quantity": 3}],
    }

    cart = map_cart_from_data(cart_data)

    assert cart.cart_id == 1
    assert cart.user_id == 1
    assert cart.products == {101: 2, 102: 3}


def test_map_carts_from_data():
    carts_data_list = [
        {
            "id": 1,
            "userId": 1,
            "products": [{"id": 101, "quantity": 2}, {"id": 102, "quantity": 3}],
        },
        {
            "id": 2,
            "userId": 2,
            "products": [{"id": 103, "quantity": 1}, {"id": 104, "quantity": 4}],
        },
    ]

    carts = map_carts_from_data(carts_data_list)

    assert len(carts) == 2
    assert carts[0].cart_id == 1
    assert carts[0].user_id == 1
    assert carts[0].products == {101: 2, 102: 3}

    assert carts[1].cart_id == 2
    assert carts[1].user_id == 2
    assert carts[1].products == {103: 1, 104: 4}


def test_map_cart_to_entity():
    cart = Cart(cart_id=1, user_id=1, products={101: 2, 102: 3})

    cart_entity = map_cart_to_entity(cart)

    assert cart_entity.cart_id == 1
    assert cart_entity.user_id == 1


def test_map_cart_to_bought_products_entities():
    cart = Cart(cart_id=1, user_id=1, products={101: 2, 102: 3})

    bought_product_entities = map_cart_to_bought_products_entities(cart)

    assert len(bought_product_entities) == 2
    assert bought_product_entities[0].cart_id == 1
    assert bought_product_entities[0].product_id == 101
    assert bought_product_entities[0].quantity == 2

    assert bought_product_entities[1].cart_id == 1
    assert bought_product_entities[1].product_id == 102
    assert bought_product_entities[1].quantity == 3
