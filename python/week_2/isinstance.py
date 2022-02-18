class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School volvo", 12, 50)

school_bus_is_instance = isinstance(School_bus, Vehicle)
print(school_bus_is_instance)
