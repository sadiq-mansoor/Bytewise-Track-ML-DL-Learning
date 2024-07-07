# inventory.py
from .FoodItem import FoodItem
from datetime import datetime, timedelta

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def edit_item(self, barcode, **kwargs):
        for item in self.items:
            if item.barcode == barcode:
                for key, value in kwargs.items():
                    setattr(item, key, value)
                return True
        print("Item not found.")
        return False

    def delete_item(self, barcode):
        for item in self.items:
            if item.barcode == barcode:
                self.items.remove(item)
                return True
        print("Item not found.")
        return False

    def search_item(self, barcode):
        for item in self.items:
            if item.barcode == barcode:
                return item
        raise ValueError("Item not found.")

    def near_expiry_items(self):
        today = datetime.today()
        for item in self.items:
            if item.expiry_date - today < timedelta(days=7) and item.expiry_date >= today:
                yield item
    