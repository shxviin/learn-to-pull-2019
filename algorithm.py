def insertion(A):
    n = len(A)
    for j in range(1,n):
        key=A[j]
        i=j-1
        while (i>0 and A[i]>key):
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
   



def BubbleSort(A):
    n= len(A)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if (A[j] < A[j-1]):
               temp=A[j]
               A[j]=A[j-1]
               A[j-1]=temp




def SSort(A):
    n = len(A)
    for j in range(n-1):
        small = j
        for i in range(j+1,n):
            if A[i] > A[small]:
                small = i
        temp = A[j]
        A[j]= A[small]
        A[small] = temp





a=[]
for i in range(8):
    x=int(input('Enter number: '))
    a.append(x)
print(a)
##insertion(a)
BubbleSort(a)
print(a)
