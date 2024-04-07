import json
from products.category import Category
from products.product import Product


class Categories:

    def __init__(self, data):
        self.data = data

        self.count_categories = 0
        self.count_products = 0

        for category in data:
            self.count_categories += 1
            self.count_products += category.count_products

    @classmethod
    def load_from_file(cls, file):
        with open(file, 'r') as f:
            data = json.load(f)

        if not data:
            return cls([])

        categories = []

        for category in data:
            products = []

            for product in category['products']:
                products.append(Product(product['name'], product['description'], product['price'], product['quantity']))

            categories.append(Category(category['name'], category['description'], products))

        return cls(categories)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
