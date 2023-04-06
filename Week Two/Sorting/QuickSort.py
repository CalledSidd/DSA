def quickSort(li, left, right):
    if left < right:
        partition_pos = partiton(li, left, right)
        quickSort(li, left, partition_pos-1)
        quickSort(li, partition_pos+1, right)

def partiton(li, left, right):
    i = left
    j = right - 1
    pivot = li[right]

    while i < j:
        while i < right and li[i] < pivot:
            i += 1 
        while j > left and li[j] >= pivot:
            j -= 1
        if j < j:
            li[i], li[j] = li[j], li[i]

    if li[i] > pivot:
        pass



li = [1,2,3,4,9,8,7,6]
print(quickSort(li))