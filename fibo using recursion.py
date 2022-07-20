def fibo(n):
    if(n<=1):
        return n
    else:
        return (fibo(n-1)+fibo(n-2))

nterms=int(input("Enter the number of terms: "))

if(nterms<=0):
    print("Error!!")
else:
    print("Fibonacci Series: ")
    for i in range(0,nterms):
        print(fibo(i))
