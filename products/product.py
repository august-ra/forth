from sys import stdin, stdout


class Product:

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        return self.__price * self.quantity + other.__price * other.quantity

    def set_price(self, value: float, _in=stdin):
        if value <= 0:
            print("Цена некорректная, отмена действия")

            return
        elif value < self.__price:
            waits = "(y/n или д/н)"
            stdout.write(f"Устанавливаемая цена ниже текущей, подтвердите действие {waits}: ")
            user_input = _in.readline().strip().lower()

            if user_input != 'y' and user_input != 'д':
                return

        self.__price = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        self.set_price(value, stdin)
