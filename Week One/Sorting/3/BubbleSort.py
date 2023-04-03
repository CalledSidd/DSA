def bubbleSort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

li = [3,4,5,7,6,8,9,1,2]

print(bubbleSort(li))