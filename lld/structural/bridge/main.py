from carriers import Cargo, Passenger
from planes import Military, Commercial


cargo = Cargo()
passenger = Passenger()

# Bridging Military and Cargo classes
military1 = Military(cargo , 100)
military1.display_description()
military1.add_objects(25)
military1.display_description()


# Bridging Commercial and Passenger
commercial1 = Commercial(passenger , 400)
commercial1.display_description()
commercial1.add_objects(50)
commercial1.display_description()