pos = -1 


def search(list, n):
    l = 0
    u = len(list)-1 

    while l <= u:
        mid = (l+u) // 2 

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid;
            else:
                u = mid

# list = [2,3,4,5,6,7,8,9,0]
list = [2,3,5,6,7,9,1,2]
n = 6

if search(list, n):
    print("Found at Position", pos+1)
else:
    print("Not Found")