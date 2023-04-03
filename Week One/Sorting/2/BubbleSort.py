def bubbleSort(li):
    n = len(li)
    for i in range(n-1):
        for j in range(n-1-i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li


li = [9,1,2,8,7,5,6,4,3]
print(bubbleSort(li))