import pytest


@pytest.fixture
def empty_categories():
    return """{
    "count_categories": 0,
    "count_products": 0,
    "data": []
}"""


@pytest.fixture
def product_in_category_before():
    return 'test, 100 руб. Остаток: 10 шт.'


@pytest.fixture
def product_in_category_after():
    return 'test, 120 руб. Остаток: 15 шт.'


@pytest.fixture
def products_in_category_after():
    return 'test, 100 руб. Остаток: 10 шт.\ntest2, 120 руб. Остаток: 5 шт.'
