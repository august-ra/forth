import json
from products.category import Category
from products.product import Product


class Categories:

    count_categories = 0
    count_products = 0

    def __init__(self, data):
        self.data = data

    @classmethod
    def load_from_file(cls, file):
        with open(file, 'r') as f:
            data = json.load(f)

        if not data:
            return None

        categories = []

        for category in data:
            Categories.count_categories += 1  # total

            products = []

            for product in category['products']:
                Categories.count_products += 1  # total

                products.append(Product(product['name'], product['description'], product['price'], product['quantity']))

            categories.append(Category(category['name'], category['description'], products))

        # total
        Category.count_categories = Categories.count_categories
        Category.count_products = Categories.count_products

        return cls(categories)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
