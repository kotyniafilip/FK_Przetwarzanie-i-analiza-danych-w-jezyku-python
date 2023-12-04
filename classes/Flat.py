from classes.Property import Property

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        Property.__init__(self, area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat - {Property.__str__(self)}, Floor: {self.floor}"