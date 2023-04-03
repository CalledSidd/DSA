def selectionSort(A):
    for i in range(0, len(A)-1):
        minIndex = i 
        for j in range(i+1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j 
        if minIndex != i:
            A[i], A[minIndex] = A[minIndex], A[i]

li = [2,5,8,7,1,3,9,4]
print(li)
k = selectionSort(li)
print(li)