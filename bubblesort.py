def bubbleSort(arr,n):
    for i in range(n-1):
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]


n=int(input())
arr=[0]*n
i=0
for i in range(0,n):
    arr[i]=int(input())
    i=i+1

bubbleSort(arr,n)
print("Sorted array: ",end='\n')
print(arr)
