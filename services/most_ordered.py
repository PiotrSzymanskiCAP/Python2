from collections import defaultdict

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
