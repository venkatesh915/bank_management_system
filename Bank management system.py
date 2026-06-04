class BankAccount:
    def __init__(self,acc_no,name,mobile,email,acc_type,branch,ifsc,balance):
        self.acc_no = acc_no
        self.name = name
        self.mobile = mobile
        self.email = email
        self.acc_type = acc_type
        self.branch = branch
        self.ifsc =ifsc
        self.transaction_count = 0
        self.status = "active"
        self.withdraw_count = 0
        self.deposit_count = 0
        self.balance = balance

    def display(self):
        print("===============Bank Account Details=====================")
        print("Account Number:",self.acc_no)
        print("Customer name:",self.name)
        print("Account mobile:",self.mobile)
        print("Account email:",self.email)
        print("Account Type",self.acc_type)
        print("Account Branch",self.branch)
        print("Account ifsc code:",self.ifsc)
        print("Transactions ",self.transaction_count)
        print("Status:",self.status)

    def deposit(self,amount):
        if self.status =="closed":
            print("Account is closed, Please Activate to deposit ")
            return
        if amount >0:
            self.balance += amount
            print("Deposit successful")
            self.transaction_count +=1
            self.deposit_count +=1
        else:
            print("Deposit amount must be greater than 0")

    
    def withdraw(self,amount):
        if self.status =="closed":
            print("Account is closed, Please Activate to withdraw ")
            return
        
        if self.balance - amount >= 1000 and amount>=50:
            print("Withdraw successful")
            self.transaction_count +=1
            self.withdraw_count +=1
            self.balance -= amount
        else:
            print(" Enter minimum withdraw amount 50 and Minimum balance 1000 required ")
           
    
    def check_balance(self):
        print("Current balance:",self.balance)

    def transfer_money(self,receiver,amount):
        if self.status =="closed":
            print("Account is closed ")
            return
        if receiver.status =="closed":
            print("Receiver Account is closed ")
            return
        if amount <= 0:
            print("Invalid transfer amount")
            return
        if self.balance - amount >= 1000:
            print("Amount Transferred")
            self.balance -= amount
            receiver.balance += amount
            self.transaction_count +=1
            self.withdraw_count +=1
            receiver.deposit_count +=1
            receiver.transaction_count +=1
            print("Money transferred successfully")
        else:
            print("Insufficient balance ")
        
    def update_details(self,name,mobile,email):
        self.name = name
        self.mobile = mobile     
        self.email = email
        print("Successfully updated ")
    def transaction_summary(self):
        print("=========Transaction Summary=======")
        print("Total withdraws = ", self.withdraw_count)
        print("Total deposit count :",self.deposit_count)
        print("Transaction count",self.transaction_count)
        
    def calculate_interest(self):
        if self.acc_type == "savings":
            interest = self.balance * 4 /100
            print("Interest amount:",interest)
        else:
            print("Interest only for savings account")

    

    def close_account(self):
        self.status = "closed"
        print("Account closed successfully")
    def reopen_account(self):
        self.status = "active" 
        print("Account reopened successfully")

accounts = []

def create_account():
    acc_no = int(input("Enter account number:"))
    for acc in accounts:
        if acc.acc_no == acc_no:
            print("Account number already exits")
            return
    name = input("Enter customer name:")
    mobile = input("Enter mobile number:")
    email = input("Enter mail id:")
    acc_type = input("Enter account type (savings/current)")
    branch = input("Enter account branch:")
    ifsc = input("Enter ifsc code:")
    balance = float(input("Enter inital amount:"))
    if balance <= 1000:
        print("Minimum deposit is 1000")
        return
    acc=BankAccount(acc_no,name,mobile,email,acc_type,branch,ifsc,balance)

    accounts.append(acc)
    print("Account created successfully")

def view_accounts():
    if len(accounts) == 0:
        print("No accounts found")
    else:
        for acc in accounts:
            acc.display()

def search_account():
    acc_no = int(input("Enter account number:"))
    for acc in accounts:
        if acc_no == acc.acc_no:
            acc.display()
            return acc
    print("Account  not found")
    return None

def deposit_money():
    acc = search_account()

    if acc:
        amount = float(input("Enter deposit amount:"))
        acc.deposit(amount)

