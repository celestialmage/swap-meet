from uuid import uuid4

class Item:
    def __init__(self, id=None):
        new_id = id if id != None else uuid4().int % (10**32)

        self.id = new_id
        self.category = "Item"

    def get_category(self):
        return self.category