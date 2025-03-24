from models.product import Product


def map_products_from_data(products_data: list[dict]) -> list[Product]:
    all_products = []
    for product in products_data:
        new_product = map_product_from_data(product)
        all_products.append(new_product)
    return all_products


def map_product_from_data(product) -> Product:
    return Product(
        product["id"],
        product["title"],
        product["price"],
        product["category"],
    )
