from car import Car
from motorcycle import Motorcycle
from motorcycle_adapter import MotorcycleAdapter
import traceback

if __name__ == '__main__':
    car = Car()

    print("The Car\n")
    car.assign_driver("Sushant")
    car.accelerate()
    car.apply_brakes()
    print("\n")

    print("Attempting to call client methods with the service object\n")

    bike = Motorcycle()
    
    bike_adapter = MotorcycleAdapter(bike)

    print("The Motorcycle\n")
    bike_adapter.assign_driver("Subodh")
    bike_adapter.accelerate()
    bike_adapter.apply_brakes()
    print("\n")