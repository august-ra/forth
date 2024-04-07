from io import StringIO

from settings import DATA_PATH, EMPTY_PATH
from products.categories import Categories
from products.category import Category
from products.product import Product


def test_get_data():
    categories = Categories.load_from_file(DATA_PATH)
    assert isinstance(categories.data, list)
    assert len(categories.data) > 0


def test_get_empty():
    categories = Categories.load_from_file(EMPTY_PATH)
    assert isinstance(categories.data, list)
    assert len(categories.data) == 0


def test_product_init():
    product = Product(name='test', description='test', price=100, quantity=10)
    assert product.name == 'test'
    assert product.description == 'test'
    assert product.price == 100
    assert product.quantity == 10


def test_price_reading():
    product = Product(name='test', description='test', price=100, quantity=10)
    assert product.price == 100


def test_price_writing_less_zero():
    product = Product(name='test', description='test', price=100, quantity=10)
    product.price = -10
    assert product.price == 100


def test_less_price_writing():
    product = Product(name='test', description='test', price=100, quantity=10)
    product.set_price(80, StringIO("n"))
    assert product.price == 100
    product.set_price(80, StringIO("y"))
    assert product.price == 80


def test_bigger_price_writing():
    product = Product(name='test', description='test', price=100, quantity=10)
    product.price = 120
    assert product.price == 120


def test_adding_same_products_to_category(product_in_category_before, product_in_category_after):
    category = Category(name='test', description='test', products=[])
    category.add_product(name='test', description='test', price=100, quantity=10)
    assert category.count_products == 1
    assert category.products == product_in_category_before
    category.add_product(name='test', description='test', price=120, quantity=5)
    assert category.count_products == 1
    assert category.products == product_in_category_after


def test_adding_different_products_to_category(product_in_category_before, products_in_category_after):
    category = Category(name='test', description='test', products=[])
    category.add_product(name='test', description='test', price=100, quantity=10)
    assert category.count_products == 1
    assert category.products == product_in_category_before
    category.add_product(name='test2', description='test2', price=120, quantity=5)
    assert category.count_products == 2
    assert category.products == products_in_category_after


def test_count_categories():
    category_1 = Category(name='test', description='test', products=[])
    category_2 = Category(name='test', description='test', products=[])
    categories = [category_1, category_2]
    categories = Categories(categories)
    assert categories.count_categories == 2


def test_count_products():
    product_1 = Product(name='test', description='test', price=100, quantity=10)
    product_2 = Product(name='test', description='test', price=100, quantity=10)
    products = [product_1, product_2]
    category = Category(name='test', description='test', products=products)
    assert category.count_products == 2


def test_empty_json(empty_categories):
    categories = Categories.load_from_file(EMPTY_PATH)
    assert categories.to_json() == empty_categories
