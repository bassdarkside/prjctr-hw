# 1
class Product:
    def __init__(self, name: str, price: int | float, quantity: int):
        self.name = name
        if price > 0 and quantity > 0:
            self.price = price
            self.quantity = quantity
        else:
            raise ValueError(
                "'price' and 'quantity' must be greater than zero."
            )


class Book(Product):
    def __init__(
        self, name: str, price: int | float, quantity: int, author: str
    ):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self) -> str:
        name = f"name - '{self.name}'"
        price = f"price - {self.price*self.quantity}$"
        quantity = f"quantity - {self.quantity}"
        author = f"author - {self.author}"
        return f"About book: {name}, {price}, {quantity}, {author}."


book = Book("1984", 9.99, 3, "George Orwell")
print(book.read())

# 2


class Restaurant:
    def __init__(self, name: str, cuisine: str, menu: dict):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(self, name: str, cuisine: str, menu: dict, drive_thru: bool):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish: str, quantity: int):
        if quantity > 0:
            if self.menu.get(dish) is None:
                return "Dish not available"
                # raise ValueError("Dish not available")
            if quantity > self.menu[dish]["quantity"]:
                return "Requested quantity not available"
                # raise ValueError("Requested quantity not available")
            total_cost = self.update_menu(dish, quantity)
            return f"{total_cost}$"
        else:
            return f"Value must be greater than zero, but given {quantity}"
            # raise ValueError(f"Value must be greater than zero, but given {quantity}")

    def update_menu(self, dish: str, quantity: int):
        available_quantity = self.menu[dish]["quantity"]
        new_quantity = available_quantity - quantity
        self.menu[dish]["quantity"] = new_quantity
        total_cost = self.menu[dish]["price"] * quantity
        return total_cost


menu = {
    "burger": {"price": 5, "quantity": 10},
    "pizza": {"price": 10, "quantity": 20},
    "drink": {"price": 1, "quantity": 15},
}

mc = FastFood("McDonalds", "Fast Food", menu, True)

print(mc.order("burger", 5))  # 25
print(mc.order("burger", 15))  # Requested quantity not available
print(mc.order("soup", 5))  # Dish not available
