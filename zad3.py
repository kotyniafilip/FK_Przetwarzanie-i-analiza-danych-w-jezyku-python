class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property - Area: {self.area}, Rooms: {self.rooms}, Price: {self.price}, Address: {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        Property.__init__(self, area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House - {Property.__str__(self)}, Plot: {self.plot}"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        Property.__init__(self, area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat - {Property.__str__(self)}, Floor: {self.floor}"

house = House(area=200, rooms=5, price=500000, address="Grunwaldzka 40", plot=10)
flat = Flat(area=70, rooms=3, price=100000, address="Jaśminowa 50", floor=7)

print(house)
print(flat)