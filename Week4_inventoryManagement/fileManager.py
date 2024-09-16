# file_manager.py
import csv
from .inventory import Inventory
import os
from .FoodItem import FoodItem

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def read_csv(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                inventory = Inventory()
                for row in reader:
                    item = FoodItem(*row)
                    inventory.add_item(item)
                return inventory
        except FileNotFoundError:
            print("File not found.")
            return None

    def write_csv(self, inventory):
        try:
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Category", "Quantity", "Barcode", "Expiry Date"])
                for item in inventory.items:
                    writer.writerow([item.name, item.category, item.quantity, item.barcode, item.expiry_date.strftime("%Y-%m-%d")])
        except IOError:
            print("Error writing to file.")
