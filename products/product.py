
class Product:

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена некорректная, отмена действия")

            return
        elif value < self.__price:
            waits = "(y/n или д/н)"
            user_input = input(f"Устанавливаемая цена ниже текущей, подтвердите действие {waits}: ").strip().lower()

            if user_input != 'y' and user_input != 'д':
                return

        self.__price = value
