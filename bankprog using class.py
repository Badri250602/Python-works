class bank:
    def deposit(self,cb):
        self.cb=cb
        self.deposit=int(input("Enter the money to be added: "))
        self.cb+=self.deposit
        return self.cb
    def withdrawal(self,cb):
        self.cb=cb
        self.withdraw=int(input("Enter the money to be taken: "))
        self.cb-=self.withdraw
        return self.cb
    def currbal(self,cb):
        self.cb=cb
        return self.cb


cb=int(input("Enter the current balance: "))
c='y'
obj1=bank()
while(c=='y'):
    pref=int(input("1-Deposit 2-Withdrawal 3-Current balance"))
    if(pref==1):
        cb=obj1.deposit(cb)
        print("Deposited amt: ",cb)
    elif(pref==2):
        cb=obj1.withdrawal(cb)
        print("Withdrawed amt: ",cb)
    elif(pref==3):
        cb=obj1.currbal(cb)
        print("Current bal: ",cb)
    else:
        print("Wrong data entry!!")

    c=str(input("Do you want to continue?? y-Yes n-No"))
    
        
