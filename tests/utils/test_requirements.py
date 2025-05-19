import inspect
import subprocess

# import Domain Objects
from application.domain.models.cart import Cart
from application.domain.models.product import Product
from application.domain.models.user import User


def test_black_dependency():
    result = subprocess.run(["pip", "freeze"], capture_output=True, text=True)
    dependencies = result.stdout.split("\n")
    assert any(
        "black" in dep.lower() for dep in dependencies
    ), "Black linter is not installed"


def test_fastapi_dependency():
    result = subprocess.run(["pip", "freeze"], capture_output=True, text=True)
    dependencies = result.stdout.split("\n")
    assert any(
        "fastapi" in dep.lower() for dep in dependencies
    ), "fastAPI is not installed"


def test_uvtool_dependency():
    result = subprocess.run(["pip", "freeze"], capture_output=True, text=True)
    dependencies = result.stdout.split("\n")
    assert any("uv" in dep.lower() for dep in dependencies), "UV Tool is not installed"


def test_classes_have_str_and_repr():
    # use your domain objects
    classes = [Cart, User, Product]

    for cls in classes:
        str_method = cls.__str__
        repr_method = cls.__repr__

        str_source = inspect.getsource(str_method)
        assert (
            "object.__str__" not in str_source
        ), f"{cls.__name__} does not override __str__ method"

        repr_source = inspect.getsource(repr_method)
        assert (
            "object.__repr__" not in repr_source
        ), f"{cls.__name__} does not override __repr__ method"
