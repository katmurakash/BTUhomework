#1
# class transport:
#     brand = "Tesla"
#     capacity = 5
#     speed = 180
#     fuel_type = "no fuel (electric energy)"
#2
class Transport:
    #4
    def __init__(self, name, capacity, speed, fuel_type):
        self.name = name
        self.capacity = capacity
        self.speed = speed
        self.fuel_type = fuel_type

    # 2
    @staticmethod
    def idle():
        print("manqana gacherebulia.")

    # 3
    @classmethod
    def create_car(cls, name, capacity, speed):
        return cls(name, capacity, speed, 'petrol')

    @classmethod
    def create_train(cls, name, capacity, speed):
        return cls(name, capacity, speed, 'diesel')

    # 5
    def time(self, distance):
        return distance / self.speed

    def fuel_type_info(self):
        if self.fuel_type == 'benzini':
            return 'gamoiyeneba benzini.'
        elif self.fuel_type == 'diesel':
            return 'gamoiyeneba dieseli.'
        else:
            return 'ucnobi swavavi.'

    # 6
    def __repr__(self):
        return f"{self.name} (Capacity: {self.capacity}, Speed: {self.speed}, Fuel: {self.fuel_type})"

# 7
car1 = Transport('Car', 5, 120, 'petrol')
train1 = Transport('Train', 200, 80, 'diesel')
car2 = Transport.create_car('SUV', 7, 150)
train2 = Transport.create_train('Express', 300, 100)
ship = Transport('Ship', 5000, 30, 'diesel')


Transport.idle()
print(car1)
print(train1)
print(car2)
print(train2)
print(ship)

print(f"Car fuel type : {car1.fuel_type_info()}")


