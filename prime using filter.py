def check_prime(num):
    flag=False
    if(num>1):
        for i in range(2,num):
            if(num%i)==0:
                flag=True
                break
        if(flag==True):
            return False
        else:
            return True
            
numbers=[1,2,3,4,5,6,7,8,9,10]
prime=list(filter(check_prime,numbers))
print(prime)
