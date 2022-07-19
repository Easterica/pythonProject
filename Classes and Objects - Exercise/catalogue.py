class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = list()

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        return [product for product in self.products if product[0] == first_letter]

    def __repr__(self):
        string_for_return = f"Items in the {self.name} catalogue:\n"
        self.products = sorted(self.products)
        string_for_return += "\n".join(self.products)
        return string_for_return


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
