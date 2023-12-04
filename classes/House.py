from classes.Property import Property

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        Property.__init__(self, area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House - {Property.__str__(self)}, Plot: {self.plot}"