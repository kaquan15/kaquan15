class Shop:
     def __init__(self, name, items):
        self.name = name
        self.items = items

     def get_items_count(self):
        #cho biet so luong mat hang co trong cua hang
        return len(self.items)

#Test code
shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])

print(shop.get_items_count())