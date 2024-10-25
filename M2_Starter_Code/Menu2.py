# This line defines a class named 'FoodTruck'.
class FoodTruck:
    # __init__ is the constructor method, which initializes the instance of the class when it is created.
    # self.menus is a dictionary that stores various food categories (Snacks, Meals, Drinks, Dessert) and their respective items, each with an id, name, and price.
    # self.order is an empty list that will hold the items ordered by the customer.
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
                {"id": 6, "name": "Tea - Irish breakfast", "price": 2.49},
                {"id": 7, "name": "Coffee - Espresso", "price": 2.99},
                {"id": 8, "name": "Coffee - Flat white", "price": 2.99},
                {"id": 9, "name": "Coffee - Iced", "price": 3.49},
            ]},
            4: {"Dessert": []}
        }
        self.order = []
# This method takes a category
# as an argument and displays the items in that category.

    def display_menu(self, category):
     #  Retrieves the name of the menu and its items from the menus dictionary based on the provided
     # Category
        menu_name, items = list(self.menus[category].items())[0]
# Prints the header for the menu display
        print(f"\n{menu_name} Menu:")
        print(f"{'Item #':<8} | {'Item name':<20} | {'Price':>6}")
        print("-" * 40)
# Loops through the items and prints their id, name, and price in a formatted way
        for item in items:
            print(
                f"{item['id']:<8} | {item['name']:<20} | ${item['price']:.2f}")
# This method allows the user to add items to their order based on a selected category

    def add_to_order(self, category):
        self.display_menu(category)
# Prompts for the item id and quantity (defaulting to 1 if not specified)
        item_id = int(input("\nType menu number: "))
        quantity = input("Enter quantity (default is 1): ").strip()
        quantity = int(quantity) if quantity else 1

        menu_name, items = list(self.menus[category].items())[0]
# Looks for the item in the list and appends it to the order list with its quantity
        for item in items:
            if item['id'] == item_id:
                self.order.append((item, quantity))
                break
# This method displays the customer's order and calculates the total price

    def display_order(self):
        print("\nThank you for your order. This is what we are preparing for you:")
# Initializes a variable to track the total price
        total_price = 0
        print(f"{'Item name':<20} | {'Price':>6} | {'Quantity':>8}")
        print("-" * 42)
# Loops through the order items and prints each item with its price and quantity, while calculating the total
        for item, quantity in self.order:
            print(f"{item['name']:<20} | ${item['price']:.2f} | {quantity:>8}")
            total_price += item['price'] * quantity
        print(f"\nTotal price: ${total_price:.2f}")
# This method contains the main loop that facilitates interaction with the user

    def run(self):
        # Starts an infinite loop, allowing the user to continue ordering until they choose to stop
        while True:
            try:
                print("\nFrom which menu would you like to order?")
# Displays the available menu categories for the user to choose from
                for key, value in self.menus.items():
                    print(f"{key}\t{list(value.keys())[0]}")
                category = int(input("Type menu number: "))

                if category not in self.menus:
                    print("Invalid choice, please try again.")
                    continue
# Calls the method to add an item to the order
                self.add_to_order(category)
# Asks the user if they want to continue ordering
                keep_ordering = input(
                    "Would you like to keep ordering? (Y)es or (N)o: ").strip().lower()
                if keep_ordering != 'y':
                    break

            except ValueError:
                print("Invalid input, please try again.")

        self.display_order()


# This conditional checks if the script is being run directly
# Creates an instance of the FoodTruck class and calls the run method to start the program.
if __name__ == "__main__":
    truck = FoodTruck()
    truck.run()
