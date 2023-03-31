class MotorcycleAdapter:

    def __init__(self, motorcycle):
        self.motorcycle = motorcycle

    def accelerate(self):
        self.motorcycle.rev_throttle()

    def apply_brakes(self):
        self.motorcycle.pull_brake_lever()

    def assign_driver(self, name):
        self.motorcycle.assign_rider(name)