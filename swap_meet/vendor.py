class Vendor:
    
    def __init__(self, inventory=None):
        self.inventory = [] if inventory == None else inventory 
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        result = False
        if item in self.inventory:
            self.inventory.remove(item)
            result = item
        return result
    
    def get_by_id(self, item_id):

        results = None

        for item in self.inventory:
            if item.id == item_id:
                results = item
                break

        return results
