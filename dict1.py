#To count no. of letters in word
n=str(input("enter the string: "))
temp={}
for i in n:
    if i in temp:
        temp[i]=temp[i]+1   #temp[i]-value and i is key
    else:
        temp[i]=1

print("Expected dictionary",temp)
