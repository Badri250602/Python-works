def checkvowel(string):
    print(string)
    c=0
    for i in string:
        if((i.lower() in "aeiou") or (i.upper() in "aeiou")):
            c+=1 
    return c 
    

names=[str(i)  for i in input().split()]
count=list(map(checkvowel,names))
print(count)
