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
