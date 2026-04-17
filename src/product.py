from typing import Any


class Product:
    """Класс для представления характеристик товара"""

    name: str
    description: str
    quantity: int
    product_list: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализирует новый экземпляр товара.
        При создании объекта автоматически добавляет его в список product_list."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.product_list.append(self)

    @classmethod
    def new_product(cls, product: dict) -> Any:
        """Добавляет новый товар или обновляет существующий с таким же именем."""

        existing_product = None
        for unit in cls.product_list:
            if product["name"] == unit.name:
                existing_product = unit
                break

        if existing_product:
            # Обновляем существующий товар
            existing_product.price = max(existing_product.price, product["price"])
            existing_product.quantity += product["quantity"]
            return existing_product
        else:
            # Создаём новый товар
            new_unit = cls(
                name=product["name"],
                description=product["description"],
                price=product["price"],
                quantity=product["quantity"],
            )
            return new_unit
