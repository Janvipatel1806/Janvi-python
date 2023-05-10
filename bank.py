class Bank:

    def open(self,ano,cname,clname,balance):
        self.no=ano
        self.cname=cname
        self.clname=clname
        self.balance=balance
        print("Your Account is opend with",self.no,"and balance is",self.balance)

    def deposite(self,amount):
        self.balance=self.balance+amount
        print("Thanks for Deposite money")

    def withdraw(self,amount):
        if(amount<=self.balance):
            self.balance=self.balance-amount
            print("Thanks for Withdraw a money")
        else:
            print("You have insufficent balance")

    def checkbalance(self):
        print("Your Balance is",self.balance)

o1=Bank()
    
while(1):
    print("1.open Account")
    print("2.Deposite money")
    print("3.Withdraw money")
    print("4.check balance")
    print("5.Exit")
    choice=int(input("Enter your choice"))
    if(choice==1):
        o=int(input("Enter the money for open the account"))
        o1.open(123,"Janvi","patel",o)
    elif(choice==2):
        d=int(input("Enter the amount you want to deposite"))
        o1.deposite(d)
    elif(choice==3):
        w=int(input("Enter the amount you want to withdraw"))
        o1.withdraw(w)
    elif(choice==4):
        o1.checkbalance()
    elif:
        break
    else:
        print("Please enter between 1 to 5")
    

    
 
