class Inventory:
    def __init__(self):
        """Initialize the inventory."""
        self.stock = {}

    def add_product(self, product, quantity):
        """Add a product to the inventory."""
        if product in self.stock:
            self.stock[product] += quantity
        else:
            self.stock[product] = quantity

    def check_availability(self, product):
        """Check if a product is in stock."""
        return product in self.stock and self.stock[product] > 0

    def make_sale(self, product, quantity):
        """Make a sale and reduce stock."""
        if not self.check_availability(product):
            raise ValueError("Product is out of stock.")
        if quantity > self.stock[product]:
            raise ValueError("Not enough stock to fulfill the sale.")
        self.stock[product] -= quantity

    def get_stock_level(self, product):
        """Get the current stock level of a product."""
        return self.stock.get(product, 0)

    def print_inventory(self):
        """Print the current inventory levels."""
        for product, quantity in self.stock.items():
            print(f"{product}: {quantity}")


def main():
    """Main function."""
    inventory = Inventory()
    inventory.add_product("Apple", 10)
    inventory.add_product("Banana", 20)
    inventory.add_product("Orange", 30)

    print("Initial Inventory:")
    inventory.print_inventory()

    print("\nChecking availability:")
    print(f"Apple: {inventory.check_availability('Apple')}")
    print(f"Banana: {inventory.check_availability('Banana')}")
    print(f"Orange: {inventory.check_availability('Orange')}")
    print(f"Grapes: {inventory.check_availability('Grapes')}")

    print("\nMaking sales:")
    inventory.make_sale("Apple", 5)
    inventory.make_sale("Banana", 10)
    try:
        inventory.make_sale("Orange", 50)
    except ValueError as e:
        print(e)

    print("\nUpdated Inventory:")
    inventory.print_inventory()

    print("\nGetting stock levels:")
    print(f"Apple: {inventory.get_stock_level('Apple')}")
    print(f"Banana: {inventory.get_stock_level('Banana')}")
    print(f"Orange: {inventory.get_stock_level('Orange')}")
    print(f"Grapes: {inventory.get_stock_level('Grapes')}")


if __name__ == "__main__":
    main()