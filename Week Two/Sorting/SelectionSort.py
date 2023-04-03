def selectionSort(li):
    n = len(li)
    for i in range(0, n-1):
        min_index = i 
        for j in range(i+1, n):
            if li[j] < li[min_index]:
                min_index = j
        li[i], li[min_index] = li[min_index], li[i]
        
    return li

li = [8,9,5,6,4,1,2,3]

print(selectionSort(li))