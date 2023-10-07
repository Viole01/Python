class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.quantity = qty

    def calculate_total_value(self):
        return self.price * self.quantity


class DiscountedProduct(Product):
    def __init__(self, name, price, qty, discount):
        super().__init__(name, price, qty)
        self.discount = discount

    def calculate_total_value(self):
        discounted_price = (self.price - (self.price * (self.discount / 100)))
        return discounted_price * self.quantity
