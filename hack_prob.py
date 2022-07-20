
n=int(input())
x=0
for i in range(0,n+1):
    if(i>9):
        if(i==(n+1)):
            x=x+i
        else:
            x=(x*100)+i
    else:
        x=(x*10)+i
    
print(x)
