if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
i=0
'''a=[int for int in range(x)]
b=[int for int in range(y)]
c=[int for int in range(z)]'''
j=0
k=0
a=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
print(a)

