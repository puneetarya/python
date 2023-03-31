# Military & Commercial Planes
class Plane:
    def __init__(self, Carrier):
        self.carrier = Carrier
        
    def display_description(self):
        pass
    
    def add_objects(self):
        pass
    
class Commercial(Plane):
    def __init__(self, Carrier, objects):
        super().__init__(Carrier)
        self.objects = objects

    def display_description(self):
        self.carrier.carry_commercial(self.objects)

    def add_objects(self, new_objects):
        self.objects += new_objects   

class Military(Plane):
    def __init__(self, Carrier, objects):
        super().__init__(Carrier)
        self.objects = objects

    def display_description(self):
        self.carrier.carry_military(self.objects)

    def add_objects(self, new_objects):
        self.objects += new_objects