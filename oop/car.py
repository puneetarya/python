class car:
    def __init__(self, make, model, year, mileage) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, distance_travelled):
        self.mileage += distance_travelled

    def get_info(self):
        return "The car made by {} {} of year {} with mileage {}".format(self.make, self.model, self.year, self.mileage)
