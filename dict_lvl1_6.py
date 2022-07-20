#UNFINISHED!!
'''#dictionary to sort based on no of occurence of input str in given str:
given_str=eval(input("Enter the list: "))

inp_str=str(input("Enter the string: "))

temp={} #initialising a dictionary

for i in given_str:
    count=0
    for j in i.split():
        if(j==inp_str):
            count=count+1
    temp[count]=i

print(temp)


out_str=[] #initialising a list
x=0


for k in sorted(temp):  #sorted() function is used to sort a dictionary/list in ascending order
    out_str.insert(x,temp[k])
    x=x+1

print("Output string: ",out_str)'''

#demo1
a=eval(input("Dict: "))
b=[0]*(len(a))
print(b)
for i in a:
    print(i)
    print(a[i])

    
    
