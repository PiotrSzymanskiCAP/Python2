class Cart:

    # DOMAIN MODELS
    def __init__(self, cart_id: int, user_id: int, products: dict):
        self._cart_id = cart_id
        self._user_id = user_id
        self._products = products

    # # just normal adding product with already defined quantity
    # def add_product(self, product_id, quantity):
    #     if product_id in self._products:
    #         self._products[product_id] += quantity
    #     else:
    #         self._products[product_id] = quantity

    def __repr__(self):
        return f"Cart with ID: {self._cart_id}, for user with ID: {self._user_id} -> Products(ID, Quantity) {self._products !r}\n"
