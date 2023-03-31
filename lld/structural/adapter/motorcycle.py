import random

class Motorcycle:
    def __init__(self):
        self.generator = random.Random()

    def rev_throttle(self):
        random_num = self.generator.randint(50, 100)
        speed = random_num
        print(f"The speed of the motorcycle is {speed} mph")

    def pull_brake_lever(self):
        random_num = self.generator.randint(20, 40)
        speed = random_num
        print(
            f"The speed of the motorcycle is {speed} mph after applying the brakes")

    def assign_rider(self, rider_name):
        print(f"{rider_name} is riding the motorcycle") 