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
    
    def swap_items(self, other_vendor, my_item, their_item):
        
        result = False

        if my_item in self.inventory and their_item in other_vendor.inventory:
                self.remove(my_item)
                other_vendor.remove(their_item)
                self.add(their_item)
                other_vendor.add(my_item)
                result = True
        return result

    def swap_first_item(self, other_vendor):

        result = False

        if self.inventory and other_vendor.inventory:
            self_item = self.inventory[0]
            self.inventory[0] = other_vendor.inventory[0]
            other_vendor.inventory[0] = self_item
            result = True

        return result
    
    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]
    
    def get_best_by_category(self, category):
        category_list = self.get_by_category(category)

        best_item = None

        for item in category_list:

            if not best_item or item.condition > best_item.condition:
                best_item = item

        return best_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):

        my_best = self.get_best_by_category(their_priority)
        their_best = other_vendor.get_best_by_category(my_priority)

        valid_trade = my_best and their_best

        if valid_trade:

            self.remove(my_best)
            self.add(their_best)

            other_vendor.remove(their_best)
            other_vendor.add(my_best)

        return valid_trade