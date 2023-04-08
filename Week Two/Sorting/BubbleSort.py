def bubbleSort(li):
    for i in range(len(li)-1, 0, -1):
        for j in range(i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

li = [9,2,1,4,3,8,7,6,5]

print(bubbleSort(li))