import os
import json
from unittest.mock import patch, mock_open
from src.category import Category
from src.utils import loads_category_and_product_data_from_json, create_object_from_json


def test_valid_json_data() -> None:
    """Тест с корректными данными"""
    expected_data = [
        {
            "name": "Смартфоны",
            "description": "Описание",
            "products": [{"name": "Samsung Galaxy S23 Ultra", "price": 180000}],
        }
    ]
    json_data = json.dumps(expected_data, ensure_ascii=False)
    input_path = "../data/products.json"
    expected_absolute_path = os.path.abspath(input_path)
    with patch("builtins.open", mock_open(read_data=json_data)) as mock_file:
        result = loads_category_and_product_data_from_json(input_path)
    assert result == expected_data
    mock_file.assert_called_once_with(expected_absolute_path, "r", encoding="UTF-8")


def test_create_object_from_json_success():
    """Тест успешного создания объектов из JSON"""
    sample_data = [
        {
            "name": "Смартфоны",
            "description": "Описание категории смартфонов",
            "products": [
                {"name": "Samsung Galaxy S23 Ultra", "description": "Смартфон", "price": 180000, "quantity": 5},
                {"name": "Iphone 15", "description": "Смартфон Apple", "price": 150000, "quantity": 3},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Описание категории телевизоров",
            "products": [
                {"name": '55" QLED 4K', "description": "Телевизор с QLED-экраном", "price": 80000, "quantity": 2}
            ],
        },
    ]

    # Вызываем тестируемую функцию
    result = create_object_from_json(sample_data)

    # Проверяем, что вернули список из 2 категорий
    assert len(result) == 2
    assert isinstance(result[0], Category)
    assert isinstance(result[1], Category)

    # Проверяем первую категорию
    category1 = result[0]
    assert category1.name == "Смартфоны"
    assert category1.description == "Описание категории смартфонов"
    assert len(category1.products_in_list) == 2

    # Проверяем первый продукт в первой категории
    product1 = category1.products_in_list[0]
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "Смартфон"
    assert product1.price == 180000
    assert product1.quantity == 5

    # Проверяем второй продукт в первой категории
    product2 = category1.products_in_list[1]
    assert product2.name == "Iphone 15"
    assert product2.description == "Смартфон Apple"
    assert product2.price == 150000
    assert product2.quantity == 3

    # Проверяем вторую категорию
    category2 = result[1]
    assert category2.name == "Телевизоры"
    assert category2.description == "Описание категории телевизоров"
    assert len(category2.products_in_list) == 1

    # Проверяем продукт во второй категории
    product3 = category2.products_in_list[0]
    assert product3.name == '55" QLED 4K'
    assert product3.description == "Телевизор с QLED-экраном"
    assert product3.price == 80000
    assert product3.quantity == 2
