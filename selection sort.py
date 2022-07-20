def selectionSort(arr,n):
    for i in range(n):
        min_=i
        for j in range(i+1,n):
            if(arr[j]<arr[min_]): #ascending order
                min_=j
        arr[i],arr[min_]=arr[min_],arr[i]  #swapping the min and the smallest element

n=int(input())
arr=[0]*n
i=0
for i in range(n):
    arr[i]=int(input())
    i=i+1

selectionSort(arr,n)
print("Sorted Array: ")
print(arr)
