from src.product import Product


def test_product_init(product):
    """Тест: проверка инициализации товара."""
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_price_property(product):
    """Тест: проверка работы свойства price."""
    assert product.price == 180000.0


def test_price_setter_valid(product):
    """Тест: установка корректной цены через сеттер."""
    product.price = 200000.0
    assert product.price == 200000.0


def test_price_setter_invalid(product, capsys):
    """Тест: попытка установить некорректную цену (≤0)."""
    product.price = -1000
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевой или отрицательной" in captured.out
    # Цена не должна измениться
    assert product.price == 180000.0


def test_check_change_price_with_confirmation(product, monkeypatch):
    """Тест: изменение цены с подтверждением пользователя."""
    monkeypatch.setattr("builtins.input", lambda _: "да")

    new_price = 170000.0
    result = product.check_change_price(new_price, None)
    assert result == new_price
    assert product.price == new_price


def test_check_change_price_without_confirmation(product, monkeypatch):
    """Тест: отказ от изменения цены."""
    monkeypatch.setattr("builtins.input", lambda _: "нет")

    initial_price = product.price
    result = product.check_change_price(170000.0, None)
    assert result == initial_price
    assert product.price == initial_price


def test_check_change_price_invalid_response(product, monkeypatch, capsys):
    """Тест: некорректный ответ пользователя."""
    monkeypatch.setattr("builtins.input", lambda _: "что?")

    initial_price = product.price
    result = product.check_change_price(170000.0, None)
    captured = capsys.readouterr()
    assert "Некорректный ответ. Цена не изменена." in captured.out
    assert result == initial_price
    assert product.price == initial_price


def test_check_change_price_same_price(product):
    """Тест: попытка изменить цену на такую же."""
    initial_price = product.price
    result = product.check_change_price(initial_price, "да")
    assert result == initial_price


def test_new_product_create_new(another_product):
    """Тест: создание нового товара через new_product."""
    Product.product_list.clear()
    new_product_data = {
        "name": "Xiaomi Redmi Note 11",
        "description": "Бюджетный смартфон",
        "price": 25000.0,
        "quantity": 10,
    }

    created_product = Product.new_product(new_product_data)

    assert created_product.name == "Xiaomi Redmi Note 11"
    assert created_product.price == 25000.0
    assert created_product.quantity == 10
    assert created_product in Product.product_list


def test_new_product_update_existing(product):
    """Тест: обновление существующего товара через new_product."""
    update_data = {"name": "Samsung Galaxy S23 Ultra", "price": 190000.0, "quantity": 3}

    updated_product = Product.new_product(update_data)

    assert updated_product == product
    assert updated_product.price == 190000.0
    assert updated_product.quantity == 8


def test_product_list_contains_all_products(product, another_product):
    """Тест: проверка списка всех товаров product_list."""
    assert len(Product.product_list) >= 2  # как минимум 2 товара
    assert product in Product.product_list
    assert another_product in Product.product_list

def test_add_two_products_correct_calculation(product, another_product):
    """Тест: корректное вычисление общей стоимости двух товаров"""
    total_cost = product + another_product
    expected_cost = (180000 * 5) + (150000 * 3)
    assert total_cost == expected_cost
