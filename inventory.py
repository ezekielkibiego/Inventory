import csv

class InventoryItem:
    def __init__(self, name,  quantity, price):
        self.name = name
        
        self.quantity = quantity
        self.price = price

class InventoryManagementSystem:
    def __init__(self):
        self.inventory = []
    
    def add_item(self, item):
        self.inventory.append(item)
    
    def remove_item(self, item):
        self.inventory.remove(item)
    
    def update_item(self, item, quantity=None, price=None):
        if quantity:
            item.quantity = quantity
        if price:
            item.price = price
    
    def display_inventory(self):
        for item in self.inventory:
            print(f"{item.name} - Quantity: {item.quantity}, Price: {item.price}")
    
    def load_inventory(self, file):
        with open(file, mode='r') as f:
            reader = csv.reader(f)
            for row in reader:
                item = InventoryItem(row[0], int(row[1]), float(row[2]))
                self.add_item(item)
    
    def save_inventory(self, file):
        with open(file, mode='w', newline='') as f:
            writer = csv.writer(f)
            for item in self.inventory:
                writer.writerow([item.name, item.quantity, item.price])

def main():
    ims = InventoryManagementSystem()
    ims.load_inventory('inventory.csv')
    
    while True:
        print("1. Add item")
        print("2. Remove item")
        print("3. Update item")
        print("4. Display inventory")
        print("5. Save inventory")
        print("6. Quit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            item = InventoryItem(name, quantity, price)
            ims.add_item(item)
        
        elif choice == '2':
            name = input("Enter item name: ")
            item = next((item for item in ims.inventory if item.name == name), None)
            if item:
                ims.remove_item(item)
            else:
                print("Item not found")
        
        elif choice == '3':
            name = input("Enter item name: ")
            item = next((item for item in ims.inventory if item.name == name), None)
            if item:
                quantity = input("Enter new quantity (leave blank to skip): ")
                if quantity:
                    quantity = int(quantity)
                price = input("Enter new price (leave blank to skip): ")
                if price:
                    price = float(price)
                ims.update_item(item, quantity, price)
            else:
                print("Item not found")
        
        elif choice == '4':
            ims.display_inventory()
        
        elif choice == '5':
            ims.save_inventory('inventory.csv')
        
        elif choice == '6':
            break
        
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()
