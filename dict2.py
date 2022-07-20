#dictionary to sort the items in ascending order:
given_str=eval(input("Enter the list: "))

inp_str=str(input("Enter the string: "))

temp={} #initialising a dictionary

for i in given_str:
    count=0
    for j in i.split():
        if(j==inp_str):
            count=count+1
    temp[count]=i

out_str=[] #initialising a list

for k in sorted(temp):  #sorted() function is used to sort a dictionary/list in ascending order
    out_str.append(temp[k])

print("Output string: ",out_str)

    
    
