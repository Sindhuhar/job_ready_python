class person:
    def __init__(self,fname,lname):
        self.First_name = fname
        self.Last_name = lname
    def display_info(self):
        print("Person First name: " + self.First_name)
        print("Person Last name: " + self.Last_name)

Person_1 = person("Virat","Kohli")
Person_1.display_info()
Person_2 = person("Yuvaraj","Singh")
Person_2.display_info()