class CheckingAccount:
    type = "checking"

    def __init__(self, id, balance):
        self.account_id = id
        self.balance = balance


ch1 = CheckingAccount("ID13434", 120000)
ch2 = CheckingAccount("ID13435", 180000)

print(ch1.type)
print(ch2.type)

#In this code we created a class CheckingAccount with instance attributes id and balance
#and one class attribute called type, which is assigned the value “ checking.”
# That means that all objects created from the CheckingAccount class will have the same value for type