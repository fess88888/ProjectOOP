from typing import Any, Dict
from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс для всех продуктов"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация продукта"""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Строковое представление товара"""
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        """Получение цены товара"""
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        """Установка цены товара с валидацией"""
        pass

    @abstractmethod
    def calculate_total_cost(self) -> float:
        """Расчёт общей стоимости товара на складе (цена × количество)"""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: Dict[str, Any]) -> Any:
        """Создание нового продукта или обновление существующего"""
        pass


class LoggingMixin:
    """Миксин для логирования создания объектов — выводит информацию о классе и параметрах инициализации."""

    def log_creation(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(BaseProduct, LoggingMixin):
    """Класс для представления характеристик товара"""

    product_list: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализирует новый экземпляр товара.
        При создании объекта автоматически добавляет его в список product_list."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.product_list.append(self)
        self.log_creation()

    def __str__(self) -> str:
        """Возвращает строковое представление товара: название, цена и остаток на складе."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self) -> float:
        """Возвращает цену товара."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Устанавливает цену товара с проверкой на корректность."""
        if value <= 0:
            raise ValueError("Цена не должна быть нулевой или отрицательной")
        self.__price = value

    def calculate_total_cost(self) -> float:
        """Рассчитывает общую стоимость товара на складе."""
        return self.price * self.quantity

    def check_change_price(self, new_price: float, user_confirmed: str = None) -> float:
        """Изменение цены в случае её понижения с согласия пользователя"""
        if self.price != new_price:
            if user_confirmed is None:
                user_confirmed = input("Вы уверены, что хотите изменить цену? (да/нет): ")
            if user_confirmed == "да":
                self.price = new_price
            elif user_confirmed != "нет":
                print("Некорректный ответ. Цена не изменена.")
        return self.price

    @classmethod
    def new_product(cls, product: Dict[str, Any]) -> Any:
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

    def __add__(self, other) -> float:
        """Получает полную стоимость всех товаров на складе."""
        if isinstance(other, Product):
            return self.calculate_total_cost() + other.calculate_total_cost()
        raise TypeError("Можно складывать только объекты класса Product")


class Smartphone(Product):
    """Класс товаров: Смартфоны"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self) -> str:
        """Расширенное строковое представление смартфона"""
        base_str = super().__str__()
        return (
            f"{base_str}, модель: {self.model}, память: {self.memory} ГБ, "
            f"цвет: {self.color}, эффективность: {self.efficiency}"
        )

    def __add__(self, other) -> float:
        """Получает полную стоимость смартфонов на складе"""
        if isinstance(other, Smartphone):
            return self.calculate_total_cost() + other.calculate_total_cost()
        raise TypeError("Можно складывать только смартфоны")


class LawnGrass(Product):
    """Класс товаров: Трава газонная"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        """Расширенное строковое представление газонной травы"""
        base_str = super().__str__()
        return (
            f"{base_str}, страна: {self.country}, период прорастания: "
            f"{self.germination_period}, цвет: {self.color}"
        )

    def __add__(self, other) -> float:
        """Получает полную стоимость газонной травы на складе"""
        if isinstance(other, LawnGrass):
            return self.calculate_total_cost() + other.calculate_total_cost()
        raise TypeError("Можно складывать только газонную траву")
