class BankCustomer:
    def __init__(self,c_id,fname,lname):
        self.First_Name = fname
        self.Last_Name = lname
        self.Customer_id = c_id

    def display_info(self):
        print("Customer's First Name is: " + self.First_Name)
        print("Customer's Last Name is: " + self.Last_Name)
        print("Customer's id Name is: " + str(self.Customer_id))

class BankAccount:
    def __init__(self,a_id,name,type):
        self.account_id = a_id
        self.account_name = name
        self.account_type = type

    def display_info(self):
        print("Account Name is: " + self.account_name)
        print("The type of account is: " + self.account_type)
        print("Account ID is: " + str(self.account_id))

#setup customer1
customer1 = BankCustomer(1000002,"Sanjay","Patel")

#setup customer2
customer2 = BankCustomer(1000003,"Sandya","Rao")

#setup customer3
customer3 = BankCustomer(1000004,"Rachana","Iyer")

#setup account1
account1 = BankAccount(1000002,"Sanjay's account","Saving" )

customer1.display_info()
customer2.display_info()
customer3.display_info()
account1.display_info()
