import os

class Inventory():
    def __init__(self):
        self.items = {"Bricks": {"Quantity": 100, "Price": 10.50},
                 "Cement": {"Quantity": 100, "Price": 50.99},
                 "Concrete": {"Quantity": 100, "Price": 100.0},
                 "Steel": {"Quantity": 100, "Price": 120.5},
                 "Glass": {"Quantity": 100, "Price": 200.99},
                 "Tiles": {"Quantity": 100, "Price": 125.15}
                 }
        while True:
            print("1. Add Item")
            print("2. Remove Item")
            print("3. View inventory")
            print("4. Update Inventory")
            print("5. Exit")
            choice = input("Enter your choice : ")

            if choice == "1":
                os.system('cls')
                print("-----Add Item-----")
                name = input("Enter item name: ")
                if name in self.items.keys():
                    print("Item already exists")
                else:
                    quantity = int(input("Enter item quantity: "))
                    price = float(input("Enter item price: "))
                    self.add(name, quantity, price)
            
            elif choice == "2":
                os.system('cls')
                print("-----Remove Item-----")
                print("1. Remove Item")
                print("2. Remove Quantity")
                choice = input("Enter your choice: ")
                if choice == "1":
                    name = input("Enter item to remove: ")
                else:
                    name = input("Enter item name: ")
                    quantity = int(input("Enter quantity to remove: "))
                    self.remove_quantity(name, quantity)

            elif choice == "3":
                os.system('cls')
                print("-----View Inventory-----")

                self.view()
            
            elif choice == "4":
                os.system('cls')
                print("-----Update Item-----")
                name = input("Enter item name: ")
                quantity = int(input("Enter item's new quantity: "))
                price = float(input("Enter item's new price: "))

                self.update(name, quantity, price)
            
            elif choice == "5":
                break

            x = input("Return to main menu [y/n]? ")
            if x == 'y':
                os.system('cls')
                continue
            else:
                break

            exit(0)

    def add(self, name, quantity, price):
        while True:
            self.items[name] = {"Quantity": quantity, "Price": price}
            print('Item saved')
            x = input("Do you want to add another item [y/n]? ")
            if x == 'y':
                os.system('cls')
                continue
            else:
                break

    def remove_item(self, name):
        del self.items[name]

    def remove_quantity(self, name, quantity):
        self.items[name]["Quantity"] -= quantity
    
    def view(self):
        for item in self.items.items():
            print(*item)
    
    def update(self, name, quantity, price):
        self.items.update({name: {"Quantity": quantity, "Price": price}})

inventory = Inventory()