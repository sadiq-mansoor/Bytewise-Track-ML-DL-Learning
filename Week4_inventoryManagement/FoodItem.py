# FoodItem.py
from datetime import datetime

class FoodItem:
    def __init__(self, name, category, quantity, barcode, expiry_date):
        self.name = name
        self.category = category
        self.quantity = int(quantity)
        self.barcode = int(barcode)
        self.expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d")
        