'''#1
length=eval(input("Values of length: "))
breadth=eval(input("Values of breadth: "))
m=len(length)
for i in range(0,m):
    if(length[i]==breadth[i]):
        print(" ",length[i],"and"," ",breadth[i],"forms a square!!")
    else:
        print("Not a square!!")'''


'''#2a
n1=eval(input("List1: "))
n2=eval(input("List2: "))
x=len(n1)
for i in range(0,x):
    if(n1[i]>n2[i]):
        print(" ",n1[i],"is greater than"," ",n2[i])
    else:
        print(" ",n2[i],"is greater than"," ",n1[i])'''

'''#2b
n1=eval(input("List1: "))
n2=eval(input("List2: "))
n3=eval(input("List3: "))
y=len(n1)
for i in range(0,y):
    if(n1[i]>n2[i]):
        if(n1[i]>n3[i]):
            print(" ",n1[i],"is greatest!!")
        else:
            print(" ",n3[i],"is greatest!!")
    elif(n1[i]<n2[i]):
        if(n2[i]>n3[i]):
            print(" ",n2[i],"is greatest!!")
        else:
            print(" ",n3[i],"is greatest!!")'''

'''#3
quan=eval(input("Quantities of items: "))
z=len(quan)
price=[0]*z
totprice=0
for i in range(0,z):
    price[i]=(quan[i]*100)

    if(price[i]>500):
        dis_price=price[i]*(10/100)
        price[i]=price[i]-dis_price        
    totprice=totprice+price[i]

print(price)
print("Totalprice= ",totprice)'''

'''#4
salary=eval(input("Salaries of employee: "))
year=eval(input("Years of experience: "))
a=len(year)
for i in range(0,a):
    if(year[i]>5):
        dis_sal=0.05*salary[i]
        salary[i]=(salary[i]+dis_sal)
print(salary)'''


#4a
emp=eval(input("Data: "))
sal=[0]*(len(emp))
j=0
for i in emp:
    sal[j]=emp[i]
    j+=1
dis_sal=[0]*(len(emp))
k=0
for i in emp:
    if(i>5):
        dis_sal[k]=0.05*sal[k]
        sal[k]=sal[k]+dis_sal[k]
    k+=1
print(sal)
    

















        

    
