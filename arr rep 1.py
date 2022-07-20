#NOT UNDERSTOOD!!!

import array as arr  #creating python arrays
def getFirst(y):
    while(y>=10):
        y=y//10
    return y

def getLast(y):
    y=y%10
    return y
n=int(input())
x=eval(input())
a=arr.array('i',x)       #creating array in integer type
b=arr.array('i',[0]*(int)(len(a)/2)) #initialising b as [0,0]
print(b)
s=len(a)
j=0
k=(s//2)-1
'''for j in range(0,s+1):
    b[k]=a[j]
    k=k+1'''
while(k<s):
    b[k]=a[j]
    k=k+1
    j=j+1

print(b)
l=0
t1=0
for l in range(0,n):
    if(l<(int)(n/2)):
        t1=(t1*10)+getFirst(a[l])
    else:
        t1=(t1*10)+getLast(b[l-(int)(n/2)])

print(t1)

