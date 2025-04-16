import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from controllers import controllers
from database.db import Base, db
from services.carts_service import CartService
from services.products_service import ProductsService
from services.users_service import UserService

Base.metadata.create_all(db)
user_service = UserService()
product_service = ProductsService()
cart_service = CartService()

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    user_service.fetch_and_save_all_users_info(40)
    cart_service.fetch_and_save_all_carts_info(40)
    product_service.fetch_and_save_all_products_info(40)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(controllers.router)

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    uvicorn.run(app, host="0.0.0.0", port=8000)
