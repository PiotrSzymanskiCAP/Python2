from collections import defaultdict

from sqlalchemy import func
from sqlalchemy.orm import aliased

from database.cart_entity import CartEntity
from database.product_entity import ProductEntity


def get_most_ordered_category_by_user(session):
    user_category_count = defaultdict(lambda: defaultdict(int))

    carts = session.query(CartEntity).all()
    for cart in carts:
        user_id = cart.user_id
        for product_id, quantity in cart.products.items():
            product = session.query(ProductEntity).filter_by(id=product_id).first()
            if product:
                user_category_count[user_id][product.category] += quantity

    most_ordered_category = {}
    for user_id, category_count in user_category_count.items():
        most_ordered_category[user_id] = max(category_count, key=category_count.get)

    sorted_most_ordered_category = dict(sorted(most_ordered_category.items()))

    return sorted_most_ordered_category


def get_most_ordered_category_by_user_querry(session):
    product_alias = aliased(ProductEntity)

    cart_products = (
        session.query(
            CartEntity.user_id,
            product_alias.category,
            func.sum(func.json_extract(CartEntity.products, '$."quantity"')).label(
                "total_quantity"
            ),
        )
        .join(
            product_alias,
            func.json_extract(CartEntity.products, '$."product_id"')
            == product_alias.id,
        )
        .group_by(CartEntity.user_id, product_alias.category)
        .subquery()
    )

    most_ordered_category = (
        session.query(cart_products.c.user_id, cart_products.c.category)
        .group_by(cart_products.c.user_id, cart_products.c.category)
        .having(func.max(cart_products.c.total_quantity))
        .order_by(cart_products.c.user_id)
        .all()
    )

    return most_ordered_category


def save_most_ordered_to_file(most_ordered):
    with open("most_ordered_output.txt", "w") as file:
        file.write(f"{most_ordered !r}")

    print("Output has been saved to most_ordered_output.txt")
