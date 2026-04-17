import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )


@pytest.fixture
def category_1():
    product1 = Product(
        name="Samsung Galaxy S23 Ultra",
        description="Смартфон",
        price=180000,
        quantity=5
    )
    product2 = Product(
        name="Iphone 15",
        description="Смартфон Apple",
        price=150000,
        quantity=3
    )
    product3 = Product(
        name="Xiaomi Redmi Note 11",
        description="Бюджетный смартфон",
        price=25000,
        quantity=10
    )
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


@pytest.fixture
def category_2():
    product1 = Product(
        name='55" QLED 4K',
        description="Телевизор с QLED-экраном",
        price=80000,
        quantity=2
    )
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product1],
    )


@pytest.fixture
def another_product():
    return Product(
        name="Iphone 15",
        description="Смартфон Apple",
        price=150000.0,
        quantity=3
    )
