class Inventory:


    def __init__(self, capacity):
        self.capacity = capacity
        self.items = list()
        self.__capacity = capacity

    def add_item(self, item):
        if self.capacity > 0:
            self.items.append(item)
        else:
            return "not enough room in inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {','.join(self.items)}\nCapacity left: {self.capacity}"


inventory = Inventory(2)
inventory.add_item("potion")    
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