def withdraw_amount():
    acc = search_account()
    if acc:
        amount = float(input("Enter withdraw amount:"))
        acc.withdraw(amount)

def check_balance():
    acc = search_account()
    if acc:

        acc.check_balance()
    


def transfer_money():

    sender_no =int(input("Enter sender account number:"))
    receiver_no =int(input("Enter receiver account number:"))

    sender = None
    receiver = None
    for acc in accounts:
        if acc.acc_no ==sender_no:
            sender =acc
        if acc.acc_no ==receiver_no:
            receiver = acc

    if sender is None:
        print("Sender account not found")
        return
    if receiver is None:
        print("Receiver account not found")
        return
    amount = float(input("Enter transfer amount:"))

    sender.transfer_money(receiver,amount)


def update():
    acc = search_account()
    if acc:
        name = input("Enter customer name:")
        mobile = input("Enter mobile number:")
        email = input("Enter mail id:")

        acc.update_details(name,mobile,email)


def transaction_summary():
    acc = search_account()
    if acc: 
        acc.transaction_summary()

def calculate_interest():
    acc = search_account()
    if acc: 
        acc.calculate_interest()


def close_account(): 
    acc = search_account() 
    if acc: 
        acc.close_account()

def reopen_account(): 
    acc = search_account() 
    if acc: 
        acc.reopen_account()  

def top_account_holder(): 
    if len(accounts) == 0: 
        print("No accounts available") 
        return 
    top = accounts[0] 
    for acc in accounts: 
        if acc.balance > top.balance: 
            top = acc 
    print("Top Account Holder") 
    top.display()


def bank_statistics():

    total_accounts = len(accounts)

    active_accounts = 0
    closed_accounts = 0
    total_bank_balance = 0

    for acc in accounts:

        if acc.status =="active":
            active_accounts += 1
        else:
            closed_accounts += 1

        total_bank_balance += acc.balance

    if total_accounts > 0:
        average_balance =total_bank_balance / total_accounts
    else:
        average_balance = 0

    print("\n=========BANK STATISTICS=========")

    print("Total Accounts:",total_accounts)
    print("Active Accounts:",active_accounts)
    print("Closed Accounts:",closed_accounts)
    print("Total Bank Balance:",total_bank_balance)
    print("Average Account Balance:",average_balance)   


