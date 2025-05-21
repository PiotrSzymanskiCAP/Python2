from collections import defaultdict
from typing import Dict

from sqlalchemy import func
from sqlalchemy.orm import Session

from adapters.database.bought_product_entity import BoughtProductEntity
from adapters.database.cart_entity import CartEntity
from adapters.database.product_entity import ProductEntity
from application.domain.ports.most_ordered_category_repository import (
    MostOrderedCategoryRepository,
)


class SqlAlchemyMostOrderedCategoryRepository(MostOrderedCategoryRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_most_ordered_category_by_user(self) -> Dict[int, str]:
        user_category_count = defaultdict(lambda: defaultdict(int))
        results = (
            self.session.query(
                CartEntity.user_id,
                ProductEntity.category,
                func.sum(BoughtProductEntity.quantity).label("total_quantity"),
            )
            .join(
                BoughtProductEntity, CartEntity.cart_id == BoughtProductEntity.cart_id
            )
            .join(
                ProductEntity,
                BoughtProductEntity.product_id == ProductEntity.product_id,
            )
            .group_by(CartEntity.user_id, ProductEntity.category)
            .all()
        )
        for user_id, category, total_quantity in results:
            user_category_count[user_id][category] = total_quantity

        most_ordered_category = {}
        for user_id, category_count in user_category_count.items():
            most_ordered_category[user_id] = max(category_count, key=category_count.get)

        return dict(sorted(most_ordered_category.items()))
