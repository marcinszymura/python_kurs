# # class monitor:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def __str__(self):
#         return f'<monitor {self.brand} | {self.model}>'
#
#     def wlacz(self):
#         print(self, 'on')
#
# d = int()
# m = monitor('Philips', 'M01')
# m2 = monitor('Sony', 'B2')
#
# print(m)
# print(m2)
# print(m2.brand)
# m.wlacz()

class product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f'Produkt \"{self.name}\", id: {self.id}, cena: {self.price} PLN'

    def print_info(self):
        print(self)

item = product('1', 'woda', '10.99')
product.print_info(item)