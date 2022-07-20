def mergeSort(arr,n):
    if(n>1):  #checking size of array
        r=n//2    #dividing into two subarrays
        L=arr[:r]  #left subarray in L[]
        R=arr[r:]   #right subarray in R[]
        mergeSort(L,len(L))
        mergeSort(R,len(R))
        merge(arr,L,R)

def merge(arr,L,R):
    i=j=k=0
    while(i<len(L) and j<len(R)):
        if(L[i]<=R[j]):
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    while(i<len(L)):
        arr[k]=L[i]
        i+=1
    while(j<len(R)):
        arr[k]=R[j]
        j+=1

def printArray(arr):
    i=0
    print("Sorted Array: ",end="\n")
    for i in range(len(arr)):
        print(arr[i],end=" ")


if __name__=='__main__':
    n=int(input("Enter the size of array: "))
    arr=[int(i) for i in input().split()]
    mergeSort(arr,n)
    printArray(arr)
