from products.product import Product


class Category:

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        self.count_products = 0

        for _ in products:
            self.count_products += 1

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)}"

    def __len__(self):
        result = 0

        for product in self.__products:
            result += product.quantity

        return result

    def __add_product(self, name, description, price, quantity):
        for product in self.__products:
            if product.name == name:
                product.price = max(product.price, price)
                product.quantity += quantity

                return None

        product = Product(name, description, price, quantity)

        return product

    def add_product(self, name, description, price, quantity):
        product = self.__add_product(name, description, price, quantity)

        if product is None:
            return

        self.count_products += 1
        self.__products.append(product)

    @property
    def products(self):
        return "\n".join([f"{product}" for product in self.__products])
