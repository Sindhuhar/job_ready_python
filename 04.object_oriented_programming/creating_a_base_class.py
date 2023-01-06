class Person:
    def __init__(self,fname,lname):
        self.First_Name = fname
        self.Last_Name = lname

    def display(self):
        print(self.First_Name + " " + self.Last_Name)

x = Person("Ankitha","Iyer")
x.display()