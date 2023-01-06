class Person:  # This is a parent class or base class
    def __init__(self,fname,lname):
        self.First_name = fname
        self.Last_name = lname

    def display(self):
        print(self.First_name + " " + self.Last_name)

# Create employee class that inherits from person class.
class Employee(Person):
    pass
e=Employee("Harsha","Vardhana")
e.display()