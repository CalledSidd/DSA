# Swapping method
def insertionSort(A):
    for i in range(1, len(A)):
        j = i-1 
        while A[j] > A[j+1] and j>=0:
            A[j], A[j+1] = A[j+1], A[j]
            j -= 1

# Shifting Method 
def insertion_sort(A):
    for i in range(1, len(A)):
        curNum = A[i] 
        for j in range(i-1, 0, -1):
            if A[j] > curNum:
                A[j+1] = A[j]
            else:
                A[j+1] = curNum
                break

li = [2,5,8,7,1,3,9,4]
print(li)
k = insertionSort(li)
print(li)

# Time complexity of Insertion sort is O(n^2)