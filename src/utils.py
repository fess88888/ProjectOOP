import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def loads_category_and_product_data_from_json(path: str) -> Any:
    """Функция, которая загружает данные по категориям и товарам из файла JSON"""
    path_to_file = os.path.abspath(path)
    with open(path_to_file, "r", encoding="UTF-8") as file:
        category_and_product_data = json.load(file)
        return category_and_product_data


def create_object_from_json(category_and_product_data: list[dict]) -> list[Category]:
    """Функция, которая конвертирует полученные данные из файла JSON в объекты классов."""
    categories = []
    for category in category_and_product_data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
            print(products)
        category["products"] = products
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    my_data = loads_category_and_product_data_from_json("../data/products.json")
    print(my_data)
    categories_data = create_object_from_json(my_data)
    print(categories_data)
    print(categories_data[0].name)
