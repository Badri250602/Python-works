dict1={"food1":20,"food2":50,"food3":30}
i=0
c='y'
while(c=='y'):
    item[i]=str(input())
    quan[i]=int(input())
    i=i+1
    c=str(input("y/n: "))
j=0
k=0
for j in (0,i):
    for k in dict1:
    if(item[j]==k):
        
