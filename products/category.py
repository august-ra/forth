from products.product import Product


class Category:

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        self.count_products = 0

        for _ in products:
            self.count_products += 1

    def __add_product(self, name, description, price, quantity):
        for product in self.__products:
            if product.name == name:
                product.price = max(product.price, price)
                product.quantity += quantity

                return None

        product = Product(name, description, price, quantity)
        self.__products.append(product)

        return product

    def add_product(self, name, description, price, quantity):
        product = self.__add_product(name, description, price, quantity)

        if product is None:
            return

        self.count_products += 1
        self.__products.append(product)

    @property
    def products(self):
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]
