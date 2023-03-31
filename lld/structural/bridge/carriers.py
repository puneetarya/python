class Carrier:
    def carry_military(self, items):
        pass
    
    def carry_commercial(self, items):
        pass
    
class Cargo(Carrier):
    def carry_military(self, items):
        print("The plane carries ", items," military cargo goods")
        
    def carry_commercial(self, items):
        print("The plane carries ", items," commercial cargo goods") 

class Passenger(Carrier):
    def carry_military(self, passengers):
        print("The plane carries ",  passengers , " military passengers")
        
    def carry_commercial(self, passengers):
        print("The plane carries ",  passengers , " commercial passengers")