class Car:
    # dunder
    def __init__(self,model,Brand,color):
        self.Model=model
        self.Brand=Brand
        self.color=color
        self.is_runing=False
    
    def start(self):
        if self.is_runing==True:
            print(f"{self.Brand} is already running")
        else:
            self.is_runing=True
            print(f"{self.Brand} is now  running")
    def stop(self):
        if self.is_runing==True:
            self.is_runing=False
            print(f"{self.Brand} is now Stoped")
        else:
            print(f"{self.Brand} is already stoped")    
    def display(self):
        print(f"Car Brand Name : {self.Brand}\nCar Model : {self.Model}\nCar Color : {self.color}")
          
        
            
c1=Car(2007,"Civic","white")
c2=Car(2021,'bmw','black')
c1.display()
c2.display()
# c1.start()
# c1.stop()


    
    

