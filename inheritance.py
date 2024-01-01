class Vehical:
    def __init__(self,color,model) :
        self.color=color
        self.model=model
    def fuel(self):
        print("Vehical runs on fuel")
        
    def brakes(self):
        print("Apply brakes")
    
class Car(Vehical):
    def light(self):
        print("Lights On")
        
        
    
c1=Car("Black",2022)
print(c1.model)
print(c1.color)