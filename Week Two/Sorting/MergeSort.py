def mergeSort(li):
    if len(li)>1:
        n = len(li)
        left = li[:n//2]
        right = li[n//2:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                li[k] = left[i]
                i += 1
            else:
                li[k] = right[j]
                j += 1 
            k += 1

        while i < len(left):
            li[k] = left[i]
            i += 1
            k += 1 
        
        while j < len(right):
            li[k] = right[j]
            j += 1
            k += 1

        return li

li = [9,7,6,8,2,3,1,4,5]
print(mergeSort(li))