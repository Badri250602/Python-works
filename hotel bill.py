class hotel:

    def __init__(self):
        print("Welcome to ABC Hotel")
        print("*********************")
        self.acc_ids={"badri@xyz.com":"12345","karthi@abc.com":"67890","ranjith@lmn.com":"34567"}

    def login(self):
        self.id=str(input("Enter the user id: "))
        self.password=str(input("Enter the password: "))
        i=0
        for i in self.acc_ids:
            if((self.id==i)and(self.password==self.acc_ids[i])):
                self.login="successfull"
                print("Login successfull!!")
            else:
                pass

class h_menu(hotel):

    def menu(self):
        if(self.login=="successfull"):
            self.item=["Biriyani","Meals","FriedRice","Grilled","BBQ"]
            self.amount=[100,70,150,300,350]
            self.lth=len(self.item)
            j=0
            for j in range(0,self.lth):
                print(" ",self.item[j],"-"," ",self.amount[j])
        else:
            print("Error!!")

    def choice(self):
        if(self.login=="successfull"):
            c='y'
            j=0
            self.i_item=[0]*10
            self.i_quan=[0]*10
            x=0
            while(c=='y'):
                self.i_item[j]=str(input("Enter the item name: "))
                self.i_quan[j]=int(input("Enter the quantity: "))
                for k in range(0,self.lth):
                    if(self.i_item[j]==self.item[k]):
                        print("Price of the item: ",self.amount[k])
                    else:
                        pass
                        
                
                
                '''while(x!=j):
                    for k in self.m:
                        if((self.item[j]==k)):
                            print("Price: ",self.m[k])
                        else:
                            print("Item is not found!!")'''
        
                j=j+1
                c=str(input("Do you want to continue??y/n: "))
        else:
            print("Error!!")

    def available(self):
        if(self.login=="successfull"):
            self.av_item=["Biriyani","Meals"]
            self.av_amt=[100,70]
            self.lth2=len(self.av_item)
            
            
            '''self.av={"Biriyani":100,"Meals":70}'''
            print("AVAILABLE: ")
            l=0
            for l in range(0,self.lth2):
                print(" ",self.av_item[l],"-"," ",self.av_amt[l])
        else:
            print("Error!!")

    def choice2(self):
        if(self.login=="successfull"):
            m=0
            x=0
            self.f_item=[0]*10
            self.f_quan=[0]*10
            self.f_amt=[0]*10
            c2='y'
            while(c2=='y'):
                self.f_item[m]=str(input("Enter the item: "))
                if(self.f_item[m] in self.av_item):
                    for x in range(0,self.lth2):
                        if(self.f_item[m]==self.av_item[x]):
                            self.f_quan[m]=int(input("Enter the quantity: "))
                            self.f_amt[m]=self.av_amt[x]
                            m=m+1
                        else:
                            pass
                else:
                    print("Sorry your item is not available right now!!") 
                c2=str(input("Do you want to continue??y/n: "))
            self.m=m
        else:
            print("Error!!")

    def price(self):
        if(self.login=="successfull"):
            n=0
            self.f_price=0
            for n in range(0,self.m):
                self.f_price=self.f_price+(self.f_quan[n]*self.f_amt[n])
                '''self.f_price=self.f_price+(self.quan[n]*self.av[o])'''
                    

            self.totprice=self.f_price
            print("Original Price= ",self.totprice)
            self.gst=((12/self.totprice)*100)
            print("GST 12%= ",self.gst)
            self.totprice=self.totprice-self.gst
            print("Total Amount:Rs. ",self.totprice)


obj=h_menu()
obj.login()
obj.menu()
obj.choice()
obj.available()
obj.choice2()
obj.price()
            
            
                
        
        
            
        
    
        
        
            
        
        
    
        
