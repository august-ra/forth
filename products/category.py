
class Category:

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        self.count_products = 0

        for _ in products:
            self.count_products += 1
