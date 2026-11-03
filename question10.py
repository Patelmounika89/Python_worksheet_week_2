class BankAccount:
    def __init__(self,Account_number,Account_Holder_name,Balance):
        self.Account_number=Account_number
        self.Account_Holder_name=Account_Holder_name
        self.Balance=Balance
    def deposit(self,Amount):
        if Amount >0:
            self.Balance += Amount
            print("Amount Deposit Successfully!")
            print("Deposite Amount:",Amount)
            print("Current Balance",self.Balance)

        else:
            print("Inavlid Deposit Amount")
    def withdraw(self,Amount):
        if Amount <=0:
            print("Invalid  withdraw Amount") 
        elif Amount > self.Balance:
            print("Insufficient Balance")
        else:
            self.Balance -= Amount
            print("Amount withdraw Successfully!")
            print("Withdraw Amount:",Amount)
            print("Remaining Balance",self.Balance)
    def check_balance(self):
        print("Acc0unt Number:",self.Account_number)
        print("Account Holder Name:",self.Account_Holder_name)
        print("Balance",self.Balance)
bankaccount=BankAccount("5600134210","Mounika",10000)
while True:
    print("#####Bank Account Menu\n#####")
    print("1.Deposite")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Exit")
    choice=input("Enter your Choice:")
    if choice =="1":
       Amount=int(input("Enter your Deposit Amount"))
       bankaccount.deposit(Amount)
    elif choice =="2":
           Amount=int(input("Enter your Withdraw Amount"))
           bankaccount.withdraw(Amount)
    elif choice =="3":
           bankaccount.check_balance()
    elif choice =="4":
           print("Thank you for using our banking service")
    else:
         print("Invalid Choice")
  

        

