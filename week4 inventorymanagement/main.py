# main.py
from main_package import FileManager
from main_package import inventory
from main_package import FoodItem

def main():
    # Create an instance of FileManager with the correct file path
    file_manager = FileManager('D:\\BWT\\Week4_inventoryManagement\\main_package\\inventory.csv')

    # Read data from the CSV file
    inventory = file_manager.read_csv()

    # Example usage: Add a new item
    new_item = FoodItem("Orange", "Fruit", 15, 987654, "2023-06-10")
    inventory.add_item(new_item)

    # Example usage: Edit an existing item
    inventory.edit_item(123456, quantity=25)

    # Example usage: Search for an item
    try:
        searched_item = inventory.search_item(789012)
        print(f"Found item: {searched_item.name} ({searched_item.category})")
    except ValueError as e:
        print(e)

    # Example usage: Get near expiry items
    near_expiry_items = inventory.near_expiry_items()
    print("Near expiry items:")
    for item in near_expiry_items:
        print(f"{item.name} ({item.expiry_date.strftime('%Y-%m-%d')})")

    # Write updated data back to the CSV file
    file_manager.write_csv(inventory)

if __name__ == "__main__":
    main()