def selectionSort(list):
    print(li)
    for i in range(0, len(list)-1):
        minpos = i 
        for j in range(i, len(list)):
            if list[j] < list[minpos]:
                minpos = j 
        list[i], list[minpos] = list[minpos], list[i]
    return list


li = [8,6,9,7,2,3,1,4,5]
print(selectionSort(li))