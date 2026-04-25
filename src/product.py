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
        self.__price = price
        self.quantity = quantity
        Product.product_list.append(self)

    def __str__(self) -> str:
        """Возвращает строковое отображение продукта в следующем виде: Название продукта, руб. Остаток: шт."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self) -> float:
        """Возвращает цену товаров."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Возвращает строку с ценой или сообщением об ошибке"""
        if value <= 0:
            print("Цена не должна быть нулевой или отрицательной")
            return
        self.__price = value

    def check_change_price(self, new_price: float, user_confirmed: str) -> float:
        """Изменение цены в случае ее понижения с согласия пользователя"""
        if self.price != new_price:
            if user_confirmed is None:
                user_confirmed = input("Вы уверены, что хотите изменить цену? (да/нет): ")
            if user_confirmed == "да":
                self.price = new_price
            elif user_confirmed != "нет":
                print("Некорректный ответ. Цена не изменена.")
        return self.price

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
