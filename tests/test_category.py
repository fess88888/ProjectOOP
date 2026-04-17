def test_category_init(category_1, category_2):

    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_1.products == ["Samsung Galaxy S23 Ultra", "Iphone 15", "Xiaomi Redmi Note 11"]
    assert len(category_1.products) == 3
    assert len(category_2.products) == 1

    assert category_1.category_count == 2
    assert category_1.product_count == 4
