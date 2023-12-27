class Atm:
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self,amount):
        self.amount=amount
        if self.amount<0:
            return "Invalid Amount"
        else:
            self.balance=self.balance+self.amount
            return f"{self.amount} is successfully Deposit and Your current Balance is : {self.balance}"
    def withdraw(self,amount):
         self.amount=amount
         if self.amount<0:
            return "Invalid Amount"
         elif self.amount>self.balance:
             return "Your current balance is insufficent"
         else:
             self.balance=self.balance-self.amount
             return f"{self.amount} is successfully withdraw and Your current Balance is : {self.balance}"
    
    def __str__(self):
        return f"Your current balance is {self.balance}"

      
        

my_atm=Atm(500)    
my_atm=Atm(500)    
 
def display_menu():
    print("\n\n**********Atm Menu**********")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    



while True:
    
    display_menu()
    choice = input('Enter Your choice (1-4) : ')
    try:
        if choice=="1":
            print(my_atm)
        elif choice=="2":
            amount=float(input('Enter the Amount for Deposit :'))
            print(my_atm.deposit(amount))
        elif choice=="3":
            amount=float(input('Enter the Amount for Withdraw :'))
            print(my_atm.withdraw(amount))
            
        elif choice=="4":
            print("Thank for Using ATM :)")
            break
    except Exception as e:
        print(e)
    