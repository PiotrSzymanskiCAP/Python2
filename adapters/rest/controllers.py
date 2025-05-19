from typing import List

from fastapi import Depends, APIRouter
from starlette.responses import JSONResponse

from adapters.database.bought_product_entity import BoughtProductEntity
from adapters.database.cart_entity import CartEntity
from adapters.database.db import Session, get_db
from adapters.database.product_entity import ProductEntity
from adapters.database.user_entity import UserEntity
from application.domain.models.pydantic_models import User, Product, Cart, BoughtProduct
from application.domain.services.most_ordered_service import (
    get_most_ordered_category_by_user_query,
)

router = APIRouter()


@router.get("/users", response_model=List[User])
async def get_users(db: Session = Depends(get_db)):
    return db.query(UserEntity).all()


@router.get("/products", response_model=List[Product])
async def get_products(db: Session = Depends(get_db)):
    return db.query(ProductEntity).all()


@router.get("/carts", response_model=List[Cart])
async def get_carts(db: Session = Depends(get_db)):
    return db.query(CartEntity).all()


@router.get("/bought-products", response_model=List[BoughtProduct])
async def get_bought_products(db: Session = Depends(get_db)):
    return db.query(BoughtProductEntity).all()


@router.get("/most-ordered-category")
async def most_ordered_category(db: Session = Depends(get_db)):
    data = get_most_ordered_category_by_user_query(db)
    return JSONResponse(content=data)
