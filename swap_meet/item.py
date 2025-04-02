from uuid import uuid4

class Item:
    def __init__(self, id=None, condition=0):
        new_id = id if id != None else int(uuid4().hex, 16)

        self.id = new_id
        self.condition = condition
        self.category = "Item"

    def get_category(self):
        return self.category
    

    def __str__(self):
        return f"An object of type {self.category} with id {self.id}."
    
    def condition_description(self):
        descriptions = {
            0: "barely holding together",
            1: "Has seen some things",
            2: "Great from a distance",
            3: "Gently used",
            4: "Loved",
            5: "Still in the box"
        }
        return descriptions[self.condition]