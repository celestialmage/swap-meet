from .item import Item

class Electronics(Item):
    def __init__(self, id=None, condition=0, type="Unknown"):
        super().__init__(id, condition)

        self.type = type
        self.category = "Electronics"

    def __str__(self):
        string1 = super().__str__()
        string2 = f"This is a {self.type} device."

        return " ".join([string1,string2])