while True:
    print("\n===================================") 
    print("BANK MANAGEMENT SYSTEM") 
    print("===================================") 
    print("1. Create Account") 
    print("2. View Accounts") 
    print("3. Search Account") 
    print("4. Deposit Money") 
    print("5. Withdraw Money") 
    print("6. Check Balance") 
    print("7. Transfer Money") 
    print("8. Update Customer Details") 
    print("9. Transaction Summary") 
    print("10. Calculate Interest") 
    print("11. Close Account") 
    print("12. Reopen Account") 
    print("13. Top Account Holder") 
    print("14. Bank Statistics") 
    print("15. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1: 
        create_account()
    elif choice == 2: 
        view_accounts()
    elif choice == 3: 
        search_account()
    elif choice == 4: 
        deposit_money()
    elif choice == 5: 
        withdraw_amount()
    elif choice == 6: 
        check_balance()
    elif choice == 7: 
        transfer_money()
    elif choice == 8: 
        update()
    elif choice == 9: 
        transaction_summary()
    elif choice == 10: 
        calculate_interest()
    elif choice == 11: 
        close_account()
    elif choice == 12: 
        reopen_account()
    elif choice == 13: 
        top_account_holder()
    elif choice == 14: 
        bank_statistics()
    elif choice == 15:
        print("Thank You") 
        break
    else: 
        print("Invalid choice")  



"""  OUTPUT
===================================
BANK MANAGEMENT SYSTEM
===================================
1. Create Account
2. View Accounts
3. Search Account
4. Deposit Money
5. Withdraw Money
6. Check Balance
7. Transfer Money
8. Update Customer Details
9. Transaction Summary
10. Calculate Interest
11. Close Account
12. Reopen Account
13. Top Account Holder
14. Bank Statistics
15. Exit
Enter choice: 1
Enter account number:123
Enter customer name:venky
Enter mobile number:123456963
Enter mail id:venky@gmail.com
Enter account type (savings/current)savings
Enter account branch:chirala
Enter ifsc code:12345567
Enter inital amount:50000
Account created successfully

===================================
BANK MANAGEMENT SYSTEM
===================================
1. Create Account
2. View Accounts
3. Search Account
4. Deposit Money
5. Withdraw Money
6. Check Balance
7. Transfer Money
8. Update Customer Details
9. Transaction Summary
10. Calculate Interest
11. Close Account
12. Reopen Account
13. Top Account Holder
14. Bank Statistics
15. Exit
Enter choice: 6
Enter account number:123
===============Bank Account Details=====================
Account Number: 123
Customer name: venky
Account mobile: 123456963
Account email: venky@gmail.com
Account Type savings
Account Branch chirala
Account ifsc code: 1234567
Transactions  0
Status: active
Current balance: 50000.0

===================================
BANK MANAGEMENT SYSTEM
===================================
1. Create Account
2. View Accounts
3. Search Account
4. Deposit Money
5. Withdraw Money
6. Check Balance
7. Transfer Money
8. Update Customer Details
9. Transaction Summary
10. Calculate Interest
11. Close Account
12. Reopen Account
13. Top Account Holder
14. Bank Statistics
15. Exit
Enter choice: 13
Top Account Holder
===============Bank Account Details=====================
Account Number: 123
Customer name: venky
Account mobile: 123456963
Account email: venky@gmail.com
Account Type savings
Account Branch chirala
Account ifsc code: 1234567
Transactions  0
Status: active

===================================
BANK MANAGEMENT SYSTEM
===================================
1. Create Account
2. View Accounts
3. Search Account
4. Deposit Money
5. Withdraw Money
6. Check Balance
7. Transfer Money
8. Update Customer Details
9. Transaction Summary
10. Calculate Interest
11. Close Account
12. Reopen Account
13. Top Account Holder
14. Bank Statistics
15. Exit
Enter choice: 2
===============Bank Account Details=====================
Account Number: 123
Customer name: venky
Account mobile: 123456963
Account email: venky@gmail.com
Account Type savings
Account Branch chirala
Account ifsc code: 1234567
Transactions  0
Status: active

===================================
BANK MANAGEMENT SYSTEM
===================================
1. Create Account
2. View Accounts
3. Search Account
4. Deposit Money
5. Withdraw Money
6. Check Balance
7. Transfer Money
8. Update Customer Details
9. Transaction Summary
10. Calculate Interest
11. Close Account
12. Reopen Account
13. Top Account Holder
14. Bank Statistics
15. Exit
Enter choice: 4
Enter account number:123
===============Bank Account Details=====================
Account Number: 123
Customer name: venky
Account mobile: 123456963
Account email: venky@gmail.com
Account Type savings
Account Branch chirala
Account ifsc code: 1234567
Transactions  0
Status: active
Enter deposit amount:1500
Deposit successful

===================================
BANK MANAGEMENT SYSTEM
===================================
1. Create Account
2. View Accounts
3. Search Account
4. Deposit Money
5. Withdraw Money
6. Check Balance
7. Transfer Money
8. Update Customer Details
9. Transaction Summary
10. Calculate Interest
11. Close Account
12. Reopen Account
13. Top Account Holder
14. Bank Statistics
15. Exit
Enter choice: 6
Enter account number:123
===============Bank Account Details=====================
Account Number: 123
Customer name: venky
Account mobile: 123456963
Account email: venky@gmail.com
Account Type savings
Account Branch chirala
Account ifsc code: 1234567
Transactions  1
Status: active
Current balance: 51500.0

===================================
BANK MANAGEMENT SYSTEM
===================================
1. Create Account
2. View Accounts
3. Search Account
4. Deposit Money
5. Withdraw Money
6. Check Balance
7. Transfer Money
8. Update Customer Details
9. Transaction Summary
10. Calculate Interest
11. Close Account
12. Reopen Account
13. Top Account Holder
14. Bank Statistics
15. Exit
Enter choice: 15
Thank You"""

       
