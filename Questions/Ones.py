def pattern(li):
    stack = []
    value = li[0]
    n = len(li)
    for i in range(n):
        if li[i] == value:
            stack.append(li[i])
            value = (value + 1) % 2
        else:
            return False
    print(stack[:2])
    return True

elements = [
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [1,0,0,1,0,1,0,1],
]
for element in elements:
    print(pattern(element))
