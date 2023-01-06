def check_transaction_limit(amount):
    if amount>10000:
        print("Above transaction limit.")
    else:
        print("Transaction is within the limit.")

check_transaction_limit(5600)
check_transaction_limit(15500)