def bubbleSort(A):
    for i in range(0, len(A)-1):
        for j in range(0, len(A)-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A 

li = [2,5,8,7,1,3,9,4]
print(li)
k = bubbleSort(li)
print(li)