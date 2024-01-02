class Person:
    def __init__(self, first_name,middle_name,last_name, age):
        self.first_name=first_name
        self.middle_name=middle_name
        self.last_name=last_name
        self.age=age
    
    def __repr__(self):

        return f"<Person first_name={self.first_name} last_name={self.last_name} age={self.age}> "
    
    def is_adult(self):
        if self.age>=18:
            return True
        else:
            return False
class Student(Person): 
    def __init__(self, first_name,middle_name,last_name, age,roll_no):
        super().__init__(first_name,middle_name,last_name, age)
        self.roll_no=roll_no
    def display(self):
        print(self.roll_no)
      
  

# p1=Person("Jan", "van" ,"Dijk",18)
# print(p1)
# print(p1.is_adult())

s1=Student("John", "Doe" ,"John",17,77)
print(s1)
print(s1.is_adult())
s1.display()
