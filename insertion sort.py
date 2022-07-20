def insertionSort(arr,n):
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while((key<arr[j])and(j>=0)):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key


n=int(input())
arr=[0]*n
i=0
for i in range(0,n):
    arr[i]=int(input())
    i=i+1
insertionSort(arr,n)
print("Sorted Array: ");
print(arr)
