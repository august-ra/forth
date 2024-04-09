import pytest


@pytest.fixture
def empty_categories():
    return """{
    "count_categories": 0,
    "count_products": 0,
    "data": []
}"""
