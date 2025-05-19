import pytest
import sqlalchemy
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker

from database.bought_product_entity import BoughtProductEntity
from database.cart_entity import CartEntity
from database.db import Base, get_db
from database.product_entity import ProductEntity
from database.user_entity import UserEntity
from main import app

engine = sqlalchemy.create_engine(
    "sqlite:///:memory:", echo=True, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def db_session(setup_database):
    session = TestingSessionLocal()
    yield session
    session.close()


def test_get_users(client, db_session):
    try:
        user = UserEntity(
            user_id=1,
            firstname="Alice",
            lastname="Wonderland",
            age=99,
            longitude=2.00,
            latitude=1.00,
            country="China",
        )
        db_session.add(user)
        db_session.commit()

        response = client.get("/users")
        print(response.json())
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert response.json()[0]["firstname"] == "Alice"
    except Exception as e:
        print(f"An error occurred: {e}")


def test_get_products(client, db_session):
    try:
        product = ProductEntity(
            product_id=1, title="Product 1", price=10.0, category="Category 1"
        )
        db_session.add(product)
        db_session.commit()

        response = client.get("/products")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert response.json()[0]["title"] == "Product 1"
    except Exception as e:
        print(f"An error occurred: {e}")


def test_get_carts(client, db_session):
    try:
        user = UserEntity(
            user_id=1,
            firstname="Alice",
            lastname="Wonderland",
            age=99,
            longitude=2.00,
            latitude=1.00,
            country="China",
        )
        db_session.add(user)
        db_session.commit()
        print("User added.")

        cart = CartEntity(cart_id=1, user_id=1)
        db_session.add(cart)
        db_session.commit()
        print("Cart added.")

        response = client.get("/carts")
        print("Response received.")
        print(response.json())  # Inspect the response
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert response.json()[0]["cart_id"] == 1
    except Exception as e:
        print(f"An error occurred: {e}")


def test_get_bought_products(client, db_session):
    try:
        product = ProductEntity(
            product_id=1, title="Product 1", price=10.0, category="Category 1"
        )
        db_session.add(product)
        db_session.commit()
        print("Product added.")

        cart = CartEntity(cart_id=1, user_id=1)
        db_session.add(cart)
        db_session.commit()
        print("Cart added.")

        bought_product = BoughtProductEntity(cart_id=1, product_id=1, quantity=2)
        db_session.add(bought_product)
        db_session.commit()
        print("Bought product added.")

        response = client.get("/bought-products")
        print("Response received.")
        print(response.json())  # Inspect the response
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert response.json()[0]["quantity"] == 2
    except Exception as e:
        print(f"An error occurred: {e}")


def test_most_ordered_category(client, db_session):
    try:
        response = client.get("/most-ordered-category")
        print("Response received.")
        print(response.json())
        assert response.status_code == 200
    except Exception as e:
        print(f"An error occurred: {e}")


def test_invalid_endpoint(client):
    response = client.get("/invalid-endpoint")
    assert response.status_code == 404
