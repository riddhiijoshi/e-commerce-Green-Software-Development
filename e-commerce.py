from codecarbon import OfflineEmissionsTracker

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def display_cart(self):
        if not self.products:
            print("Your cart is empty. Please add items to your cart.")
        else:
            print("Items in your cart are as follows:")
            for product in self.products:
                print(f"- {product.name} (${product.price})")

    def remove_from_cart(self, product):
        if product in self.products:
            self.remove_product(product)
            print(f"Successfully removed {product.name} from the cart.")
        else:
            print(f"{product.name} is not present in your cart.")


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product):
        self.shopping_cart.add_product(product)

    def remove_from_cart(self, product):
        self.shopping_cart.remove_from_cart(product)

    def checkout(self):
        total = self.shopping_cart.calculate_total()
        print(f"Total amount to pay: ${total}")


# Sample usage
product1 = Product(1, "Kindle", 50000)
product2 = Product(2, "Smartwatch", 10000)
product3 = Product(3, "iPhone", 75000)
product4 = Product(4, "Laptop", 30000)
product5 = Product(5, "iPad", 20000)
product6 = Product(6, "Washing machine", 10250)

customer = Customer("John Doe", "john@example.com")

print("Welcome to our online store!")
print("Here are some available products:")

products = [product1, product2, product3, product4, product5, product6]

for product in products:
    print(f"{product.id}. {product.name} - ${product.price}")

tracker = OfflineEmissionsTracker(country_iso_code="IND")
tracker.start()

while True:
    print("\nPlease select an option from below:")
    print("1. Add a product to the cart")
    print("2. Display cart")
    print("3. Remove a product from the cart")
    print("4. Checkout")
    print("-----------------------------------------------")
    user_input = input("Enter your choice: ")
    
    if user_input == '1':
        print("\nSelect a product to add to the cart:")
        product_id = int(input("Product ID: "))
        selected_product = next((product for product in products if product.id == product_id), None)
        if selected_product:
            customer.add_to_cart(selected_product)
            print(f"Added {selected_product.name} to the cart.")
        else:
            print("Invalid product ID. Please try again.")

    elif user_input == '2':
        customer.shopping_cart.display_cart()

    elif user_input == '3':
        print("\nSelect a product to remove from the cart:")
        product_id = int(input("Product ID: "))
        selected_product = next((product for product in customer.shopping_cart.products if product.id == product_id), None)
        if selected_product:
            customer.remove_from_cart(selected_product)
        else:
            print("Invalid product ID. Please try again.")

    elif user_input == '4':
        customer.checkout()
        break

    else:
        print("Invalid option. Please try again.")

tracker.stop()
