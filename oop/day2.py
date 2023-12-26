class Car:
    def __init__(self,brand,color):
        self.Brand=brand
        self.Color=color
        self.is_runing=False
        print("this is init method")
    def start(self):
        if self.is_runing:
            print(f"{self.Brand} is already Start")
        else:
            self.is_runing=True
            print(f"{self.Brand} is now start")
    def stop(self):
        if self.is_runing:
            self.is_runing=False
            print(f"{self.Brand}  now stop")
        else:
            print(f"{self.Brand}  already stop")
        



c1=Car("toyota",'Black')
c2=Car("bmw","white")

# c1.start()
# c2.start()
# c1.stop()
# c2.stop()