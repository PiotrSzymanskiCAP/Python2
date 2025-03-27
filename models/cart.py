import uuid


class Cart:

    def __init__(self, id: int, user_id: int):
        self._uuid = uuid.uuid4()
        self._id = id
        self._user_id = user_id
        self._products = {}

    def add_product(self, product_id, quantity):
        if product_id in self._products:
            self._products[product_id] += quantity
        else:
            self._products[product_id] = quantity

    def remove_product(self, product_id, quantity):
        if product_id in self._products:
            if self._products[product_id] > quantity:
                self._products[product_id] -= quantity
            elif self._products[product_id] == quantity:
                del self._products[product_id]
            else:
                print("Error: Not enough quantity to remove.")
        else:
            print("Error: Product not found in Cart.")

    def get_total_items(self):
        return sum(self._products.values())

    def __repr__(self):
        return f"Cart with ID: {self._id}, for user with ID: {self._user_id} -> Products(ID, Quantity) {self._products !r}\n"
