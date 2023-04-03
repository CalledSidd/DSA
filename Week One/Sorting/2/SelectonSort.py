def selectionSort(list):
    print(list)
    n = len(list)
    for i in range(n-1):
        min = i
        for j in range(min+1,n):
            if list[j] < list[min]:
                min = j 
        if i != min:
            list[i], list[min] = list[min], list[i]
    return list

li = [9,1,2,8,7,5,6,4,3]
print(selectionSort(li))