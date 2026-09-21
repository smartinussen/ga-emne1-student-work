# OOP introduction

class Product:
    def __init__(self, name: str, price: float):
        self.product_name: str = name
        self.product_price: float = price

    def product_info(self):
        print(f"Name: {self.product_name}: {self.product_price:.2f} kr")

meieri = Product("Melk", 24.0)

meieri.product_info()
meieri.product_price = 33

meieri.product_info()
