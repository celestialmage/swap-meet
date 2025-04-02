from .item import Item

class Clothing(Item):
    def __init__(self, id=None, condition=0, fabric="Unknown"):
        super().__init__(id, condition)

        self.fabric = fabric
        self.category = "Clothing"

    def __str__(self):
        string1 = super().__str__()
        string2 = f"It is made from {self.fabric} fabric."

        return " ".join([string1,string2])