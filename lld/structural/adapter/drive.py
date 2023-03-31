from car import Car
from motorcycle import Motorcycle
import traceback

if __name__ == '__main__':
    car = Car()
    bike = Motorcycle()

    print("The Motorcycle\n")
    bike.assign_rider("Subodh")
    bike.rev_throttle()
    bike.pull_brake_lever()
    print("\n")

    print("The Car\n")
    car.assign_driver("Sushant")
    car.accelerate()
    car.apply_brakes()
    print("\n")

    print("Attempting to call client methods with the service object\n")

    try:
        bike.assign_driver("Robert")
        bike.accelerate()
        bike.apply_brakes()
    except AttributeError:
        print("Oops! bike object cannot access car methods")
        traceback.print_exc()
