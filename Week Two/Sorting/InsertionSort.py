# o(n2)

def insertionSort(li):
    n = len(li)
    for i in range(1, n):
        j = i 
        while li[j-1] > li[j] and j>0:
            li[j-1], li[j] = li[j], li[j-1]
            j -= 1
    return li



li = [7,8,6,9,4,3,1,2]
print(insertionSort(li))