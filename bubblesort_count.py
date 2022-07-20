'''def bubbleSort(arr,n):
    c=0
    for i in range(n-1):
        swapped=False
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
                c=c+1
        if not swapped:
            break
    return c

n=int(input())
arr=[int(i) for i in input().split()]
count=0
count=bubbleSort(arr,n)
print(count)'''



#Programiz code
'''def bubbleSort(array):
    
  # loop through each element of array
  for i in range(len(array)):
        
    # keep track of swapping
    swapped = False
    
    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping occurs if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

        swapped = True
          
    # no swapping means the array is already sorted
    # so no need for further comparison
    if not swapped:
      break

data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)'''



#Own code
def bubbleSort(arr,n):
    c=0
    swapped=True
    while(swapped is not False):
        swapped=False
        c=c+1
        for i in range(n-1):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swapped=True
    return c



n=int(input())
arr=[int(i) for i in input().split()]
count=0
count=bubbleSort(arr,n)
print(count)
