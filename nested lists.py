def findsecMax(records):
    '''min_=list()
    l=len(records)
    print(l)'''
    temp=list()
    [temp.append(i) for i in records if i not in temp]
    firstmax=max(temp)
    temp.remove(firstmax)
    sec_max=max(temp)
    check_sec_max(temp,sec_max)

def check_sec_max(temp,sec_max):
    l=len(temp)
    for i in temp:
        while(se
    


'''def recursive_loop(records):
    max_count=list()
    temp=list()
    temp=records
    
    for i in range(len(temp)):
        t_max=0
        t_max=max(temp)
        temp.remove(t_max)'''
        
        
        
        
    
    

if __name__ == '__main__':
    n=int(input())
    records=list()
    for i in range(n):
        records.append([])
        for j in range(1):
            name=str(input())
            records[i].append(name)
            mark=float(input())
            records[i].append(mark)
    findsecMax(records)
            
            
