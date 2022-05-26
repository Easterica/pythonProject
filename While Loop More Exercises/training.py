class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity = 0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate(self):
        return self.price * self.quantity

    def __repr__(self):
        return self.name



item1 = Item("Gosho", 100)
item2 = Item("Pesho", 200)

print(Item.all)