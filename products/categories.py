import json

from products.category import Category
from products.product import Product


class Categories:

    data = []
    count_categories = 0
    count_products = 0

    def __init__(self, data):
        self.data = data

        self.count_categories = 0
        self.count_products = 0

        for category in data:
            self.count_categories += 1
            self.count_products += category.count_products


    @classmethod
    def count_inner(cls):
        cls.count_categories = 0
        cls.count_products = 0

        for category in cls.data:
            cls.count_categories += 1
            cls.count_products += category.count_products

    @classmethod
    def load_from_data(cls, categories: list):
        cls.data = categories
        cls.count_inner()

    @classmethod
    def load_from_file(cls, file) -> bool:
        with open(file, 'r') as f:
            data = json.load(f)

        if not data:
            return False

        cls.data = []

        for category in data:
            products = []

            for product in category['products']:
                products.append(Product(product['name'], product['description'], product['price'], product['quantity']))

            cls.data.append(Category(category['name'], category['description'], products))

        cls.count_inner()

        return True

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
