from .item import Item

class Decor(Item):
    def __init__(self, id=None, condition=0, width=0, length=0):
        super().__init__(id, condition)

        self.width, self.length = [width, length]
        self.category = "Decor"

    def __str__(self):
        string1 = super().__str__()
        string2 = f"It takes up a {self.width} by {self.length} sized space."

        return " ".join([string1,string2])