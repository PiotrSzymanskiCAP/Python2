from collections import defaultdict

from sqlalchemy import func

from database.bought_product_entity import BoughtProductEntity
from database.cart_entity import CartEntity
from database.product_entity import ProductEntity
from services.file_service import clear_file, save_most_ordered_to_file


def get_most_ordered_category_by_user(session):
    user_category_count = defaultdict(lambda: defaultdict(int))
    FILE_NAME = "most_ordered_output.txt"
    clear_file(FILE_NAME)

    carts = session.query(CartEntity).all()
    products = session.query(ProductEntity).all()
    product_dict = {product.id: product for product in products}
    bought_products = session.query(BoughtProductEntity).all()

    cart_user_map = {cart.id: cart.user_id for cart in carts}

    for bought_product in bought_products:
        cart_id = bought_product.cart_id
        product_id = bought_product.product_id
        quantity = bought_product.quantity

        user_id = cart_user_map.get(cart_id)
        if user_id is not None:
            product = product_dict.get(product_id)
            if product:
                user_category_count[user_id][product.category] += quantity

    most_ordered_category = {}
    for user_id, category_count in user_category_count.items():
        most_ordered_category[user_id] = max(category_count, key=category_count.get)

    sorted_most_ordered_category = dict(sorted(most_ordered_category.items()))
    save_most_ordered_to_file(sorted_most_ordered_category, FILE_NAME)


def get_most_ordered_category_by_user_query(session):
    user_category_count = defaultdict(lambda: defaultdict(int))
    FILE_NAME = "most_ordered_output.txt"
    clear_file(FILE_NAME)

    results = (
        session.query(
            CartEntity.user_id,
            ProductEntity.category,
            func.sum(BoughtProductEntity.quantity).label("total_quantity"),
        )
        .join(BoughtProductEntity, CartEntity.cart_id == BoughtProductEntity.cart_id)
        .join(ProductEntity, BoughtProductEntity.product_id == ProductEntity.product_id)
        .group_by(CartEntity.user_id, ProductEntity.category)
        .all()
    )

    for user_id, category, total_quantity in results:
        user_category_count[user_id][category] = total_quantity

    most_ordered_category = {}
    for user_id, category_count in user_category_count.items():
        most_ordered_category[user_id] = max(category_count, key=category_count.get)

    sorted_most_ordered_category = dict(sorted(most_ordered_category.items()))
    save_most_ordered_to_file(sorted_most_ordered_category, FILE_NAME)
    return sorted_most_ordered_category
