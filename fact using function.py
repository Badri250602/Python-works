def factorial(n):
    if(n==1):
        return n
    else:
        return (n*factorial(n-1))

n=int(input("Enter the number: "))
fact=factorial(n)
print("Factorial of ",n,"is: ",fact)
