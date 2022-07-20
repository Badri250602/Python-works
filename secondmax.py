def runnerUp(arr,n):
    temp=[]
    [temp.append(i) for i in arr if i not in temp]
    firstmax=max(temp)
    temp.remove(firstmax)
    secondmax=max(temp)
    return secondmax





if __name__=='__main__':
    n=int(input())
    arr=[int(i) for i in input().split()]
    sec_max=runnerUp(arr,n)
    print(sec_max)
