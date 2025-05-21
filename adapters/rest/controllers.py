from typing import List

from fastapi import Depends, APIRouter

from adapters.database.db import get_db
from adapters.database.impl.bought_product_repository_impl import (
    SqlAlchemyBoughtProductRepository,
)
from adapters.database.impl.cart_repository_impl import SqlAlchemyCartRepository
from adapters.database.impl.products_repository_impl import SqlAlchemyProductRepository
from adapters.database.impl.user_repository_impl import SqlAlchemyUserRepository
from application.domain.models.pydantic_models import User, Product, Cart, BoughtProduct
from application.use_cases.get_all_bought_products import GetAllBoughtProductsUseCase
from application.use_cases.get_all_carts import GetAllCartsUseCase
from application.use_cases.get_all_products import GetAllProductsUseCase
from application.use_cases.get_all_users import GetAllUsersUseCase
from application.use_cases.get_most_ordered_category import (
    GetMostOrderedCategoryUseCase,
)

router = APIRouter()


def get_bought_product_use_case(db=Depends(get_db)):
    repo = SqlAlchemyBoughtProductRepository(db)
    return GetAllBoughtProductsUseCase(repo)


def get_cart_use_case(db=Depends(get_db)):
    repo = SqlAlchemyCartRepository(db)
    return GetAllCartsUseCase(repo)


def get_user_use_case(db=Depends(get_db)):
    repo = SqlAlchemyUserRepository(db)
    return GetAllUsersUseCase(repo)


def get_product_use_case(db=Depends(get_db)):
    repo = SqlAlchemyProductRepository(db)
    return GetAllProductsUseCase(repo)


from adapters.database.impl.most_ordered_category_repository_impl import (
    SqlAlchemyMostOrderedCategoryRepository,
)


def get_most_ordered_category_use_case(db=Depends(get_db)):
    repo = SqlAlchemyMostOrderedCategoryRepository(db)
    return GetMostOrderedCategoryUseCase(repo)


@router.get("/most-ordered-category")
async def most_ordered_category(
    use_case: GetMostOrderedCategoryUseCase = Depends(
        get_most_ordered_category_use_case
    ),
):
    return use_case.execute()


@router.get("/bought-products", response_model=List[BoughtProduct])
async def get_bought_products(
    use_case: GetAllBoughtProductsUseCase = Depends(get_bought_product_use_case),
):
    return use_case.execute()


@router.get("/carts", response_model=List[Cart])
async def get_carts(
    use_case: GetAllCartsUseCase = Depends(get_cart_use_case),
):
    return use_case.execute()


@router.get("/users", response_model=List[User])
async def get_users(
    use_case: GetAllUsersUseCase = Depends(get_user_use_case),
):
    return use_case.execute()


@router.get("/products", response_model=List[Product])
async def get_products(
    use_case: GetAllProductsUseCase = Depends(get_product_use_case),
):
    return use_case.execute()
