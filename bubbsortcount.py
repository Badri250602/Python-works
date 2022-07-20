def bubblesort(arr,n):
    c=0
    swapped=True
    while(swapped is not False):
        swapped=False
        c=c+1
        for i in range(n-1):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swapped=True
    print(arr)
    return c




n=int(input())
arr=[int(i) for i in input().split()]
count=0
count=bubblesort(arr,n)
print(count)