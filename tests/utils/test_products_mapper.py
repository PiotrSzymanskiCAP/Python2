from models.product import Product
from utils.mappers.products_mapper import (
    map_products_from_data,
    map_product_to_entity,
    map_product_from_data,
)


def test_map_product_from_data():
    product_data = {
        "id": 1,
        "title": "Product 1",
        "price": 10.0,
        "category": "Category 1",
    }

    product = map_product_from_data(product_data)

    assert product.product_id == 1
    assert product.title == "Product 1"
    assert product.price == 10.0
    assert product.category == "Category 1"


def test_map_products_from_data():
    products_data_list = [
        {"id": 1, "title": "Product 1", "price": 10.0, "category": "Category 1"},
        {"id": 2, "title": "Product 2", "price": 20.0, "category": "Category 2"},
    ]

    products = map_products_from_data(products_data_list)

    assert len(products) == 2
    assert products[0].product_id == 1
    assert products[0].title == "Product 1"
    assert products[0].price == 10.0
    assert products[0].category == "Category 1"

    assert products[1].product_id == 2
    assert products[1].title == "Product 2"
    assert products[1].price == 20.0
    assert products[1].category == "Category 2"


def test_map_product_to_entity():
    product = Product(
        product_id=1, title="Product 1", price=10.0, category="Category 1"
    )

    product_entity = map_product_to_entity(product)

    assert product_entity.product_id == 1
    assert product_entity.title == "Product 1"
    assert product_entity.price == 10.0
    assert product_entity.category == "Category 1"
