from src.category import Category
from src.product import Product


def test_category_init(category_1, category_2):
    """Тест: проверка инициализации категорий и счётчиков."""
    assert category_1.category_count == 2
    assert category_1.product_count == 4


def test_add_product_to_category(category_1, product):
    """Тест: добавление товара в категорию."""
    initial_product_count = Category.product_count
    initial_products_count = len(category_1.products_in_list)

    category_1.add_product(product)

    assert product in category_1.products_in_list
    assert len(category_1.products_in_list) == initial_products_count + 1
    assert Category.product_count == initial_product_count + 1


def test_products_property(category_1):
    """Тест: проверка работы свойства products."""
    products_str = category_1.products

    assert "Samsung Galaxy S23 Ultra" in products_str
    assert "180000 руб." in products_str
    assert "5 шт." in products_str


def test_products_in_list_property(category_2):
    """Тест: проверка работы свойства products_in_list."""
    products_list = category_2.products_in_list

    assert isinstance(products_list, list)
    assert len(products_list) == 1
    assert isinstance(products_list[0], Product)
    assert products_list[0].name == '55" QLED 4K'


def test_multiple_add_products(category_1):
    """Тест: последовательное добавление нескольких товаров."""
    initial_count = Category.product_count

    product1 = Product("Новый смартфон 1", "Описание", 30000, 7)
    product2 = Product("Новый смартфон 2", "Описание", 40000, 4)

    category_1.add_product(product1)
    category_1.add_product(product2)

    assert product1 in category_1.products_in_list
    assert product2 in category_1.products_in_list
    assert Category.product_count == initial_count + 2
