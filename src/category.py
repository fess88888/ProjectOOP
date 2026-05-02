from src.product import Product


class Category:
    """Класс для представления категории товаров."""

    name: str
    description: str
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """Инициализирует новый экземпляр категории.
        При создании категории увеличивает статические счётчики:
        - category_count на 1 (количество категорий);
        - product_count на количество товаров в категории."""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """Возвращает строковое представление категории: название и общее количество единиц товара."""
        total_number_of_products = 0
        for product in self.__products:
            total_number_of_products += product.quantity
        return f"{self.name}, количество продуктов: {total_number_of_products} шт."

    def add_product(self, product_: Product) -> None:
        """Добавляет новый товар в категорию.
        Обновляет общий счётчик товаров (product_count), увеличивая его на 1."""
        if isinstance(product_, Product):
            self.__products.append(product_)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> str:
        """Возвращает форматированное строковое представление всех товаров в категории."""
        product_list = [f"{str(product_)}" for product_ in self.__products]
        return "\n".join(product_list) + "\n"

    @property
    def products_in_list(self) -> list[Product]:
        """Возвращает список товаров категории в виде Python‑списка."""
        return self.__products
