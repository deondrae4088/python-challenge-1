class FoodTruck:
    def __init__(self):
        self.menus = {
            1: {"Snacks": []},
            2: {"Meals": [
                {"id": 1, "name": "Burrito", "price": 4.49},
                {"id": 2, "name": "Teriyaki Chicken", "price": 9.99},
                {"id": 3, "name": "Sushi", "price": 7.49},
                {"id": 4, "name": "Pad Thai", "price": 6.99},
                {"id": 5, "name": "Pizza - Cheese", "price": 8.99},
                {"id": 6, "name": "Pizza - Pepperoni", "price": 10.99},
                {"id": 7, "name": "Pizza - Vegetarian", "price": 9.99},
                {"id": 8, "name": "Burger - Chicken", "price": 7.49},
                {"id": 9, "name": "Burger - Beef", "price": 8.49},
            ]},
            3: {"Drinks": [
                {"id": 1, "name": "Soda - Small", "price": 1.99},
                {"id": 2, "name": "Soda - Medium", "price": 2.49},
                {"id": 3, "name": "Soda - Large", "price": 2.99},
                {"id": 4, "name": "Tea - Green", "price": 2.49},
                {"id": 5, "name": "Tea - Thai iced", "price": 3.99},
                {"id": 6, "name": "Tea - Iris breakfast", "price": 2.49},
                {"id": 7, "name": "Coffee - Espresso", "price": 2.99},
                {"id": 8, "name": "Coffee - Flat white", "price": 2.99},
                {"id": 9, "name": "Coffee - Iced", "price": 3.49},
            ]},
            4: {"Dessert": []}
        }
        self.order = []

    def display_menu(self, category):
        menu_name, items = list(self.menus[category].items())[0]
        print(f"\n{menu_name} Menu:")
        print(f"{'Item #':<8} | {'Item name':<20} | {'Price':>6}")
        print("-" * 40)
        for item in items:
            print(
                f"{item['id']:<8} | {item['name']:<20} | ${item['price']:.2f}")

    def add_to_order(self, category):
        self.display_menu(category)
        item_id = int(input("\nType menu number: "))
        quantity = input("Enter quantity (default is 1): ").strip()
        quantity = int(quantity) if quantity else 1

        menu_name, items = list(self.menus[category].items())[0]
        for item in items:
            if item['id'] == item_id:
                self.order.append((item, quantity))
                break

    def display_order(self):
        print("\nThank you for your order. This is what we are preparing for you:")
        total_price = 0
        print(f"{'Item name':<20} | {'Price':>6} | {'Quantity':>8}")
        print("-" * 42)
        for item, quantity in self.order:
            print(f"{item['name']:<20} | ${item['price']:.2f} | {quantity:>8}")
            total_price += item['price'] * quantity
        print(f"\nTotal price: ${total_price:.2f}")

    def run(self):
        while True:
            try:
                print("\nFrom which menu would you like to order?")
                for key, value in self.menus.items():
                    print(f"{key}\t{list(value.keys())[0]}")
                category = int(input("Type menu number: "))

                if category not in self.menus:
                    print("Invalid choice, please try again.")
                    continue

                self.add_to_order(category)

                keep_ordering = input(
                    "Would you like to keep ordering? (Y)es or (N)o: ").strip().lower()
                if keep_ordering != 'y':
                    break

            except ValueError:
                print("Invalid input, please try again.")

        self.display_order()


if __name__ == "__main__":
    truck = FoodTruck()
    truck.run()
