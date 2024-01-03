class Animal:
    def make_sound(self):
        print("Generic Sound")
        
class Dog(Animal):
      def make_sound(self):
        print("Barking")

d1 = Dog()
d1.make_sound()