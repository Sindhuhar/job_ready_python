class Manager:
    level = "L1"  # this is a class attribute shared among all objects

    def __init__(self, fname, lname):
        self.fname = fname  # instance attribute tied to the object
        self.lname = lname  # instance attribute tied to the object


p1 = Manager("Ankitha", "Hegde")
print(p1.fname)
print(p1.level)
p2 = Manager("Sushmitha", "Aachar")
print(p2.fname)
print(p2.level)