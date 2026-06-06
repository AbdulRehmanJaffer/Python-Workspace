class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):     
    def fare(self):
        amount = super().fare()
        maintenance_charge = amount * 0.10
        total_fare = amount + maintenance_charge
        return total_fare


# Create Bus object with seating capacity of 50
school_bus = Bus(50)

print("total Bus Fare is :", school_bus.fare())